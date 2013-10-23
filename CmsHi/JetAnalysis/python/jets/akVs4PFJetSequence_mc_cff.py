
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs4PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs4PFJets"),
    matched = cms.InputTag("ak4GenJets")
    )

akVs4PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs4PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs4PFcorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs4PFJets"),
    payload = "CAPak4OBJECT"
    )

akVs4PFpatJets = patJets.clone(jetSource = cms.InputTag("akVs4PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs4PFcorr")),
                                               genJetMatch = cms.InputTag("akVs4PFmatch"),
                                               genPartonMatch = cms.InputTag("akVs4PFparton"),
                                               jetIDMap = cms.InputTag("akVs4PFJetID"),
                                               )

akVs4PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs4PFpatJets"),
                                                             genjetTag = 'ak4GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs4PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs4PFSequence_mc = cms.Sequence(akVs4PFmatch
                                                  *
                                                  akVs4PFparton
                                                  *
                                                  akVs4PFcorr
                                                  *
                                                  akVs4PFpatJets
                                                  *
                                                  akVs4PFAnalyzer
                                                  )

akVs4PFSequence_data = cms.Sequence(akVs4PFcorr
                                                    *
                                                    akVs4PFpatJets
                                                    *
                                                    akVs4PFAnalyzer
                                                    )


akVs4PFSequence = akVs4PFSequence_mc
