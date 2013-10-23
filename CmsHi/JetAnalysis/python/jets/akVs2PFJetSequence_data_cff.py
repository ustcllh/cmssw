
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs2PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs2PFJets"),
    matched = cms.InputTag("ak2HiGenJets")
    )

akVs2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs2PFJets"),
                                                        matched = cms.InputTag("hiGenParticles")
                                                        )

akVs2PFcorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs2PFJets"),
    payload = "AK2PF_hiIterativeTracks"
    )

akVs2PFpatJets = patJets.clone(jetSource = cms.InputTag("akVs2PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs2PFcorr")),
                                               genJetMatch = cms.InputTag("akVs2PFmatch"),
                                               genPartonMatch = cms.InputTag("akVs2PFparton"),
                                               jetIDMap = cms.InputTag("akVs2PFJetID"),
                                               addBTagInfo         = False,
                                               addTagInfos         = False,
                                               addDiscriminators   = False,
                                               addAssociatedTracks = False,
                                               addJetCharge        = False,
                                               addJetID            = True,
                                               getJetMCFlavour     = False,
                                               addGenPartonMatch   = True,
                                               addGenJetMatch      = True,
                                               embedGenJetMatch    = True,
                                               embedGenPartonMatch = True,
                                               embedCaloTowers     = False,
				            )

akVs2PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs2PFpatJets"),
                                                             genjetTag = 'ak2HiGenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs2PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs2PFJetSequence_mc = cms.Sequence(akVs2PFmatch
                                                  *
                                                  akVs2PFparton
                                                  *
                                                  akVs2PFcorr
                                                  *
                                                  akVs2PFpatJets
                                                  *
                                                  akVs2PFAnalyzer
                                                  )

akVs2PFJetSequence_data = cms.Sequence(akVs2PFcorr
                                                    *
                                                    akVs2PFpatJets
                                                    *
                                                    akVs2PFAnalyzer
                                                    )

akVs2PFJetSequence = cms.Sequence(akVs2PFJetSequence_data)
