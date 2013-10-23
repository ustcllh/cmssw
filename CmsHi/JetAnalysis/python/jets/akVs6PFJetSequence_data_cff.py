
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs6PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs6PFJets"),
    matched = cms.InputTag("ak6GenJets")
    )

akVs6PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs6PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs6PFcorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs6PFJets"),
    payload = "CAPak6OBJECT"
    )

akVs6PFpatJets = patJets.clone(jetSource = cms.InputTag("akVs6PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs6PFcorr")),
                                               genJetMatch = cms.InputTag("akVs6PFmatch"),
                                               genPartonMatch = cms.InputTag("akVs6PFparton"),
                                               jetIDMap = cms.InputTag("akVs6PFJetID"),
                                               )

akVs6PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs6PFpatJets"),
                                                             genjetTag = 'ak6GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs6PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs6PFSequence_mc = cms.Sequence(akVs6PFmatch
                                                  *
                                                  akVs6PFparton
                                                  *
                                                  akVs6PFcorr
                                                  *
                                                  akVs6PFpatJets
                                                  *
                                                  akVs6PFAnalyzer
                                                  )

akVs6PFSequence_data = cms.Sequence(akVs6PFcorr
                                                    *
                                                    akVs6PFpatJets
                                                    *
                                                    akVs6PFAnalyzer
                                                    )


akVs6PFSequence = akVs6PFSequence_data
