
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu5Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu5CaloJets"),
    matched = cms.InputTag("ak5GenJets")
    )

akPu5Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu5CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu5Calocorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu5CaloJets"),
    payload = "CAPak5OBJECT"
    )

akPu5CalopatJets = patJets.clone(jetSource = cms.InputTag("akPu5CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5Calocorr")),
                                               genJetMatch = cms.InputTag("akPu5Calomatch"),
                                               genPartonMatch = cms.InputTag("akPu5Caloparton"),
                                               jetIDMap = cms.InputTag("akPu5CaloJetID"),
                                               )

akPu5CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu5CalopatJets"),
                                                             genjetTag = 'ak5GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu5CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu5CaloSequence_mc = cms.Sequence(akPu5Calomatch
                                                  *
                                                  akPu5Caloparton
                                                  *
                                                  akPu5Calocorr
                                                  *
                                                  akPu5CalopatJets
                                                  *
                                                  akPu5CaloAnalyzer
                                                  )

akPu5CaloSequence_data = cms.Sequence(akPu5Calocorr
                                                    *
                                                    akPu5CalopatJets
                                                    *
                                                    akPu5CaloAnalyzer
                                                    )


akPu5CaloSequence = akPu5CaloSequence_mc
