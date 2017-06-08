

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropZ05B155Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropZ05B155CaloJets"),
    matched = cms.InputTag("ak5GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akPuSoftDropZ05B155CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B155GenJets"),
    matched = cms.InputTag("ak5GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akPuSoftDropZ05B155Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropZ05B155CaloJets")
                                                        )

akPuSoftDropZ05B155Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropZ05B155CaloJets"),
    payload = "AKPu5Calo_offline"
    )

akPuSoftDropZ05B155CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropZ05B155CaloJets'))

#akPuSoftDropZ05B155Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak5GenJets'))

akPuSoftDropZ05B155CalobTagger = bTaggers("akPuSoftDropZ05B155Calo",0.5)

#create objects locally since they dont load properly otherwise
#akPuSoftDropZ05B155Calomatch = akPuSoftDropZ05B155CalobTagger.match
akPuSoftDropZ05B155Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropZ05B155CaloJets"), matched = cms.InputTag("genParticles"))
akPuSoftDropZ05B155CaloPatJetFlavourAssociationLegacy = akPuSoftDropZ05B155CalobTagger.PatJetFlavourAssociationLegacy
akPuSoftDropZ05B155CaloPatJetPartons = akPuSoftDropZ05B155CalobTagger.PatJetPartons
akPuSoftDropZ05B155CaloJetTracksAssociatorAtVertex = akPuSoftDropZ05B155CalobTagger.JetTracksAssociatorAtVertex
akPuSoftDropZ05B155CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropZ05B155CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B155CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B155CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B155CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B155CaloCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B155CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropZ05B155CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B155CalobTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropZ05B155CaloJetBProbabilityBJetTags = akPuSoftDropZ05B155CalobTagger.JetBProbabilityBJetTags
akPuSoftDropZ05B155CaloSoftPFMuonByPtBJetTags = akPuSoftDropZ05B155CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropZ05B155CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropZ05B155CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropZ05B155CaloTrackCountingHighEffBJetTags = akPuSoftDropZ05B155CalobTagger.TrackCountingHighEffBJetTags
akPuSoftDropZ05B155CaloTrackCountingHighPurBJetTags = akPuSoftDropZ05B155CalobTagger.TrackCountingHighPurBJetTags
akPuSoftDropZ05B155CaloPatJetPartonAssociationLegacy = akPuSoftDropZ05B155CalobTagger.PatJetPartonAssociationLegacy

akPuSoftDropZ05B155CaloImpactParameterTagInfos = akPuSoftDropZ05B155CalobTagger.ImpactParameterTagInfos
akPuSoftDropZ05B155CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropZ05B155CaloJetProbabilityBJetTags = akPuSoftDropZ05B155CalobTagger.JetProbabilityBJetTags

akPuSoftDropZ05B155CaloSecondaryVertexTagInfos = akPuSoftDropZ05B155CalobTagger.SecondaryVertexTagInfos
akPuSoftDropZ05B155CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B155CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B155CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B155CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B155CaloCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B155CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropZ05B155CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B155CalobTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropZ05B155CaloSecondaryVertexNegativeTagInfos = akPuSoftDropZ05B155CalobTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropZ05B155CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B155CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B155CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B155CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B155CaloNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B155CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropZ05B155CaloPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B155CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropZ05B155CaloNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B155CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropZ05B155CaloPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B155CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropZ05B155CaloSoftPFMuonsTagInfos = akPuSoftDropZ05B155CalobTagger.SoftPFMuonsTagInfos
akPuSoftDropZ05B155CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropZ05B155CaloSoftPFMuonBJetTags = akPuSoftDropZ05B155CalobTagger.SoftPFMuonBJetTags
akPuSoftDropZ05B155CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropZ05B155CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropZ05B155CaloSoftPFMuonByPtBJetTags = akPuSoftDropZ05B155CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropZ05B155CaloNegativeSoftPFMuonByPtBJetTags = akPuSoftDropZ05B155CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropZ05B155CaloPositiveSoftPFMuonByPtBJetTags = akPuSoftDropZ05B155CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropZ05B155CaloPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropZ05B155CaloPatJetPartonAssociationLegacy*akPuSoftDropZ05B155CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropZ05B155CaloPatJetFlavourAssociation = akPuSoftDropZ05B155CalobTagger.PatJetFlavourAssociation
#akPuSoftDropZ05B155CaloPatJetFlavourId = cms.Sequence(akPuSoftDropZ05B155CaloPatJetPartons*akPuSoftDropZ05B155CaloPatJetFlavourAssociation)

akPuSoftDropZ05B155CaloJetBtaggingIP       = cms.Sequence(akPuSoftDropZ05B155CaloImpactParameterTagInfos *
            (akPuSoftDropZ05B155CaloTrackCountingHighEffBJetTags +
             akPuSoftDropZ05B155CaloTrackCountingHighPurBJetTags +
             akPuSoftDropZ05B155CaloJetProbabilityBJetTags +
             akPuSoftDropZ05B155CaloJetBProbabilityBJetTags 
            )
            )

akPuSoftDropZ05B155CaloJetBtaggingSV = cms.Sequence(akPuSoftDropZ05B155CaloImpactParameterTagInfos
            *
            akPuSoftDropZ05B155CaloSecondaryVertexTagInfos
            * (akPuSoftDropZ05B155CaloSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropZ05B155CaloSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropZ05B155CaloCombinedSecondaryVertexBJetTags+
                akPuSoftDropZ05B155CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropZ05B155CaloJetBtaggingNegSV = cms.Sequence(akPuSoftDropZ05B155CaloImpactParameterTagInfos
            *
            akPuSoftDropZ05B155CaloSecondaryVertexNegativeTagInfos
            * (akPuSoftDropZ05B155CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropZ05B155CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropZ05B155CaloNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropZ05B155CaloPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropZ05B155CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropZ05B155CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropZ05B155CaloJetBtaggingMu = cms.Sequence(akPuSoftDropZ05B155CaloSoftPFMuonsTagInfos * (akPuSoftDropZ05B155CaloSoftPFMuonBJetTags
                +
                akPuSoftDropZ05B155CaloSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropZ05B155CaloSoftPFMuonByPtBJetTags
                +
                akPuSoftDropZ05B155CaloNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropZ05B155CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropZ05B155CaloJetBtagging = cms.Sequence(akPuSoftDropZ05B155CaloJetBtaggingIP
            *akPuSoftDropZ05B155CaloJetBtaggingSV
            *akPuSoftDropZ05B155CaloJetBtaggingNegSV
#            *akPuSoftDropZ05B155CaloJetBtaggingMu
            )

akPuSoftDropZ05B155CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropZ05B155CaloJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropZ05B155Calomatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropZ05B155Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropZ05B155Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropZ05B155CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropZ05B155CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropZ05B155CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropZ05B155CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropZ05B155CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropZ05B155CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropZ05B155CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropZ05B155CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropZ05B155CaloJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropZ05B155CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropZ05B155CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropZ05B155CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropZ05B155CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropZ05B155CaloJetID"),
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

akPuSoftDropZ05B155CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropZ05B155CaloJets"),
           	    R0  = cms.double( 0.5)
)
akPuSoftDropZ05B155CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropZ05B155CaloNjettiness:tau1','akPuSoftDropZ05B155CaloNjettiness:tau2','akPuSoftDropZ05B155CaloNjettiness:tau3']

akPuSoftDropZ05B155CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropZ05B155CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak5GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
							     doSubEvent = True,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akPuSoftDropZ05B155Calo"),
                                                             jetName = cms.untracked.string("akPuSoftDropZ05B155Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
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

akPuSoftDropZ05B155CaloJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropZ05B155Caloclean
                                                  #*
                                                  akPuSoftDropZ05B155Calomatch
                                                  #*
                                                  #akPuSoftDropZ05B155CalomatchGroomed
                                                  *
                                                  akPuSoftDropZ05B155Caloparton
                                                  *
                                                  akPuSoftDropZ05B155Calocorr
                                                  *
                                                  #akPuSoftDropZ05B155CaloJetID
                                                  #*
                                                  akPuSoftDropZ05B155CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropZ05B155CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropZ05B155CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropZ05B155CaloJetBtagging
                                                  *
                                                  akPuSoftDropZ05B155CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropZ05B155CalopatJetsWithBtagging
                                                  *
                                                  akPuSoftDropZ05B155CaloJetAnalyzer
                                                  )

akPuSoftDropZ05B155CaloJetSequence_data = cms.Sequence(akPuSoftDropZ05B155Calocorr
                                                    *
                                                    #akPuSoftDropZ05B155CaloJetID
                                                    #*
                                                    akPuSoftDropZ05B155CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropZ05B155CaloJetBtagging
                                                    *
                                                    akPuSoftDropZ05B155CaloNjettiness 
                                                    *
                                                    akPuSoftDropZ05B155CalopatJetsWithBtagging
                                                    *
                                                    akPuSoftDropZ05B155CaloJetAnalyzer
                                                    )

akPuSoftDropZ05B155CaloJetSequence_jec = cms.Sequence(akPuSoftDropZ05B155CaloJetSequence_mc)
akPuSoftDropZ05B155CaloJetSequence_mb = cms.Sequence(akPuSoftDropZ05B155CaloJetSequence_mc)

akPuSoftDropZ05B155CaloJetSequence = cms.Sequence(akPuSoftDropZ05B155CaloJetSequence_mc)
akPuSoftDropZ05B155CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropZ05B155CaloJets:sym']
akPuSoftDropZ05B155CalopatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropZ05B155CaloJets:droppedBranches']
