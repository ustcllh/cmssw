
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu2PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu2PFJets"),
    matched = cms.InputTag("ak2GenJets")
    )

akPu2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPu2PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu2PFcorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu2PFJets"),
    payload = "CAPak2OBJECT"
    )

akPu2PFpatJets = patJets.clone(jetSource = cms.InputTag("akPu2PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2PFcorr")),
                                               genJetMatch = cms.InputTag("akPu2PFmatch"),
                                               genPartonMatch = cms.InputTag("akPu2PFparton"),
                                               jetIDMap = cms.InputTag("akPu2PFJetID"),
                                               )

akPu2PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu2PFpatJets"),
                                                             genjetTag = 'ak2GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu2PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu2PFSequence_mc = cms.Sequence(akPu2PFmatch
                                                  *
                                                  akPu2PFparton
                                                  *
                                                  akPu2PFcorr
                                                  *
                                                  akPu2PFpatJets
                                                  *
                                                  akPu2PFAnalyzer
                                                  )

akPu2PFSequence_data = cms.Sequence(akPu2PFcorr
                                                    *
                                                    akPu2PFpatJets
                                                    *
                                                    akPu2PFAnalyzer
                                                    )


akPu2PFSequence = akPu2PFSequence_mc
