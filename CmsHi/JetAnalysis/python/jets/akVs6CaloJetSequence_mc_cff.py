
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs6Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs6CaloJets"),
    matched = cms.InputTag("ak6GenJets")
    )

akVs6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVs6CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs6Calocorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs6CaloJets"),
    payload = "CAPak6OBJECT"
    )

akVs6CalopatJets = patJets.clone(jetSource = cms.InputTag("akVs6CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs6Calocorr")),
                                               genJetMatch = cms.InputTag("akVs6Calomatch"),
                                               genPartonMatch = cms.InputTag("akVs6Caloparton"),
                                               jetIDMap = cms.InputTag("akVs6CaloJetID"),
                                               )

akVs6CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs6CalopatJets"),
                                                             genjetTag = 'ak6GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs6CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs6CaloSequence_mc = cms.Sequence(akVs6Calomatch
                                                  *
                                                  akVs6Caloparton
                                                  *
                                                  akVs6Calocorr
                                                  *
                                                  akVs6CalopatJets
                                                  *
                                                  akVs6CaloAnalyzer
                                                  )

akVs6CaloSequence_data = cms.Sequence(akVs6Calocorr
                                                    *
                                                    akVs6CalopatJets
                                                    *
                                                    akVs6CaloAnalyzer
                                                    )


akVs6CaloSequence = akVs6CaloSequence_mc
