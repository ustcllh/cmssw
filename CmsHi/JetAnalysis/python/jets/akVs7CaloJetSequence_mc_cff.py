
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs7Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs7CaloJets"),
    matched = cms.InputTag("ak7GenJets")
    )

akVs7Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVs7CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs7Calocorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs7CaloJets"),
    payload = "CAPak7OBJECT"
    )

akVs7CalopatJets = patJets.clone(jetSource = cms.InputTag("akVs7CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs7Calocorr")),
                                               genJetMatch = cms.InputTag("akVs7Calomatch"),
                                               genPartonMatch = cms.InputTag("akVs7Caloparton"),
                                               jetIDMap = cms.InputTag("akVs7CaloJetID"),
                                               )

akVs7CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs7CalopatJets"),
                                                             genjetTag = 'ak7GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs7CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs7CaloSequence_mc = cms.Sequence(akVs7Calomatch
                                                  *
                                                  akVs7Caloparton
                                                  *
                                                  akVs7Calocorr
                                                  *
                                                  akVs7CalopatJets
                                                  *
                                                  akVs7CaloAnalyzer
                                                  )

akVs7CaloSequence_data = cms.Sequence(akVs7Calocorr
                                                    *
                                                    akVs7CalopatJets
                                                    *
                                                    akVs7CaloAnalyzer
                                                    )


akVs7CaloSequence = akVs7CaloSequence_mc
