
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu6Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu6CaloJets"),
    matched = cms.InputTag("ak6HiGenJets")
    )

akPu6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu6CaloJets"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

akPu6Calocorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu6CaloJets"),
    payload = "AK6Calo_hiIterativeTracks"
    )

akPu6CalopatJets = patJets.clone(jetSource = cms.InputTag("akPu6CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu6Calocorr")),
                                               genJetMatch = cms.InputTag("akPu6Calomatch"),
                                               genPartonMatch = cms.InputTag("akPu6Caloparton"),
                                               jetIDMap = cms.InputTag("akPu6CaloJetID"),
                                               addBTagInfo         = False,
                                               addTagInfos         = False,
                                               addDiscriminators   = False,
                                               addAssociatedTracks = False,
                                               addJetCharge        = False,
                                               addJetID            = True,
                                               getJetMCFlavour     = False,
                                               addGenPartonMatch   = True,
                                               addGenJetMatch      = True,
                                               embedGenJetMatch    = True,
                                               embedGenPartonMatch = True,
                                               embedCaloTowers     = False,
				            )

akPu6CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu6CalopatJets"),
                                                             genjetTag = 'ak6HiGenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu6CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu6CaloJetSequence_mc = cms.Sequence(akPu6Calomatch
                                                  *
                                                  akPu6Caloparton
                                                  *
                                                  akPu6Calocorr
                                                  *
                                                  akPu6CalopatJets
                                                  *
                                                  akPu6CaloAnalyzer
                                                  )

akPu6CaloJetSequence_data = cms.Sequence(akPu6Calocorr
                                                    *
                                                    akPu6CalopatJets
                                                    *
                                                    akPu6CaloAnalyzer
                                                    )

akPu6CaloJetSequence = cms.Sequence(akPu6CaloJetSequence_data)
