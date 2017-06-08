

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropZ05B155Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B155CaloJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akSoftDropZ05B155CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B155HiSignalGenJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akSoftDropZ05B155Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropZ05B155CaloJets")
                                                        )

akSoftDropZ05B155Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropZ05B155CaloJets"),
    payload = "AK5Calo_offline"
    )

akSoftDropZ05B155CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropZ05B155CaloJets'))

#akSoftDropZ05B155Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak5HiSignalGenJets'))

akSoftDropZ05B155CalobTagger = bTaggers("akSoftDropZ05B155Calo",0.5)

#create objects locally since they dont load properly otherwise
#akSoftDropZ05B155Calomatch = akSoftDropZ05B155CalobTagger.match
akSoftDropZ05B155Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropZ05B155CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akSoftDropZ05B155CaloPatJetFlavourAssociationLegacy = akSoftDropZ05B155CalobTagger.PatJetFlavourAssociationLegacy
akSoftDropZ05B155CaloPatJetPartons = akSoftDropZ05B155CalobTagger.PatJetPartons
akSoftDropZ05B155CaloJetTracksAssociatorAtVertex = akSoftDropZ05B155CalobTagger.JetTracksAssociatorAtVertex
akSoftDropZ05B155CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropZ05B155CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B155CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B155CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B155CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B155CaloCombinedSecondaryVertexBJetTags = akSoftDropZ05B155CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B155CaloCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B155CalobTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropZ05B155CaloJetBProbabilityBJetTags = akSoftDropZ05B155CalobTagger.JetBProbabilityBJetTags
akSoftDropZ05B155CaloSoftPFMuonByPtBJetTags = akSoftDropZ05B155CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B155CaloSoftPFMuonByIP3dBJetTags = akSoftDropZ05B155CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B155CaloTrackCountingHighEffBJetTags = akSoftDropZ05B155CalobTagger.TrackCountingHighEffBJetTags
akSoftDropZ05B155CaloTrackCountingHighPurBJetTags = akSoftDropZ05B155CalobTagger.TrackCountingHighPurBJetTags
akSoftDropZ05B155CaloPatJetPartonAssociationLegacy = akSoftDropZ05B155CalobTagger.PatJetPartonAssociationLegacy

akSoftDropZ05B155CaloImpactParameterTagInfos = akSoftDropZ05B155CalobTagger.ImpactParameterTagInfos
akSoftDropZ05B155CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B155CaloJetProbabilityBJetTags = akSoftDropZ05B155CalobTagger.JetProbabilityBJetTags

akSoftDropZ05B155CaloSecondaryVertexTagInfos = akSoftDropZ05B155CalobTagger.SecondaryVertexTagInfos
akSoftDropZ05B155CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B155CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B155CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B155CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B155CaloCombinedSecondaryVertexBJetTags = akSoftDropZ05B155CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B155CaloCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B155CalobTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropZ05B155CaloSecondaryVertexNegativeTagInfos = akSoftDropZ05B155CalobTagger.SecondaryVertexNegativeTagInfos
akSoftDropZ05B155CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B155CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B155CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B155CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B155CaloNegativeCombinedSecondaryVertexBJetTags = akSoftDropZ05B155CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropZ05B155CaloPositiveCombinedSecondaryVertexBJetTags = akSoftDropZ05B155CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropZ05B155CaloNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B155CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropZ05B155CaloPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B155CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropZ05B155CaloSoftPFMuonsTagInfos = akSoftDropZ05B155CalobTagger.SoftPFMuonsTagInfos
akSoftDropZ05B155CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B155CaloSoftPFMuonBJetTags = akSoftDropZ05B155CalobTagger.SoftPFMuonBJetTags
akSoftDropZ05B155CaloSoftPFMuonByIP3dBJetTags = akSoftDropZ05B155CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B155CaloSoftPFMuonByPtBJetTags = akSoftDropZ05B155CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B155CaloNegativeSoftPFMuonByPtBJetTags = akSoftDropZ05B155CalobTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropZ05B155CaloPositiveSoftPFMuonByPtBJetTags = akSoftDropZ05B155CalobTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropZ05B155CaloPatJetFlavourIdLegacy = cms.Sequence(akSoftDropZ05B155CaloPatJetPartonAssociationLegacy*akSoftDropZ05B155CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropZ05B155CaloPatJetFlavourAssociation = akSoftDropZ05B155CalobTagger.PatJetFlavourAssociation
#akSoftDropZ05B155CaloPatJetFlavourId = cms.Sequence(akSoftDropZ05B155CaloPatJetPartons*akSoftDropZ05B155CaloPatJetFlavourAssociation)

akSoftDropZ05B155CaloJetBtaggingIP       = cms.Sequence(akSoftDropZ05B155CaloImpactParameterTagInfos *
            (akSoftDropZ05B155CaloTrackCountingHighEffBJetTags +
             akSoftDropZ05B155CaloTrackCountingHighPurBJetTags +
             akSoftDropZ05B155CaloJetProbabilityBJetTags +
             akSoftDropZ05B155CaloJetBProbabilityBJetTags 
            )
            )

akSoftDropZ05B155CaloJetBtaggingSV = cms.Sequence(akSoftDropZ05B155CaloImpactParameterTagInfos
            *
            akSoftDropZ05B155CaloSecondaryVertexTagInfos
            * (akSoftDropZ05B155CaloSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropZ05B155CaloSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropZ05B155CaloCombinedSecondaryVertexBJetTags+
                akSoftDropZ05B155CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropZ05B155CaloJetBtaggingNegSV = cms.Sequence(akSoftDropZ05B155CaloImpactParameterTagInfos
            *
            akSoftDropZ05B155CaloSecondaryVertexNegativeTagInfos
            * (akSoftDropZ05B155CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropZ05B155CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropZ05B155CaloNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropZ05B155CaloPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropZ05B155CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropZ05B155CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropZ05B155CaloJetBtaggingMu = cms.Sequence(akSoftDropZ05B155CaloSoftPFMuonsTagInfos * (akSoftDropZ05B155CaloSoftPFMuonBJetTags
                +
                akSoftDropZ05B155CaloSoftPFMuonByIP3dBJetTags
                +
                akSoftDropZ05B155CaloSoftPFMuonByPtBJetTags
                +
                akSoftDropZ05B155CaloNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropZ05B155CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropZ05B155CaloJetBtagging = cms.Sequence(akSoftDropZ05B155CaloJetBtaggingIP
            *akSoftDropZ05B155CaloJetBtaggingSV
            *akSoftDropZ05B155CaloJetBtaggingNegSV
#            *akSoftDropZ05B155CaloJetBtaggingMu
            )

akSoftDropZ05B155CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropZ05B155CaloJets"),
        genJetMatch          = cms.InputTag("akSoftDropZ05B155Calomatch"),
        genPartonMatch       = cms.InputTag("akSoftDropZ05B155Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropZ05B155Calocorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropZ05B155CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropZ05B155CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropZ05B155CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropZ05B155CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropZ05B155CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropZ05B155CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropZ05B155CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropZ05B155CaloJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropZ05B155CaloJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropZ05B155CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropZ05B155CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropZ05B155CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropZ05B155CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropZ05B155CaloJetID"),
        addBTagInfo = True,
        addTagInfos = True,
        addDiscriminators = True,
        addAssociatedTracks = True,
        addJetCharge = False,
        addJetID = False,
        getJetMCFlavour = True,
        addGenPartonMatch = True,
        addGenJetMatch = True,
        embedGenJetMatch = True,
        embedGenPartonMatch = True,
        # embedCaloTowers = False,
        # embedPFCandidates = True
        )

akSoftDropZ05B155CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropZ05B155CaloJets"),
           	    R0  = cms.double( 0.5)
)
akSoftDropZ05B155CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropZ05B155CaloNjettiness:tau1','akSoftDropZ05B155CaloNjettiness:tau2','akSoftDropZ05B155CaloNjettiness:tau3']

akSoftDropZ05B155CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropZ05B155CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak5HiSignalGenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
							     doSubEvent = True,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akSoftDropZ05B155Calo"),
                                                             jetName = cms.untracked.string("akSoftDropZ05B155Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B155GenJets"),
                                                             doGenTaus = cms.untracked.bool(False),
                                                             genTau1 = cms.InputTag("akSoftDropZ05B155GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropZ05B155GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropZ05B155GenNjettiness","tau3"),
                                                             doGenSym = cms.untracked.bool(True),
                                                             genSym = cms.InputTag("akSoftDropZ05B155GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropZ05B155GenJets","droppedBranches")
                                                             )

akSoftDropZ05B155CaloJetSequence_mc = cms.Sequence(
                                                  #akSoftDropZ05B155Caloclean
                                                  #*
                                                  akSoftDropZ05B155Calomatch
                                                  #*
                                                  #akSoftDropZ05B155CalomatchGroomed
                                                  *
                                                  akSoftDropZ05B155Caloparton
                                                  *
                                                  akSoftDropZ05B155Calocorr
                                                  *
                                                  #akSoftDropZ05B155CaloJetID
                                                  #*
                                                  akSoftDropZ05B155CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropZ05B155CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropZ05B155CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropZ05B155CaloJetBtagging
                                                  *
                                                  akSoftDropZ05B155CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropZ05B155CalopatJetsWithBtagging
                                                  *
                                                  akSoftDropZ05B155CaloJetAnalyzer
                                                  )

akSoftDropZ05B155CaloJetSequence_data = cms.Sequence(akSoftDropZ05B155Calocorr
                                                    *
                                                    #akSoftDropZ05B155CaloJetID
                                                    #*
                                                    akSoftDropZ05B155CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropZ05B155CaloJetBtagging
                                                    *
                                                    akSoftDropZ05B155CaloNjettiness 
                                                    *
                                                    akSoftDropZ05B155CalopatJetsWithBtagging
                                                    *
                                                    akSoftDropZ05B155CaloJetAnalyzer
                                                    )

akSoftDropZ05B155CaloJetSequence_jec = cms.Sequence(akSoftDropZ05B155CaloJetSequence_mc)
akSoftDropZ05B155CaloJetSequence_mb = cms.Sequence(akSoftDropZ05B155CaloJetSequence_mc)

akSoftDropZ05B155CaloJetSequence = cms.Sequence(akSoftDropZ05B155CaloJetSequence_mc)
akSoftDropZ05B155CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropZ05B155CaloJets:sym']
akSoftDropZ05B155CalopatJetsWithBtagging.userData.userInts.src += ['akSoftDropZ05B155CaloJets:droppedBranches']
