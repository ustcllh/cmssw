
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu6Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu6CaloJets"),
    matched = cms.InputTag("ak6GenJets")
    )

akPu6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu6CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu6Calocorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu6CaloJets"),
    payload = "CAPak6OBJECT"
    )

akPu6CalopatJets = patJets.clone(jetSource = cms.InputTag("akPu6CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu6Calocorr")),
                                               genJetMatch = cms.InputTag("akPu6Calomatch"),
                                               genPartonMatch = cms.InputTag("akPu6Caloparton"),
                                               jetIDMap = cms.InputTag("akPu6CaloJetID"),
                                               )

akPu6CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu6CalopatJets"),
                                                             genjetTag = 'ak6GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu6CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu6CaloSequence_mc = cms.Sequence(akPu6Calomatch
                                                  *
                                                  akPu6Caloparton
                                                  *
                                                  akPu6Calocorr
                                                  *
                                                  akPu6CalopatJets
                                                  *
                                                  akPu6CaloAnalyzer
                                                  )

akPu6CaloSequence_data = cms.Sequence(akPu6Calocorr
                                                    *
                                                    akPu6CalopatJets
                                                    *
                                                    akPu6CaloAnalyzer
                                                    )


akPu6CaloSequence = akPu6CaloSequence_mc
