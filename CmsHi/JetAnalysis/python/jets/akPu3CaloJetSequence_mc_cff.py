
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu3Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu3CaloJets"),
    matched = cms.InputTag("ak3GenJets")
    )

akPu3Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu3CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu3Calocorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu3CaloJets"),
    payload = "CAPak3OBJECT"
    )

akPu3CalopatJets = patJets.clone(jetSource = cms.InputTag("akPu3CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3Calocorr")),
                                               genJetMatch = cms.InputTag("akPu3Calomatch"),
                                               genPartonMatch = cms.InputTag("akPu3Caloparton"),
                                               jetIDMap = cms.InputTag("akPu3CaloJetID"),
                                               )

akPu3CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu3CalopatJets"),
                                                             genjetTag = 'ak3GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu3CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu3CaloSequence_mc = cms.Sequence(akPu3Calomatch
                                                  *
                                                  akPu3Caloparton
                                                  *
                                                  akPu3Calocorr
                                                  *
                                                  akPu3CalopatJets
                                                  *
                                                  akPu3CaloAnalyzer
                                                  )

akPu3CaloSequence_data = cms.Sequence(akPu3Calocorr
                                                    *
                                                    akPu3CalopatJets
                                                    *
                                                    akPu3CaloAnalyzer
                                                    )


akPu3CaloSequence = akPu3CaloSequence_mc
