
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs7PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs7PFJets"),
    matched = cms.InputTag("ak7GenJets")
    )

akVs7PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs7PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs7PFcorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs7PFJets"),
    payload = "CAPak7OBJECT"
    )

akVs7PFpatJets = patJets.clone(jetSource = cms.InputTag("akVs7PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs7PFcorr")),
                                               genJetMatch = cms.InputTag("akVs7PFmatch"),
                                               genPartonMatch = cms.InputTag("akVs7PFparton"),
                                               jetIDMap = cms.InputTag("akVs7PFJetID"),
                                               )

akVs7PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs7PFpatJets"),
                                                             genjetTag = 'ak7GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs7PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs7PFSequence_mc = cms.Sequence(akVs7PFmatch
                                                  *
                                                  akVs7PFparton
                                                  *
                                                  akVs7PFcorr
                                                  *
                                                  akVs7PFpatJets
                                                  *
                                                  akVs7PFAnalyzer
                                                  )

akVs7PFSequence_data = cms.Sequence(akVs7PFcorr
                                                    *
                                                    akVs7PFpatJets
                                                    *
                                                    akVs7PFAnalyzer
                                                    )


akVs7PFSequence = akVs7PFSequence_mc
