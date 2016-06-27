### HiForest Configuration
# Collisions: pp
# Type: Data
# Input: AOD

import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet()

#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()
if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.string(version)

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                "file:step2_RAW2DIGI_L1Reco_RECO.root"
                            )
)


# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10))


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_v13', '')  #for now track GT manually, since centrality tables updated ex post facto
process.HiForest.GlobalTagLabel = process.GlobalTag.globaltag

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import overrideJEC_PbPb5020
process = overrideJEC_PbPb5020(process)

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForestAOD.root"))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

####################################################################################

#############################
# Jets
#############################
from Configuration.StandardSequences.ReconstructionHeavyIons_cff import voronoiBackgroundPF, voronoiBackgroundCalo
from RecoJets.JetProducers.kt4PFJets_cfi import kt4PFJets
from RecoHI.HiJetAlgos.hiFJRhoProducer import hiFJRhoProducer
process.kt4PFJets = kt4PFJets
process.hiFJRhoProducer = hiFJRhoProducer
process.kt4PFJets.src = cms.InputTag('particleFlowTmp')
process.kt4PFJets.doAreaFastjet = True
process.kt4PFJets.jetPtMin      = cms.double(0.0)
process.kt4PFJets.GhostArea     = cms.double(0.005)
from RecoHI.HiJetAlgos.hiFJGridEmptyAreaCalculator_cff import hiFJGridEmptyAreaCalculator
process.hiFJGridEmptyAreaCalculator = hiFJGridEmptyAreaCalculator

process.load('HeavyIonsAnalysis.JetAnalysis.hiFJRhoAnalyzer_cff')

process.voronoiBackgroundPF = voronoiBackgroundPF
process.voronoiBackgroundCalo = voronoiBackgroundCalo
process.load('HeavyIonsAnalysis.JetAnalysis.jets.HiReRecoJets_HI_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak2CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs2CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak2PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs2PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu2PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akCs2PFJetSequence_PbPb_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak3CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak3PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akCs3PFJetSequence_PbPb_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak4CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak4PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akCs4PFJetSequence_PbPb_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak5CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak5PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akCs5PFJetSequence_PbPb_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akCsFilter4PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akCsFilter5PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akCsSoftDrop4PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akCsSoftDrop5PFJetSequence_PbPb_data_cff')

process.highPurityTracks = cms.EDFilter("TrackSelector",
                                        src = cms.InputTag("hiGeneralTracks"),
                                        cut = cms.string('quality("highPurity")'))

process.load("RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi")
process.offlinePrimaryVertices.TrackLabel = 'highPurityTracks'

process.jetSequences = cms.Sequence(
    voronoiBackgroundPF+
    voronoiBackgroundCalo+
    process.kt4PFJets +
    process.hiFJRhoProducer +
	process.hiFJGridEmptyAreaCalculator +
    process.hiFJRhoAnalyzer +
	
    process.ak2CaloJets +
    process.ak2PFJets +
    process.akPu2CaloJets +
    process.akPu2PFJets +
    process.akVs2CaloJets +
    process.akVs2PFJets +
    process.akCs2PFJets +

    process.ak3CaloJets +
    process.ak3PFJets +
    # process.akPu3CaloJets +
    # process.akPu3PFJets +
    process.akVs3CaloJets +
    process.akVs3PFJets +
    process.akCs3PFJets +

    process.ak4CaloJets +
    process.ak4PFJets +
    # process.akPu4CaloJets +
    # process.akPu4PFJets +
    process.akVs4CaloJets +
    process.akVs4PFJets +
    process.akCs4PFJets +

    process.ak5CaloJets +
    process.ak5PFJets +
    process.akPu5CaloJets +
    process.akPu5PFJets +
    process.akVs5CaloJets +
    process.akVs5PFJets +
    process.akCs5PFJets +

    process.akCsFilter4PFJets +
    process.akCsFilter5PFJets +
    process.akCsSoftDrop4PFJets +
    process.akCsSoftDrop5PFJets +

    process.highPurityTracks +
    process.offlinePrimaryVertices +

    process.ak2CaloJetSequence +
    process.akPu2CaloJetSequence +
    process.akVs2CaloJetSequence +
    process.ak2PFJetSequence +
    process.akVs2PFJetSequence +
    process.akPu2PFJetSequence +
    process.akCs2PFJetSequence +

    process.ak3CaloJetSequence +
    process.akPu3CaloJetSequence +
    process.akVs3CaloJetSequence +
    process.ak3PFJetSequence +
    process.akVs3PFJetSequence +
    process.akPu3PFJetSequence +
    process.akCs3PFJetSequence +

    process.ak4CaloJetSequence +
    process.akPu4CaloJetSequence +
    process.akVs4CaloJetSequence +
    process.ak4PFJetSequence +
    process.akVs4PFJetSequence +
    process.akPu4PFJetSequence +
    process.akCs4PFJetSequence +

    process.ak5CaloJetSequence +
    process.akPu5CaloJetSequence +
    process.akVs5CaloJetSequence +
    process.ak5PFJetSequence +
    process.akVs5PFJetSequence +
    process.akPu5PFJetSequence +
    process.akCs5PFJetSequence +

    process.akCsFilter4PFJetSequence +
    process.akCsFilter5PFJetSequence +
    process.akCsSoftDrop4PFJetSequence +
    process.akCsSoftDrop5PFJetSequence
)

#####################################################################################

############################
# Event Analysis
############################
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
# process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_PbPb_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_cfi')

# process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
# from HeavyIonsAnalysis.EventAnalysis.dummybranches_cff import addHLTdummybranches
# addHLTdummybranches(process)
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
from HeavyIonsAnalysis.EventAnalysis.dummybranches_cff import addHLTdummybranchesForPP
addHLTdummybranchesForPP(process)

process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_cfi")
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzerCS_cfi")
process.pfcandAnalyzerCS.skipCharged = False
process.pfcandAnalyzerCS.pfPtMin = 0
process.load("HeavyIonsAnalysis.JetAnalysis.hcalNoise_cff")

#####################################################################################

#########################
# Track Analyzer
#########################
process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_cff')
# process.load("HeavyIonsAnalysis.TrackAnalysis.METAnalyzer_cff")


####################################################################################

#####################
# Photons
#####################
process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.doGenParticles = False
process.ggHiNtuplizerGED = process.ggHiNtuplizer.clone(recoPhotonSrc = cms.InputTag('gedPhotonsTmp'),
                                                       recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerGED')
)


####################################################################################

#####################
# tupel and necessary PAT sequences
#####################

process.load("HeavyIonsAnalysis.VectorBosonAnalysis.tupelSequence_PbPb_cff")

#####################################################################################

#########################
# Main analysis list
#########################

process.ana_step = cms.Path(process.hltanalysis *
			    process.hltobject *
                            process.centralityBin *
                            process.hiEvtAnalyzer*
                            process.jetSequences +
                            process.ggHiNtuplizer +
                            process.ggHiNtuplizerGED +
                            process.pfcandAnalyzer +
                            process.pfcandAnalyzerCS +
                            process.HiForest +
                            process.trackSequencesPbPb +
                            process.hcalNoise #+
                            #process.tupelPatSequence
                            )

#####################################################################################

#########################
# Event Selection
#########################

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.pcollisionEventSelection = cms.Path(process.collisionEventSelectionAOD)
process.pHBHENoiseFilterResultProducer = cms.Path( process.HBHENoiseFilterResultProducer )
process.HBHENoiseFilterResult = cms.Path(process.fHBHENoiseFilterResult)
process.HBHENoiseFilterResultRun1 = cms.Path(process.fHBHENoiseFilterResultRun1)
process.HBHENoiseFilterResultRun2Loose = cms.Path(process.fHBHENoiseFilterResultRun2Loose)
process.HBHENoiseFilterResultRun2Tight = cms.Path(process.fHBHENoiseFilterResultRun2Tight)
process.HBHEIsoNoiseFilterResult = cms.Path(process.fHBHEIsoNoiseFilterResult)
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter )


# process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')

process.PAprimaryVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("hiSelectedVertex"),
    cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2"),
    filter = cms.bool(True), # otherwise it won't filter the events
)

process.NoScraping = cms.EDFilter("FilterOutScraping",
 applyfilter = cms.untracked.bool(True),
 debugOn = cms.untracked.bool(False),
 numtrack = cms.untracked.uint32(10),
 thresh = cms.untracked.double(0.25),
 src = cms.untracked.InputTag("hiGeneralTracks"),
)

process.pPAprimaryVertexFilter = cms.Path(process.PAprimaryVertexFilter)
process.pBeamScrapingFilter=cms.Path(process.NoScraping)

process.load("HeavyIonsAnalysis.VertexAnalysis.PAPileUpVertexFilter_cff")

process.pVertexFilterCutG = cms.Path(process.pileupVertexFilterCutG)
process.pVertexFilterCutGloose = cms.Path(process.pileupVertexFilterCutGloose)
process.pVertexFilterCutGtight = cms.Path(process.pileupVertexFilterCutGtight)
process.pVertexFilterCutGplus = cms.Path(process.pileupVertexFilterCutGplus)
process.pVertexFilterCutE = cms.Path(process.pileupVertexFilterCutE)
process.pVertexFilterCutEandG = cms.Path(process.pileupVertexFilterCutEandG)

process.pAna = cms.EndPath(process.skimanalysis)


process.load('HeavyIonsAnalysis.Configuration.hfCoincFilter_cff')
process.phfCoincFilter1 = cms.Path(process.hfCoincFilter)
process.phfCoincFilter2 = cms.Path(process.hfCoincFilter2)
process.phfCoincFilter3 = cms.Path(process.hfCoincFilter3)
process.phfCoincFilter4 = cms.Path(process.hfCoincFilter4)
process.phfCoincFilter5 = cms.Path(process.hfCoincFilter5)

process.pclusterCompatibilityFilter = cms.Path(process.clusterCompatibilityFilter)

process.pAna = cms.EndPath(process.skimanalysis)

# Customization
##########################################UE##########################################
from CondCore.DBCommon.CondDBSetup_cfi import *
process.uetable = cms.ESSource("PoolDBESSource",
      DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
        ),
      timetype = cms.string('runnumber'),
      toGet = cms.VPSet(
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("UETableCompatibilityFormat_PF_v02_offline"),
                   label = cms.untracked.string("UETable_PF")
          ),
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("UETableCompatibilityFormat_Calo_v02_offline"),
                   label = cms.untracked.string("UETable_Calo")
          )
      ), 
      connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
)
process.es_prefer_uetable = cms.ESPrefer('PoolDBESSource','uetable')
##########################################UE##########################################
