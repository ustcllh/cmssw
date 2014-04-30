

import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from HeavyIonsAnalysis.JetAnalysis.JPTJetAnalyzer_cff import *

akPu5JPTmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKtPu5"),
    matched = cms.InputTag("ak5HiGenJetsCleaned")
    )

akPu5JPTparton = patJetPartonMatch.clone(src = cms.InputTag("JetPlusTrackZSPCorJetAntiKtPu5"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

akPu5JPTcorr = patJetCorrFactors.clone(
    useNPV = True,
    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L1Offset','L1JPTOffset','L2Relative','L3Absolute'),
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKtPu5"),
    payload = "AK5JPT",
#    extraJPTOffset = cms.string("L1Offset")
    )

akPu5JPTpatJets = patJets.clone(
                                               jetSource = cms.InputTag("JetPlusTrackZSPCorJetAntiKtPu5"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5JPTcorr")),
                                               genJetMatch = cms.InputTag("akPu5JPTmatch"),
                                               genPartonMatch = cms.InputTag("akPu5JPTparton"),
                                               jetIDMap = cms.InputTag("ak5CaloJetID"),
					       addBTagInfo         = False,
                                               addTagInfos         = False,
                                               addDiscriminators   = False,
                                               addAssociatedTracks = False,
                                               addJetCharge        = False,
                                               addJetID            = False,
                                               getJetMCFlavour     = False,
                                               addGenPartonMatch   = False, 
                                               addGenJetMatch      = False,
                                               embedGenJetMatch    = False,
                                               embedGenPartonMatch = False,
                                               embedCaloTowers     = False,
                                               embedPFCandidates = False
				            )

akPu5JPTJetAnalyzer = JPTJetAnalyzer.clone(jetTag = cms.InputTag("akPu5JPTpatJets"),
                                                             genjetTag = 'ak5HiGenJetsCleaned',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akPu5CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )

akPu5JPTJetSequence_mc = cms.Sequence(
						  akPu5JPTmatch
                                                  *
                                                  akPu5JPTparton
                                                  *
                                                  akPu5JPTcorr
                                                  *
                                                  akPu5JPTpatJets
                                                  *
                                                  akPu5JPTJetAnalyzer
                                                  )

akPu5JPTJetSequence_data = cms.Sequence(
						    akPu5JPTcorr
                                                    *
                                                    akPu5JPTpatJets
                                                    *
                                                    akPu5JPTJetAnalyzer
                                                    )

akPu5JPTJetSequence = cms.Sequence(akPu5JPTJetSequence_data)
