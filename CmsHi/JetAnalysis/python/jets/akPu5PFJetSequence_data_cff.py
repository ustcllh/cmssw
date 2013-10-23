
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu5PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu5PFJets"),
    matched = cms.InputTag("ak5GenJets")
    )

akPu5PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPu5PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu5PFcorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu5PFJets"),
    payload = "CAPak5OBJECT"
    )

akPu5PFpatJets = patJets.clone(jetSource = cms.InputTag("akPu5PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5PFcorr")),
                                               genJetMatch = cms.InputTag("akPu5PFmatch"),
                                               genPartonMatch = cms.InputTag("akPu5PFparton"),
                                               jetIDMap = cms.InputTag("akPu5PFJetID"),
                                               )

akPu5PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu5PFpatJets"),
                                                             genjetTag = 'ak5GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu5PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu5PFSequence_mc = cms.Sequence(akPu5PFmatch
                                                  *
                                                  akPu5PFparton
                                                  *
                                                  akPu5PFcorr
                                                  *
                                                  akPu5PFpatJets
                                                  *
                                                  akPu5PFAnalyzer
                                                  )

akPu5PFSequence_data = cms.Sequence(akPu5PFcorr
                                                    *
                                                    akPu5PFpatJets
                                                    *
                                                    akPu5PFAnalyzer
                                                    )


akPu5PFSequence = akPu5PFSequence_data
