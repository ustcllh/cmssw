
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs4Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs4CaloJets"),
    matched = cms.InputTag("ak4GenJets")
    )

akVs4Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVs4CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs4Calocorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs4CaloJets"),
    payload = "CAPak4OBJECT"
    )

akVs4CalopatJets = patJets.clone(jetSource = cms.InputTag("akVs4CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs4Calocorr")),
                                               genJetMatch = cms.InputTag("akVs4Calomatch"),
                                               genPartonMatch = cms.InputTag("akVs4Caloparton"),
                                               jetIDMap = cms.InputTag("akVs4CaloJetID"),
                                               )

akVs4CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs4CalopatJets"),
                                                             genjetTag = 'ak4GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs4CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs4CaloSequence_mc = cms.Sequence(akVs4Calomatch
                                                  *
                                                  akVs4Caloparton
                                                  *
                                                  akVs4Calocorr
                                                  *
                                                  akVs4CalopatJets
                                                  *
                                                  akVs4CaloAnalyzer
                                                  )

akVs4CaloSequence_data = cms.Sequence(akVs4Calocorr
                                                    *
                                                    akVs4CalopatJets
                                                    *
                                                    akVs4CaloAnalyzer
                                                    )


akVs4CaloSequence = akVs4CaloSequence_mc
