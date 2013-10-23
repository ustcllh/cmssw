
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu6PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu6PFJets"),
    matched = cms.InputTag("ak6GenJets")
    )

akPu6PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPu6PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu6PFcorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu6PFJets"),
    payload = "CAPak6OBJECT"
    )

akPu6PFpatJets = patJets.clone(jetSource = cms.InputTag("akPu6PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu6PFcorr")),
                                               genJetMatch = cms.InputTag("akPu6PFmatch"),
                                               genPartonMatch = cms.InputTag("akPu6PFparton"),
                                               jetIDMap = cms.InputTag("akPu6PFJetID"),
                                               )

akPu6PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu6PFpatJets"),
                                                             genjetTag = 'ak6GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu6PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu6PFSequence_mc = cms.Sequence(akPu6PFmatch
                                                  *
                                                  akPu6PFparton
                                                  *
                                                  akPu6PFcorr
                                                  *
                                                  akPu6PFpatJets
                                                  *
                                                  akPu6PFAnalyzer
                                                  )

akPu6PFSequence_data = cms.Sequence(akPu6PFcorr
                                                    *
                                                    akPu6PFpatJets
                                                    *
                                                    akPu6PFAnalyzer
                                                    )


akPu6PFSequence = akPu6PFSequence_mc
