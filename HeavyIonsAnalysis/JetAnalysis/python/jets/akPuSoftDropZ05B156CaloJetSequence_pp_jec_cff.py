

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropZ05B156Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropZ05B156CaloJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akPuSoftDropZ05B156CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B156GenJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akPuSoftDropZ05B156Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropZ05B156CaloJets")
                                                        )

akPuSoftDropZ05B156Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropZ05B156CaloJets"),
    payload = "AKPu6Calo_offline"
    )

akPuSoftDropZ05B156CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropZ05B156CaloJets'))

#akPuSoftDropZ05B156Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak6GenJets'))

akPuSoftDropZ05B156CalobTagger = bTaggers("akPuSoftDropZ05B156Calo",0.6)

#create objects locally since they dont load properly otherwise
#akPuSoftDropZ05B156Calomatch = akPuSoftDropZ05B156CalobTagger.match
akPuSoftDropZ05B156Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropZ05B156CaloJets"), matched = cms.InputTag("genParticles"))
akPuSoftDropZ05B156CaloPatJetFlavourAssociationLegacy = akPuSoftDropZ05B156CalobTagger.PatJetFlavourAssociationLegacy
akPuSoftDropZ05B156CaloPatJetPartons = akPuSoftDropZ05B156CalobTagger.PatJetPartons
akPuSoftDropZ05B156CaloJetTracksAssociatorAtVertex = akPuSoftDropZ05B156CalobTagger.JetTracksAssociatorAtVertex
akPuSoftDropZ05B156CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropZ05B156CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B156CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B156CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B156CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B156CaloCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B156CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropZ05B156CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B156CalobTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropZ05B156CaloJetBProbabilityBJetTags = akPuSoftDropZ05B156CalobTagger.JetBProbabilityBJetTags
akPuSoftDropZ05B156CaloSoftPFMuonByPtBJetTags = akPuSoftDropZ05B156CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropZ05B156CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropZ05B156CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropZ05B156CaloTrackCountingHighEffBJetTags = akPuSoftDropZ05B156CalobTagger.TrackCountingHighEffBJetTags
akPuSoftDropZ05B156CaloTrackCountingHighPurBJetTags = akPuSoftDropZ05B156CalobTagger.TrackCountingHighPurBJetTags
akPuSoftDropZ05B156CaloPatJetPartonAssociationLegacy = akPuSoftDropZ05B156CalobTagger.PatJetPartonAssociationLegacy

akPuSoftDropZ05B156CaloImpactParameterTagInfos = akPuSoftDropZ05B156CalobTagger.ImpactParameterTagInfos
akPuSoftDropZ05B156CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropZ05B156CaloJetProbabilityBJetTags = akPuSoftDropZ05B156CalobTagger.JetProbabilityBJetTags

akPuSoftDropZ05B156CaloSecondaryVertexTagInfos = akPuSoftDropZ05B156CalobTagger.SecondaryVertexTagInfos
akPuSoftDropZ05B156CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B156CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B156CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B156CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B156CaloCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B156CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropZ05B156CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B156CalobTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropZ05B156CaloSecondaryVertexNegativeTagInfos = akPuSoftDropZ05B156CalobTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropZ05B156CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B156CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B156CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B156CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B156CaloNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B156CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropZ05B156CaloPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B156CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropZ05B156CaloNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B156CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropZ05B156CaloPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B156CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropZ05B156CaloSoftPFMuonsTagInfos = akPuSoftDropZ05B156CalobTagger.SoftPFMuonsTagInfos
akPuSoftDropZ05B156CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropZ05B156CaloSoftPFMuonBJetTags = akPuSoftDropZ05B156CalobTagger.SoftPFMuonBJetTags
akPuSoftDropZ05B156CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropZ05B156CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropZ05B156CaloSoftPFMuonByPtBJetTags = akPuSoftDropZ05B156CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropZ05B156CaloNegativeSoftPFMuonByPtBJetTags = akPuSoftDropZ05B156CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropZ05B156CaloPositiveSoftPFMuonByPtBJetTags = akPuSoftDropZ05B156CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropZ05B156CaloPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropZ05B156CaloPatJetPartonAssociationLegacy*akPuSoftDropZ05B156CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropZ05B156CaloPatJetFlavourAssociation = akPuSoftDropZ05B156CalobTagger.PatJetFlavourAssociation
#akPuSoftDropZ05B156CaloPatJetFlavourId = cms.Sequence(akPuSoftDropZ05B156CaloPatJetPartons*akPuSoftDropZ05B156CaloPatJetFlavourAssociation)

akPuSoftDropZ05B156CaloJetBtaggingIP       = cms.Sequence(akPuSoftDropZ05B156CaloImpactParameterTagInfos *
            (akPuSoftDropZ05B156CaloTrackCountingHighEffBJetTags +
             akPuSoftDropZ05B156CaloTrackCountingHighPurBJetTags +
             akPuSoftDropZ05B156CaloJetProbabilityBJetTags +
             akPuSoftDropZ05B156CaloJetBProbabilityBJetTags 
            )
            )

akPuSoftDropZ05B156CaloJetBtaggingSV = cms.Sequence(akPuSoftDropZ05B156CaloImpactParameterTagInfos
            *
            akPuSoftDropZ05B156CaloSecondaryVertexTagInfos
            * (akPuSoftDropZ05B156CaloSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropZ05B156CaloSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropZ05B156CaloCombinedSecondaryVertexBJetTags+
                akPuSoftDropZ05B156CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropZ05B156CaloJetBtaggingNegSV = cms.Sequence(akPuSoftDropZ05B156CaloImpactParameterTagInfos
            *
            akPuSoftDropZ05B156CaloSecondaryVertexNegativeTagInfos
            * (akPuSoftDropZ05B156CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropZ05B156CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropZ05B156CaloNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropZ05B156CaloPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropZ05B156CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropZ05B156CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropZ05B156CaloJetBtaggingMu = cms.Sequence(akPuSoftDropZ05B156CaloSoftPFMuonsTagInfos * (akPuSoftDropZ05B156CaloSoftPFMuonBJetTags
                +
                akPuSoftDropZ05B156CaloSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropZ05B156CaloSoftPFMuonByPtBJetTags
                +
                akPuSoftDropZ05B156CaloNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropZ05B156CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropZ05B156CaloJetBtagging = cms.Sequence(akPuSoftDropZ05B156CaloJetBtaggingIP
            *akPuSoftDropZ05B156CaloJetBtaggingSV
            *akPuSoftDropZ05B156CaloJetBtaggingNegSV
#            *akPuSoftDropZ05B156CaloJetBtaggingMu
            )

akPuSoftDropZ05B156CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropZ05B156CaloJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropZ05B156Calomatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropZ05B156Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropZ05B156Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropZ05B156CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropZ05B156CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropZ05B156CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropZ05B156CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropZ05B156CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropZ05B156CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropZ05B156CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropZ05B156CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropZ05B156CaloJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropZ05B156CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropZ05B156CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropZ05B156CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropZ05B156CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropZ05B156CaloJetID"),
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

akPuSoftDropZ05B156CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropZ05B156CaloJets"),
           	    R0  = cms.double( 0.6)
)
akPuSoftDropZ05B156CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropZ05B156CaloNjettiness:tau1','akPuSoftDropZ05B156CaloNjettiness:tau2','akPuSoftDropZ05B156CaloNjettiness:tau3']

akPuSoftDropZ05B156CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropZ05B156CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak6GenJets',
                                                             rParam = 0.6,
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
                                                             bTagJetName = cms.untracked.string("akPuSoftDropZ05B156Calo"),
                                                             jetName = cms.untracked.string("akPuSoftDropZ05B156Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
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

akPuSoftDropZ05B156CaloJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropZ05B156Caloclean
                                                  #*
                                                  akPuSoftDropZ05B156Calomatch
                                                  #*
                                                  #akPuSoftDropZ05B156CalomatchGroomed
                                                  *
                                                  akPuSoftDropZ05B156Caloparton
                                                  *
                                                  akPuSoftDropZ05B156Calocorr
                                                  *
                                                  #akPuSoftDropZ05B156CaloJetID
                                                  #*
                                                  akPuSoftDropZ05B156CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropZ05B156CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropZ05B156CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropZ05B156CaloJetBtagging
                                                  *
                                                  akPuSoftDropZ05B156CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropZ05B156CalopatJetsWithBtagging
                                                  *
                                                  akPuSoftDropZ05B156CaloJetAnalyzer
                                                  )

akPuSoftDropZ05B156CaloJetSequence_data = cms.Sequence(akPuSoftDropZ05B156Calocorr
                                                    *
                                                    #akPuSoftDropZ05B156CaloJetID
                                                    #*
                                                    akPuSoftDropZ05B156CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropZ05B156CaloJetBtagging
                                                    *
                                                    akPuSoftDropZ05B156CaloNjettiness 
                                                    *
                                                    akPuSoftDropZ05B156CalopatJetsWithBtagging
                                                    *
                                                    akPuSoftDropZ05B156CaloJetAnalyzer
                                                    )

akPuSoftDropZ05B156CaloJetSequence_jec = cms.Sequence(akPuSoftDropZ05B156CaloJetSequence_mc)
akPuSoftDropZ05B156CaloJetSequence_mb = cms.Sequence(akPuSoftDropZ05B156CaloJetSequence_mc)

akPuSoftDropZ05B156CaloJetSequence = cms.Sequence(akPuSoftDropZ05B156CaloJetSequence_jec)
akPuSoftDropZ05B156CaloJetAnalyzer.genPtMin = cms.untracked.double(1)
akPuSoftDropZ05B156CaloJetAnalyzer.jetPtMin = cms.double(1)
akPuSoftDropZ05B156CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropZ05B156CaloJets:sym']
akPuSoftDropZ05B156CalopatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropZ05B156CaloJets:droppedBranches']
