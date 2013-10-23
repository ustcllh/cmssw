
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs2Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs2CaloJets"),
    matched = cms.InputTag("ak2GenJets")
    )

akVs2Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVs2CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs2Calocorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs2CaloJets"),
    payload = "CAPak2OBJECT"
    )

akVs2CalopatJets = patJets.clone(jetSource = cms.InputTag("akVs2CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs2Calocorr")),
                                               genJetMatch = cms.InputTag("akVs2Calomatch"),
                                               genPartonMatch = cms.InputTag("akVs2Caloparton"),
                                               jetIDMap = cms.InputTag("akVs2CaloJetID"),
                                               )

akVs2CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs2CalopatJets"),
                                                             genjetTag = 'ak2GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs2CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs2CaloSequence_mc = cms.Sequence(akVs2Calomatch
                                                  *
                                                  akVs2Caloparton
                                                  *
                                                  akVs2Calocorr
                                                  *
                                                  akVs2CalopatJets
                                                  *
                                                  akVs2CaloAnalyzer
                                                  )

akVs2CaloSequence_data = cms.Sequence(akVs2Calocorr
                                                    *
                                                    akVs2CalopatJets
                                                    *
                                                    akVs2CaloAnalyzer
                                                    )


akVs2CaloSequence = akVs2CaloSequence_mc
