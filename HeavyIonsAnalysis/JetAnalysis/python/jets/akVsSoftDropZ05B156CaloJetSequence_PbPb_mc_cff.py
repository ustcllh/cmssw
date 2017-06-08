

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropZ05B156Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropZ05B156CaloJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akVsSoftDropZ05B156CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B156HiSignalGenJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akVsSoftDropZ05B156Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B156CaloJets")
                                                        )

akVsSoftDropZ05B156Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropZ05B156CaloJets"),
    payload = "AK6Calo_offline"
    )

akVsSoftDropZ05B156CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropZ05B156CaloJets'))

#akVsSoftDropZ05B156Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak6HiSignalGenJets'))

akVsSoftDropZ05B156CalobTagger = bTaggers("akVsSoftDropZ05B156Calo",0.6)

#create objects locally since they dont load properly otherwise
#akVsSoftDropZ05B156Calomatch = akVsSoftDropZ05B156CalobTagger.match
akVsSoftDropZ05B156Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B156CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropZ05B156CaloPatJetFlavourAssociationLegacy = akVsSoftDropZ05B156CalobTagger.PatJetFlavourAssociationLegacy
akVsSoftDropZ05B156CaloPatJetPartons = akVsSoftDropZ05B156CalobTagger.PatJetPartons
akVsSoftDropZ05B156CaloJetTracksAssociatorAtVertex = akVsSoftDropZ05B156CalobTagger.JetTracksAssociatorAtVertex
akVsSoftDropZ05B156CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropZ05B156CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B156CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B156CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B156CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B156CaloCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B156CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B156CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B156CalobTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B156CaloJetBProbabilityBJetTags = akVsSoftDropZ05B156CalobTagger.JetBProbabilityBJetTags
akVsSoftDropZ05B156CaloSoftPFMuonByPtBJetTags = akVsSoftDropZ05B156CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B156CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B156CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B156CaloTrackCountingHighEffBJetTags = akVsSoftDropZ05B156CalobTagger.TrackCountingHighEffBJetTags
akVsSoftDropZ05B156CaloTrackCountingHighPurBJetTags = akVsSoftDropZ05B156CalobTagger.TrackCountingHighPurBJetTags
akVsSoftDropZ05B156CaloPatJetPartonAssociationLegacy = akVsSoftDropZ05B156CalobTagger.PatJetPartonAssociationLegacy

akVsSoftDropZ05B156CaloImpactParameterTagInfos = akVsSoftDropZ05B156CalobTagger.ImpactParameterTagInfos
akVsSoftDropZ05B156CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B156CaloJetProbabilityBJetTags = akVsSoftDropZ05B156CalobTagger.JetProbabilityBJetTags

akVsSoftDropZ05B156CaloSecondaryVertexTagInfos = akVsSoftDropZ05B156CalobTagger.SecondaryVertexTagInfos
akVsSoftDropZ05B156CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B156CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B156CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B156CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B156CaloCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B156CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B156CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B156CalobTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B156CaloSecondaryVertexNegativeTagInfos = akVsSoftDropZ05B156CalobTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropZ05B156CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B156CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B156CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B156CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B156CaloNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B156CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B156CaloPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B156CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B156CaloNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B156CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B156CaloPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B156CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B156CaloSoftPFMuonsTagInfos = akVsSoftDropZ05B156CalobTagger.SoftPFMuonsTagInfos
akVsSoftDropZ05B156CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B156CaloSoftPFMuonBJetTags = akVsSoftDropZ05B156CalobTagger.SoftPFMuonBJetTags
akVsSoftDropZ05B156CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B156CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B156CaloSoftPFMuonByPtBJetTags = akVsSoftDropZ05B156CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B156CaloNegativeSoftPFMuonByPtBJetTags = akVsSoftDropZ05B156CalobTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropZ05B156CaloPositiveSoftPFMuonByPtBJetTags = akVsSoftDropZ05B156CalobTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropZ05B156CaloPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropZ05B156CaloPatJetPartonAssociationLegacy*akVsSoftDropZ05B156CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropZ05B156CaloPatJetFlavourAssociation = akVsSoftDropZ05B156CalobTagger.PatJetFlavourAssociation
#akVsSoftDropZ05B156CaloPatJetFlavourId = cms.Sequence(akVsSoftDropZ05B156CaloPatJetPartons*akVsSoftDropZ05B156CaloPatJetFlavourAssociation)

akVsSoftDropZ05B156CaloJetBtaggingIP       = cms.Sequence(akVsSoftDropZ05B156CaloImpactParameterTagInfos *
            (akVsSoftDropZ05B156CaloTrackCountingHighEffBJetTags +
             akVsSoftDropZ05B156CaloTrackCountingHighPurBJetTags +
             akVsSoftDropZ05B156CaloJetProbabilityBJetTags +
             akVsSoftDropZ05B156CaloJetBProbabilityBJetTags 
            )
            )

akVsSoftDropZ05B156CaloJetBtaggingSV = cms.Sequence(akVsSoftDropZ05B156CaloImpactParameterTagInfos
            *
            akVsSoftDropZ05B156CaloSecondaryVertexTagInfos
            * (akVsSoftDropZ05B156CaloSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B156CaloSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B156CaloCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B156CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B156CaloJetBtaggingNegSV = cms.Sequence(akVsSoftDropZ05B156CaloImpactParameterTagInfos
            *
            akVsSoftDropZ05B156CaloSecondaryVertexNegativeTagInfos
            * (akVsSoftDropZ05B156CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B156CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B156CaloNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B156CaloPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B156CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropZ05B156CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B156CaloJetBtaggingMu = cms.Sequence(akVsSoftDropZ05B156CaloSoftPFMuonsTagInfos * (akVsSoftDropZ05B156CaloSoftPFMuonBJetTags
                +
                akVsSoftDropZ05B156CaloSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropZ05B156CaloSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B156CaloNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B156CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropZ05B156CaloJetBtagging = cms.Sequence(akVsSoftDropZ05B156CaloJetBtaggingIP
            *akVsSoftDropZ05B156CaloJetBtaggingSV
            *akVsSoftDropZ05B156CaloJetBtaggingNegSV
#            *akVsSoftDropZ05B156CaloJetBtaggingMu
            )

akVsSoftDropZ05B156CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropZ05B156CaloJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropZ05B156Calomatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropZ05B156Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B156Calocorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropZ05B156CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropZ05B156CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropZ05B156CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B156CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B156CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropZ05B156CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropZ05B156CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropZ05B156CaloJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropZ05B156CaloJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B156CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B156CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropZ05B156CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B156CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropZ05B156CaloJetID"),
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

akVsSoftDropZ05B156CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropZ05B156CaloJets"),
           	    R0  = cms.double( 0.6)
)
akVsSoftDropZ05B156CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B156CaloNjettiness:tau1','akVsSoftDropZ05B156CaloNjettiness:tau2','akVsSoftDropZ05B156CaloNjettiness:tau3']

akVsSoftDropZ05B156CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropZ05B156CalopatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropZ05B156Calo"),
                                                             jetName = cms.untracked.string("akVsSoftDropZ05B156Calo"),
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

akVsSoftDropZ05B156CaloJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropZ05B156Caloclean
                                                  #*
                                                  akVsSoftDropZ05B156Calomatch
                                                  #*
                                                  #akVsSoftDropZ05B156CalomatchGroomed
                                                  *
                                                  akVsSoftDropZ05B156Caloparton
                                                  *
                                                  akVsSoftDropZ05B156Calocorr
                                                  *
                                                  #akVsSoftDropZ05B156CaloJetID
                                                  #*
                                                  akVsSoftDropZ05B156CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropZ05B156CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropZ05B156CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropZ05B156CaloJetBtagging
                                                  *
                                                  akVsSoftDropZ05B156CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropZ05B156CalopatJetsWithBtagging
                                                  *
                                                  akVsSoftDropZ05B156CaloJetAnalyzer
                                                  )

akVsSoftDropZ05B156CaloJetSequence_data = cms.Sequence(akVsSoftDropZ05B156Calocorr
                                                    *
                                                    #akVsSoftDropZ05B156CaloJetID
                                                    #*
                                                    akVsSoftDropZ05B156CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropZ05B156CaloJetBtagging
                                                    *
                                                    akVsSoftDropZ05B156CaloNjettiness 
                                                    *
                                                    akVsSoftDropZ05B156CalopatJetsWithBtagging
                                                    *
                                                    akVsSoftDropZ05B156CaloJetAnalyzer
                                                    )

akVsSoftDropZ05B156CaloJetSequence_jec = cms.Sequence(akVsSoftDropZ05B156CaloJetSequence_mc)
akVsSoftDropZ05B156CaloJetSequence_mb = cms.Sequence(akVsSoftDropZ05B156CaloJetSequence_mc)

akVsSoftDropZ05B156CaloJetSequence = cms.Sequence(akVsSoftDropZ05B156CaloJetSequence_mc)
akVsSoftDropZ05B156CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B156CaloJets:sym']
akVsSoftDropZ05B156CalopatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropZ05B156CaloJets:droppedBranches']
