
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs6Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs6CaloJets"),
    matched = cms.InputTag("ak6HiGenJets")
    )

akVs6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVs6CaloJets"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

akVs6Calocorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs6CaloJets"),
    payload = "AK6Calo_hiIterativeTracks"
    )

akVs6CalopatJets = patJets.clone(jetSource = cms.InputTag("akVs6CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs6Calocorr")),
                                               genJetMatch = cms.InputTag("akVs6Calomatch"),
                                               genPartonMatch = cms.InputTag("akVs6Caloparton"),
                                               jetIDMap = cms.InputTag("akVs6CaloJetID"),
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

akVs6CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs6CalopatJets"),
                                                             genjetTag = 'ak6HiGenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs6CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs6CaloJetSequence_mc = cms.Sequence(akVs6Calomatch
                                                  *
                                                  akVs6Caloparton
                                                  *
                                                  akVs6Calocorr
                                                  *
                                                  akVs6CalopatJets
                                                  *
                                                  akVs6CaloAnalyzer
                                                  )

akVs6CaloJetSequence_data = cms.Sequence(akVs6Calocorr
                                                    *
                                                    akVs6CalopatJets
                                                    *
                                                    akVs6CaloAnalyzer
                                                    )

akVs6CaloJetSequence = cms.Sequence(akVs6CaloJetSequence_data)
