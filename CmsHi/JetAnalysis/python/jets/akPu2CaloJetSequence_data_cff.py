
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu2Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu2CaloJets"),
    matched = cms.InputTag("ak2GenJets")
    )

akPu2Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu2CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu2Calocorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu2CaloJets"),
    payload = "CAPak2OBJECT"
    )

akPu2CalopatJets = patJets.clone(jetSource = cms.InputTag("akPu2CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2Calocorr")),
                                               genJetMatch = cms.InputTag("akPu2Calomatch"),
                                               genPartonMatch = cms.InputTag("akPu2Caloparton"),
                                               jetIDMap = cms.InputTag("akPu2CaloJetID"),
                                               )

akPu2CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu2CalopatJets"),
                                                             genjetTag = 'ak2GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu2CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu2CaloSequence_mc = cms.Sequence(akPu2Calomatch
                                                  *
                                                  akPu2Caloparton
                                                  *
                                                  akPu2Calocorr
                                                  *
                                                  akPu2CalopatJets
                                                  *
                                                  akPu2CaloAnalyzer
                                                  )

akPu2CaloSequence_data = cms.Sequence(akPu2Calocorr
                                                    *
                                                    akPu2CalopatJets
                                                    *
                                                    akPu2CaloAnalyzer
                                                    )


akPu2CaloSequence = akPu2CaloSequence_data
