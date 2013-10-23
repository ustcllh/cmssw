
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu4PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu4PFJets"),
    matched = cms.InputTag("ak4GenJets")
    )

akPu4PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPu4PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu4PFcorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu4PFJets"),
    payload = "CAPak4OBJECT"
    )

akPu4PFpatJets = patJets.clone(jetSource = cms.InputTag("akPu4PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4PFcorr")),
                                               genJetMatch = cms.InputTag("akPu4PFmatch"),
                                               genPartonMatch = cms.InputTag("akPu4PFparton"),
                                               jetIDMap = cms.InputTag("akPu4PFJetID"),
                                               )

akPu4PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu4PFpatJets"),
                                                             genjetTag = 'ak4GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu4PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu4PFSequence_mc = cms.Sequence(akPu4PFmatch
                                                  *
                                                  akPu4PFparton
                                                  *
                                                  akPu4PFcorr
                                                  *
                                                  akPu4PFpatJets
                                                  *
                                                  akPu4PFAnalyzer
                                                  )

akPu4PFSequence_data = cms.Sequence(akPu4PFcorr
                                                    *
                                                    akPu4PFpatJets
                                                    *
                                                    akPu4PFAnalyzer
                                                    )


akPu4PFSequence = akPu4PFSequence_data
