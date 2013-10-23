
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs3PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs3PFJets"),
    matched = cms.InputTag("ak3GenJets")
    )

akVs3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs3PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs3PFcorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs3PFJets"),
    payload = "CAPak3OBJECT"
    )

akVs3PFpatJets = patJets.clone(jetSource = cms.InputTag("akVs3PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs3PFcorr")),
                                               genJetMatch = cms.InputTag("akVs3PFmatch"),
                                               genPartonMatch = cms.InputTag("akVs3PFparton"),
                                               jetIDMap = cms.InputTag("akVs3PFJetID"),
                                               )

akVs3PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs3PFpatJets"),
                                                             genjetTag = 'ak3GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs3PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs3PFSequence_mc = cms.Sequence(akVs3PFmatch
                                                  *
                                                  akVs3PFparton
                                                  *
                                                  akVs3PFcorr
                                                  *
                                                  akVs3PFpatJets
                                                  *
                                                  akVs3PFAnalyzer
                                                  )

akVs3PFSequence_data = cms.Sequence(akVs3PFcorr
                                                    *
                                                    akVs3PFpatJets
                                                    *
                                                    akVs3PFAnalyzer
                                                    )


akVs3PFSequence = akVs3PFSequence_mc
