#!/usr/bin/env python2
# Run the foresting configuration on PbPb in CMSSW_5_3_X, using the new HF/Voronoi jets
# Author: Alex Barbieri
# Date: 2013-10-15

#####################################################################################
# commandline arguments
#####################################################################################
import FWCore.ParameterSet.VarParsing as VarParsing

ivars = VarParsing.VarParsing('python')

ivars.register ('randomNumber',
                1,
                ivars.multiplicity.singleton,
                ivars.varType.int,
                "Random Seed")

ivars.randomNumber = 1
#ivars.inputFiles = "file:step3_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_2.root"
ivars.inputFiles = "file:/mnt/hadoop/cms/store/user/yilmaz/hydjetTuneDrum_QuenchedMB_53X_GEN-SIM_v2/Hydjet_Drum_53X_RECO_test16/16a66057d6b9b6b77f83d561b8cd7aea/step3_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_87_1_v07.root"
ivars.outputFile = 'HiForest.root'
ivars.maxEvents = 10

ivars.parseArguments()

hiTrackQuality = "highPurity"              # iterative tracks
#hiTrackQuality = "highPuritySetWithPV"    # calo-matched tracks

import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet(
    # wantSummary = cms.untracked.bool(True)
    #SkipEvent = cms.untracked.vstring('ProductNotFound')
)

#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("CmsHi.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",
)
process.HiForest.HiForestVersion = cms.untracked.string("PbPb_53X_Voronoi")

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(ivars.inputFiles))

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(ivars.maxEvents))


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# PbPb 53X MC
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:starthi_HIon', '')

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import *
overrideGT_PbPb2760(process)
overrideJEC_pp2760(process)

process.HeavyIonGlobalParameters = cms.PSet(
    centralityVariable = cms.string("HFtowers"),
    nonDefaultGlauberModel = cms.string(""),
    centralitySrc = cms.InputTag("hiCentrality")
    )

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string(ivars.outputFile))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

process.load('Configuration.StandardSequences.Generator_cff')
process.load('RecoJets.Configuration.GenJetParticles_cff')
process.load('RecoHI.HiJetAlgos.HiGenJets_cff')
process.load('RecoHI.HiJetAlgos.HiRecoJets_cff')
process.load('RecoHI.HiJetAlgos.HiRecoPFJets_cff')

process.hiGenParticles.srcVector = cms.vstring('generator')


process.load('CmsHi.JetAnalysis.jets.HiGenJetsCleaned_cff')

process.load('CmsHi.JetAnalysis.jets.akVs3PFJetSequence_PbPb_mc_cff')
process.load('CmsHi.JetAnalysis.jets.akPu3PFJetSequence_PbPb_mc_cff')

process.load('CmsHi.JetAnalysis.jets.akVs3CaloJetSequence_PbPb_mc_cff')
process.load('CmsHi.JetAnalysis.jets.akPu3CaloJetSequence_PbPb_mc_cff')

process.load('CmsHi.HiHLTAlgos.hievtanalyzer_mc_cfi')
process.load('CmsHi.JetAnalysis.HiGenAnalyzer_cfi')

process.load('CmsHi.JetAnalysis.ExtraTrackReco_cff')
process.load('CmsHi.JetAnalysis.ExtraPfReco_cff')
process.load('CmsHi.JetAnalysis.TrkAnalyzers_MC_cff')
process.load("MitHig.PixelTrackletAnalyzer.METAnalyzer_cff")
process.load("CmsHi.JetAnalysis.pfcandAnalyzer_cfi")
process.load('CmsHi.JetAnalysis.rechitanalyzer_cfi')
process.rechitAna = cms.Sequence(process.rechitanalyzer+process.pfTowers)
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0

#########################
# Track Analyzer
#########################
process.anaTrack.qualityStrings = cms.untracked.vstring('highPurity','highPuritySetWithPV')
process.pixelTrack.qualityStrings = cms.untracked.vstring('highPurity','highPuritySetWithPV')
process.mergedTrack.qualityStrings = cms.untracked.vstring('highPurity','highPuritySetWithPV')

#photons
process.RandomNumberGeneratorService.generator.initialSeed = ivars.randomNumber 
process.RandomNumberGeneratorService.multiPhotonAnalyzer = process.RandomNumberGeneratorService.generator.clone()
process.interestingTrackEcalDetIds.TrackCollection = cms.InputTag("hiGeneralTracks")
process.load("RecoEcal.EgammaCoreTools.EcalNextToDeadChannelESProducer_cff")
process.load('CmsHi.JetAnalysis.ExtraEGammaReco_cff')
process.load('CmsHi.JetAnalysis.EGammaAnalyzers_cff')
process.multiPhotonAnalyzer.GenEventScale = cms.InputTag("generator")
process.multiPhotonAnalyzer.HepMCProducer = cms.InputTag("generator")
process.load("edwenger.HiTrkEffAnalyzer.TrackSelections_cff")
process.hiGoodTracks.src = cms.InputTag("hiGeneralTracks")
process.photonStep = cms.Path(process.hiGoodTracks * process.photon_extra_reco * process.makeHeavyIonPhotons)
process.photonStep.remove(process.interestingTrackEcalDetIds)
process.photonMatch.matched = cms.InputTag("hiGenParticles")
process.patPhotons.addPhotonID = cms.bool(False)
process.extrapatstep = cms.Path(process.selectedPatPhotons)
process.multiPhotonAnalyzer.GammaEtaMax = cms.untracked.double(100)
process.multiPhotonAnalyzer.GammaPtMin = cms.untracked.double(10)

process.hiTracks.cut = cms.string('quality("' + hiTrackQuality+  '")')
process.pfTrack.TrackQuality = cms.string(hiTrackQuality)
process.reco_extra =  cms.Path(
    #process.hiTrackReco
    #+process.hiTrackDebug
    
    #        *process.muonRecoPbPb
    process.HiParticleFlowLocalReco
    *process.HiParticleFlowReco
    #*process.iterativeConePu5CaloJets
    *process.PFTowers
)
# set track collection to iterative tracking
process.pfTrack.TkColList = cms.VInputTag("hiGeneralTracks")
process.anaTrack.doSimVertex = False
process.anaTrack.doSimTrack = False
process.mergedTrack.doSimTrack = False
process.anaTrack.trackSrc = cms.InputTag("hiGeneralTracks")


process.temp_step = cms.Path(process.hiGenParticles * process.hiGenParticlesForJets
                             *
                             process.ak6HiGenJets +
                             process.ak7HiGenJets)

process.ana_step = cms.Path(process.heavyIon*
                            process.hiEvtAnalyzer*
                            process.HiGenParticleAna*
                            process.hiGenJetsCleaned
                            +
                            process.akVs3CaloJetSequence
                            +
                            process.akPu3CaloJetSequence
                            +
                            process.akVs3PFJetSequence
                            +
                            process.akPu3PFJetSequence +
                            process.multiPhotonAnalyzer +
                            process.anaTrack + 
                            #process.hiTracks + 
                            #process.mergedTrack +
                            process.pfcandAnalyzer +
                            process.rechitAna 
                            )

# Customization
from CmsHi.JetAnalysis.customise_cfi import *
setPhotonObject(process,"cleanPhotons")

process.load('CmsHi.HiHLTAlgos.hltanalysis_cff')
process.hltanalysis.hltresults = cms.InputTag("TriggerResults","","RECO")
process.skimanalysis.hltresults = cms.InputTag("TriggerResults","","SIM")

process.hltAna = cms.Path(process.hltanalysis)
process.pAna = cms.EndPath(process.skimanalysis)
