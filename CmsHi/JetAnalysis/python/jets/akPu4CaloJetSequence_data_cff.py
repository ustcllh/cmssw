
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akPu4Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu4CaloJets"),
    matched = cms.InputTag("ak4GenJets")
    )

akPu4Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu4CaloJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akPu4Calocorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akPu4CaloJets"),
    payload = "CAPak4OBJECT"
    )

akPu4CalopatJets = patJets.clone(jetSource = cms.InputTag("akPu4CaloJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4Calocorr")),
                                               genJetMatch = cms.InputTag("akPu4Calomatch"),
                                               genPartonMatch = cms.InputTag("akPu4Caloparton"),
                                               jetIDMap = cms.InputTag("akPu4CaloJetID"),
                                               )

akPu4CaloAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu4CalopatJets"),
                                                             genjetTag = 'ak4GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu4CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akPu4CaloSequence_mc = cms.Sequence(akPu4Calomatch
                                                  *
                                                  akPu4Caloparton
                                                  *
                                                  akPu4Calocorr
                                                  *
                                                  akPu4CalopatJets
                                                  *
                                                  akPu4CaloAnalyzer
                                                  )

akPu4CaloSequence_data = cms.Sequence(akPu4Calocorr
                                                    *
                                                    akPu4CalopatJets
                                                    *
                                                    akPu4CaloAnalyzer
                                                    )


akPu4CaloSequence = akPu4CaloSequence_data
