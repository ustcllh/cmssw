
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu7Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu7CaloJets"),
    matched = cms.InputTag("ak7GenJets")
    )

akPu7Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu7CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu7Calocorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu7CaloJets"),
    payload = "CAPak7OBJECT"
    )

akPu7CalopatJets = patJets.clone(jetSource = cms.InputTag("akPu7CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu7Calocorr")),
                                               genJetMatch = cms.InputTag("akPu7Calomatch"),
                                               genPartonMatch = cms.InputTag("akPu7Caloparton"),
                                               jetIDMap = cms.InputTag("akPu7CaloJetID"),
                                               )

akPu7CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu7CalopatJets"),
                                                             genjetTag = 'ak7GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu7CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu7CaloSequence_mc = cms.Sequence(akPu7Calomatch
                                                  *
                                                  akPu7Caloparton
                                                  *
                                                  akPu7Calocorr
                                                  *
                                                  akPu7CalopatJets
                                                  *
                                                  akPu7CaloAnalyzer
                                                  )

akPu7CaloSequence_data = cms.Sequence(akPu7Calocorr
                                                    *
                                                    akPu7CalopatJets
                                                    *
                                                    akPu7CaloAnalyzer
                                                    )


akPu7CaloSequence = akPu7CaloSequence_mc
