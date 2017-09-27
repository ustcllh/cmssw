import FWCore.ParameterSet.Config as cms

#not in official reco yet
from RecoHI.HiJetAlgos.hiFJGridEmptyAreaCalculator_cff import hiFJGridEmptyAreaCalculator

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_PbPb_mb_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_mb_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akCs3PFJetSequence_PbPb_mb_cff import *

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_mb_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_mb_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akCs4PFJetSequence_PbPb_mb_cff import *

from HeavyIonsAnalysis.JetAnalysis.jets.akPu5CaloJetSequence_PbPb_mb_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu5PFJetSequence_PbPb_mb_cff import *

#to be added later
#from HeavyIonsAnalysis.JetAnalysis.jets.akCsSoftDrop4PFJetSequence_PbPb_mb_cff import *
#from HeavyIonsAnalysis.JetAnalysis.jets.akCsSoftDrop5PFJetSequence_PbPb_mb_cff import *

highPurityTracks = cms.EDFilter("TrackSelector",
                                src = cms.InputTag("hiGeneralTracks"),
                                cut = cms.string('quality("highPurity")'))

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
offlinePrimaryVertices.TrackLabel = 'highPurityTracks'

jetSequences = cms.Sequence(
    hiFJGridEmptyAreaCalculator +
    
    #jets already reconstructed in reco
    #akPu3CaloJets +
    #akPu3PFJets +
    #akCs3PFJets +

    #akPu4CaloJets +
    #akPu4PFJets +
    #akCs4PFJets +

    #akPu5CaloJets +
    #akPu5PFJets +

    #to be added later
    #akCsSoftDrop4PFJets +
    #akCsSoftDrop5PFJets +

    highPurityTracks +
    offlinePrimaryVertices +

    akPu3CaloJetSequence +
    akPu3PFJetSequence +
    akCs3PFJetSequence +

    akPu4CaloJetSequence +
    akPu4PFJetSequence +
    akCs4PFJetSequence +

    akPu5CaloJetSequence +
    akPu5PFJetSequence# +

    #to be added later
    #akCsSoftDrop4PFJetSequence +
    #akCsSoftDrop5PFJetSequence
)
