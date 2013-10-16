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
ivars.inputFiles = "file:/mnt/hadoop/cms/store/user/yilmaz/Hydjet_Drum_53X_test01/Hydjet_Drum_53X_RECO_v10/d28447d1a42bac5ad506ba0e951d23b3/step3_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_RECO_82_2_pU9.root"
ivars.outputFile = 'HiForest.root'
ivars.maxEvents = 10

ivars.parseArguments()

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

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')

process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# PbPb 53X MC
process.GlobalTag.globaltag = 'START53_V10::All'

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import *
overrideGT_PbPb2760(process)

# process.HeavyIonGlobalParameters = cms.PSet(
#     centralityVariable = cms.string("HFtowersPlusTrunc"),
#     nonDefaultGlauberModel = cms.string("Hijing"),
#     centralitySrc = cms.InputTag("pACentrality")
#     )

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string(ivars.outputFile))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################
process.load('CmsHi.JetAnalysis.PatAna_MC_cff')
process.pat_step = cms.Path(process.makeHeavyIonVsJets)

process.akVs3PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
                                            jetTag = cms.InputTag("akVs3PFpatJets"),
                                            matchTag = cms.untracked.InputTag("akVs3PFpatJets"),
                                            genjetTag = cms.InputTag("iterativeCone5HiGenJets"),
                                            eventInfoTag = cms.InputTag("generator"),
                                            isMC = cms.untracked.bool(False), 
                                            fillGenJets = cms.untracked.bool(False),
                                            rParam = cms.double(0.3),
                                            trackTag = cms.InputTag("hiGeneralTracks"),
                                            useQuality = cms.untracked.bool(True),
                                            trackQuality  = cms.untracked.string("highPurity"),
                                            useCentrality = cms.untracked.bool(False),
                                            doLifeTimeTagging = cms.untracked.bool(False),
                                            L1gtReadout = cms.InputTag("gtDigis"),
                                            skipCorrections = cms.untracked.bool(True),
                                            hltTrgResults = cms.untracked.string("TriggerResults::HLT"),
                                            hltTrgNames  = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core',
                                                                                 'HLT_HIJet35U',
                                                                                 'HLT_HIJet35U_Core',
                                                                                 'HLT_HIJet50U_Core')
)

#process.JetSequence = cms.Sequence( akVs3PFJetAnalyzer)

process.ana_step = cms.Path( process.HiForest +
                             process.akVs3PFJetAnalyzer
)

process.load('CmsHi.HiHLTAlgos.hltanalysis_cff')
process.hltanalysis.hltresults = cms.InputTag("TriggerResults","","RECO")
process.skimanalysis.hltresults = cms.InputTag("TriggerResults","","SIM")

process.hltAna = cms.Path(process.hltanalysis)
process.pAna = cms.EndPath(process.skimanalysis)
