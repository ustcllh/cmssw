
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs3Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs3CaloJets"),
    matched = cms.InputTag("ak3GenJets")
    )

akVs3Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVs3CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs3Calocorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs3CaloJets"),
    payload = "CAPak3OBJECT"
    )

akVs3CalopatJets = patJets.clone(jetSource = cms.InputTag("akVs3CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs3Calocorr")),
                                               genJetMatch = cms.InputTag("akVs3Calomatch"),
                                               genPartonMatch = cms.InputTag("akVs3Caloparton"),
                                               jetIDMap = cms.InputTag("akVs3CaloJetID"),
                                               )

akVs3CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs3CalopatJets"),
                                                             genjetTag = 'ak3GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs3CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs3CaloSequence_mc = cms.Sequence(akVs3Calomatch
                                                  *
                                                  akVs3Caloparton
                                                  *
                                                  akVs3Calocorr
                                                  *
                                                  akVs3CalopatJets
                                                  *
                                                  akVs3CaloAnalyzer
                                                  )

akVs3CaloSequence_data = cms.Sequence(akVs3Calocorr
                                                    *
                                                    akVs3CalopatJets
                                                    *
                                                    akVs3CaloAnalyzer
                                                    )


akVs3CaloSequence = akVs3CaloSequence_mc
