
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu2Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu2CaloJets"),
    matched = cms.InputTag("ak2HiGenJets")
    )

akPu2Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu2CaloJets"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

akPu2Calocorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu2CaloJets"),
    payload = "AK2Calo_hiIterativeTracks"
    )

akPu2CalopatJets = patJets.clone(jetSource = cms.InputTag("akPu2CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2Calocorr")),
                                               genJetMatch = cms.InputTag("akPu2Calomatch"),
                                               genPartonMatch = cms.InputTag("akPu2Caloparton"),
                                               jetIDMap = cms.InputTag("akPu2CaloJetID"),
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

akPu2CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu2CalopatJets"),
                                                             genjetTag = 'ak2HiGenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu2CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu2CaloJetSequence_mc = cms.Sequence(akPu2Calomatch
                                                  *
                                                  akPu2Caloparton
                                                  *
                                                  akPu2Calocorr
                                                  *
                                                  akPu2CalopatJets
                                                  *
                                                  akPu2CaloAnalyzer
                                                  )

akPu2CaloJetSequence_data = cms.Sequence(akPu2Calocorr
                                                    *
                                                    akPu2CalopatJets
                                                    *
                                                    akPu2CaloAnalyzer
                                                    )

akPu2CaloJetSequence = cms.Sequence(akPu2CaloJetSequence_data)
