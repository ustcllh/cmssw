
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu3PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu3PFJets"),
    matched = cms.InputTag("ak3GenJets")
    )

akPu3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPu3PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu3PFcorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu3PFJets"),
    payload = "CAPak3OBJECT"
    )

akPu3PFpatJets = patJets.clone(jetSource = cms.InputTag("akPu3PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr")),
                                               genJetMatch = cms.InputTag("akPu3PFmatch"),
                                               genPartonMatch = cms.InputTag("akPu3PFparton"),
                                               jetIDMap = cms.InputTag("akPu3PFJetID"),
                                               )

akPu3PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu3PFpatJets"),
                                                             genjetTag = 'ak3GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu3PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu3PFSequence_mc = cms.Sequence(akPu3PFmatch
                                                  *
                                                  akPu3PFparton
                                                  *
                                                  akPu3PFcorr
                                                  *
                                                  akPu3PFpatJets
                                                  *
                                                  akPu3PFAnalyzer
                                                  )

akPu3PFSequence_data = cms.Sequence(akPu3PFcorr
                                                    *
                                                    akPu3PFpatJets
                                                    *
                                                    akPu3PFAnalyzer
                                                    )


akPu3PFSequence = akPu3PFSequence_mc
