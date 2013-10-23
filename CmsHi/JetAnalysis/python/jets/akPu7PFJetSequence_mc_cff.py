
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu7PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu7PFJets"),
    matched = cms.InputTag("ak7GenJets")
    )

akPu7PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPu7PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu7PFcorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu7PFJets"),
    payload = "CAPak7OBJECT"
    )

akPu7PFpatJets = patJets.clone(jetSource = cms.InputTag("akPu7PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu7PFcorr")),
                                               genJetMatch = cms.InputTag("akPu7PFmatch"),
                                               genPartonMatch = cms.InputTag("akPu7PFparton"),
                                               jetIDMap = cms.InputTag("akPu7PFJetID"),
                                               )

akPu7PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu7PFpatJets"),
                                                             genjetTag = 'ak7GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu7PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu7PFSequence_mc = cms.Sequence(akPu7PFmatch
                                                  *
                                                  akPu7PFparton
                                                  *
                                                  akPu7PFcorr
                                                  *
                                                  akPu7PFpatJets
                                                  *
                                                  akPu7PFAnalyzer
                                                  )

akPu7PFSequence_data = cms.Sequence(akPu7PFcorr
                                                    *
                                                    akPu7PFpatJets
                                                    *
                                                    akPu7PFAnalyzer
                                                    )


akPu7PFSequence = akPu7PFSequence_mc
