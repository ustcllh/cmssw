
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs2PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs2PFJets"),
    matched = cms.InputTag("ak2GenJets")
    )

akVs2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs2PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs2PFcorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs2PFJets"),
    payload = "CAPak2OBJECT"
    )

akVs2PFpatJets = patJets.clone(jetSource = cms.InputTag("akVs2PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs2PFcorr")),
                                               genJetMatch = cms.InputTag("akVs2PFmatch"),
                                               genPartonMatch = cms.InputTag("akVs2PFparton"),
                                               jetIDMap = cms.InputTag("akVs2PFJetID"),
                                               )

akVs2PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs2PFpatJets"),
                                                             genjetTag = 'ak2GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs2PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs2PFSequence_mc = cms.Sequence(akVs2PFmatch
                                                  *
                                                  akVs2PFparton
                                                  *
                                                  akVs2PFcorr
                                                  *
                                                  akVs2PFpatJets
                                                  *
                                                  akVs2PFAnalyzer
                                                  )

akVs2PFSequence_data = cms.Sequence(akVs2PFcorr
                                                    *
                                                    akVs2PFpatJets
                                                    *
                                                    akVs2PFAnalyzer
                                                    )


akVs2PFSequence = akVs2PFSequence_data
