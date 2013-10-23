
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs5Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs5CaloJets"),
    matched = cms.InputTag("ak5GenJets")
    )

akVs5Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVs5CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs5Calocorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs5CaloJets"),
    payload = "CAPak5OBJECT"
    )

akVs5CalopatJets = patJets.clone(jetSource = cms.InputTag("akVs5CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs5Calocorr")),
                                               genJetMatch = cms.InputTag("akVs5Calomatch"),
                                               genPartonMatch = cms.InputTag("akVs5Caloparton"),
                                               jetIDMap = cms.InputTag("akVs5CaloJetID"),
                                               )

akVs5CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs5CalopatJets"),
                                                             genjetTag = 'ak5GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs5CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs5CaloSequence_mc = cms.Sequence(akVs5Calomatch
                                                  *
                                                  akVs5Caloparton
                                                  *
                                                  akVs5Calocorr
                                                  *
                                                  akVs5CalopatJets
                                                  *
                                                  akVs5CaloAnalyzer
                                                  )

akVs5CaloSequence_data = cms.Sequence(akVs5Calocorr
                                                    *
                                                    akVs5CalopatJets
                                                    *
                                                    akVs5CaloAnalyzer
                                                    )


akVs5CaloSequence = akVs5CaloSequence_data
