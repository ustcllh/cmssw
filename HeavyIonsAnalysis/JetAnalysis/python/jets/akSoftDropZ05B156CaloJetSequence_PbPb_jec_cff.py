

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropZ05B156Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B156CaloJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akSoftDropZ05B156CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B156HiSignalGenJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akSoftDropZ05B156Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropZ05B156CaloJets")
                                                        )

akSoftDropZ05B156Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropZ05B156CaloJets"),
    payload = "AK6Calo_offline"
    )

akSoftDropZ05B156CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropZ05B156CaloJets'))

#akSoftDropZ05B156Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak6HiSignalGenJets'))

akSoftDropZ05B156CalobTagger = bTaggers("akSoftDropZ05B156Calo",0.6)

#create objects locally since they dont load properly otherwise
#akSoftDropZ05B156Calomatch = akSoftDropZ05B156CalobTagger.match
akSoftDropZ05B156Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropZ05B156CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akSoftDropZ05B156CaloPatJetFlavourAssociationLegacy = akSoftDropZ05B156CalobTagger.PatJetFlavourAssociationLegacy
akSoftDropZ05B156CaloPatJetPartons = akSoftDropZ05B156CalobTagger.PatJetPartons
akSoftDropZ05B156CaloJetTracksAssociatorAtVertex = akSoftDropZ05B156CalobTagger.JetTracksAssociatorAtVertex
akSoftDropZ05B156CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropZ05B156CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B156CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B156CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B156CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B156CaloCombinedSecondaryVertexBJetTags = akSoftDropZ05B156CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B156CaloCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B156CalobTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropZ05B156CaloJetBProbabilityBJetTags = akSoftDropZ05B156CalobTagger.JetBProbabilityBJetTags
akSoftDropZ05B156CaloSoftPFMuonByPtBJetTags = akSoftDropZ05B156CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B156CaloSoftPFMuonByIP3dBJetTags = akSoftDropZ05B156CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B156CaloTrackCountingHighEffBJetTags = akSoftDropZ05B156CalobTagger.TrackCountingHighEffBJetTags
akSoftDropZ05B156CaloTrackCountingHighPurBJetTags = akSoftDropZ05B156CalobTagger.TrackCountingHighPurBJetTags
akSoftDropZ05B156CaloPatJetPartonAssociationLegacy = akSoftDropZ05B156CalobTagger.PatJetPartonAssociationLegacy

akSoftDropZ05B156CaloImpactParameterTagInfos = akSoftDropZ05B156CalobTagger.ImpactParameterTagInfos
akSoftDropZ05B156CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B156CaloJetProbabilityBJetTags = akSoftDropZ05B156CalobTagger.JetProbabilityBJetTags

akSoftDropZ05B156CaloSecondaryVertexTagInfos = akSoftDropZ05B156CalobTagger.SecondaryVertexTagInfos
akSoftDropZ05B156CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B156CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B156CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B156CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B156CaloCombinedSecondaryVertexBJetTags = akSoftDropZ05B156CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B156CaloCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B156CalobTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropZ05B156CaloSecondaryVertexNegativeTagInfos = akSoftDropZ05B156CalobTagger.SecondaryVertexNegativeTagInfos
akSoftDropZ05B156CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B156CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B156CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B156CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B156CaloNegativeCombinedSecondaryVertexBJetTags = akSoftDropZ05B156CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropZ05B156CaloPositiveCombinedSecondaryVertexBJetTags = akSoftDropZ05B156CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropZ05B156CaloNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B156CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropZ05B156CaloPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B156CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropZ05B156CaloSoftPFMuonsTagInfos = akSoftDropZ05B156CalobTagger.SoftPFMuonsTagInfos
akSoftDropZ05B156CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B156CaloSoftPFMuonBJetTags = akSoftDropZ05B156CalobTagger.SoftPFMuonBJetTags
akSoftDropZ05B156CaloSoftPFMuonByIP3dBJetTags = akSoftDropZ05B156CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B156CaloSoftPFMuonByPtBJetTags = akSoftDropZ05B156CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B156CaloNegativeSoftPFMuonByPtBJetTags = akSoftDropZ05B156CalobTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropZ05B156CaloPositiveSoftPFMuonByPtBJetTags = akSoftDropZ05B156CalobTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropZ05B156CaloPatJetFlavourIdLegacy = cms.Sequence(akSoftDropZ05B156CaloPatJetPartonAssociationLegacy*akSoftDropZ05B156CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropZ05B156CaloPatJetFlavourAssociation = akSoftDropZ05B156CalobTagger.PatJetFlavourAssociation
#akSoftDropZ05B156CaloPatJetFlavourId = cms.Sequence(akSoftDropZ05B156CaloPatJetPartons*akSoftDropZ05B156CaloPatJetFlavourAssociation)

akSoftDropZ05B156CaloJetBtaggingIP       = cms.Sequence(akSoftDropZ05B156CaloImpactParameterTagInfos *
            (akSoftDropZ05B156CaloTrackCountingHighEffBJetTags +
             akSoftDropZ05B156CaloTrackCountingHighPurBJetTags +
             akSoftDropZ05B156CaloJetProbabilityBJetTags +
             akSoftDropZ05B156CaloJetBProbabilityBJetTags 
            )
            )

akSoftDropZ05B156CaloJetBtaggingSV = cms.Sequence(akSoftDropZ05B156CaloImpactParameterTagInfos
            *
            akSoftDropZ05B156CaloSecondaryVertexTagInfos
            * (akSoftDropZ05B156CaloSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropZ05B156CaloSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropZ05B156CaloCombinedSecondaryVertexBJetTags+
                akSoftDropZ05B156CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropZ05B156CaloJetBtaggingNegSV = cms.Sequence(akSoftDropZ05B156CaloImpactParameterTagInfos
            *
            akSoftDropZ05B156CaloSecondaryVertexNegativeTagInfos
            * (akSoftDropZ05B156CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropZ05B156CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropZ05B156CaloNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropZ05B156CaloPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropZ05B156CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropZ05B156CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropZ05B156CaloJetBtaggingMu = cms.Sequence(akSoftDropZ05B156CaloSoftPFMuonsTagInfos * (akSoftDropZ05B156CaloSoftPFMuonBJetTags
                +
                akSoftDropZ05B156CaloSoftPFMuonByIP3dBJetTags
                +
                akSoftDropZ05B156CaloSoftPFMuonByPtBJetTags
                +
                akSoftDropZ05B156CaloNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropZ05B156CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropZ05B156CaloJetBtagging = cms.Sequence(akSoftDropZ05B156CaloJetBtaggingIP
            *akSoftDropZ05B156CaloJetBtaggingSV
            *akSoftDropZ05B156CaloJetBtaggingNegSV
#            *akSoftDropZ05B156CaloJetBtaggingMu
            )

akSoftDropZ05B156CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropZ05B156CaloJets"),
        genJetMatch          = cms.InputTag("akSoftDropZ05B156Calomatch"),
        genPartonMatch       = cms.InputTag("akSoftDropZ05B156Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropZ05B156Calocorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropZ05B156CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropZ05B156CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropZ05B156CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropZ05B156CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropZ05B156CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropZ05B156CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropZ05B156CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropZ05B156CaloJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropZ05B156CaloJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropZ05B156CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropZ05B156CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropZ05B156CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropZ05B156CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropZ05B156CaloJetID"),
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

akSoftDropZ05B156CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropZ05B156CaloJets"),
           	    R0  = cms.double( 0.6)
)
akSoftDropZ05B156CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropZ05B156CaloNjettiness:tau1','akSoftDropZ05B156CaloNjettiness:tau2','akSoftDropZ05B156CaloNjettiness:tau3']

akSoftDropZ05B156CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropZ05B156CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak6HiSignalGenJets',
                                                             rParam = 0.6,
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
                                                             bTagJetName = cms.untracked.string("akSoftDropZ05B156Calo"),
                                                             jetName = cms.untracked.string("akSoftDropZ05B156Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B156GenJets"),
                                                             doGenTaus = cms.untracked.bool(False),
                                                             genTau1 = cms.InputTag("akSoftDropZ05B156GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropZ05B156GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropZ05B156GenNjettiness","tau3"),
                                                             doGenSym = cms.untracked.bool(True),
                                                             genSym = cms.InputTag("akSoftDropZ05B156GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropZ05B156GenJets","droppedBranches")
                                                             )

akSoftDropZ05B156CaloJetSequence_mc = cms.Sequence(
                                                  #akSoftDropZ05B156Caloclean
                                                  #*
                                                  akSoftDropZ05B156Calomatch
                                                  #*
                                                  #akSoftDropZ05B156CalomatchGroomed
                                                  *
                                                  akSoftDropZ05B156Caloparton
                                                  *
                                                  akSoftDropZ05B156Calocorr
                                                  *
                                                  #akSoftDropZ05B156CaloJetID
                                                  #*
                                                  akSoftDropZ05B156CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropZ05B156CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropZ05B156CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropZ05B156CaloJetBtagging
                                                  *
                                                  akSoftDropZ05B156CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropZ05B156CalopatJetsWithBtagging
                                                  *
                                                  akSoftDropZ05B156CaloJetAnalyzer
                                                  )

akSoftDropZ05B156CaloJetSequence_data = cms.Sequence(akSoftDropZ05B156Calocorr
                                                    *
                                                    #akSoftDropZ05B156CaloJetID
                                                    #*
                                                    akSoftDropZ05B156CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropZ05B156CaloJetBtagging
                                                    *
                                                    akSoftDropZ05B156CaloNjettiness 
                                                    *
                                                    akSoftDropZ05B156CalopatJetsWithBtagging
                                                    *
                                                    akSoftDropZ05B156CaloJetAnalyzer
                                                    )

akSoftDropZ05B156CaloJetSequence_jec = cms.Sequence(akSoftDropZ05B156CaloJetSequence_mc)
akSoftDropZ05B156CaloJetSequence_mb = cms.Sequence(akSoftDropZ05B156CaloJetSequence_mc)

akSoftDropZ05B156CaloJetSequence = cms.Sequence(akSoftDropZ05B156CaloJetSequence_jec)
akSoftDropZ05B156CaloJetAnalyzer.genPtMin = cms.untracked.double(1)
akSoftDropZ05B156CaloJetAnalyzer.jetPtMin = cms.double(1)
akSoftDropZ05B156CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropZ05B156CaloJets:sym']
akSoftDropZ05B156CalopatJetsWithBtagging.userData.userInts.src += ['akSoftDropZ05B156CaloJets:droppedBranches']
