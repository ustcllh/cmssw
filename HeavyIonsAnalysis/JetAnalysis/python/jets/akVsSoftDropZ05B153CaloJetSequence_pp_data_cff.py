

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropZ05B153Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropZ05B153CaloJets"),
    matched = cms.InputTag("ak3GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akVsSoftDropZ05B153CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B153GenJets"),
    matched = cms.InputTag("ak3GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akVsSoftDropZ05B153Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B153CaloJets")
                                                        )

akVsSoftDropZ05B153Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropZ05B153CaloJets"),
    payload = "AK3Calo_offline"
    )

akVsSoftDropZ05B153CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropZ05B153CaloJets'))

#akVsSoftDropZ05B153Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak3GenJets'))

akVsSoftDropZ05B153CalobTagger = bTaggers("akVsSoftDropZ05B153Calo",0.3)

#create objects locally since they dont load properly otherwise
#akVsSoftDropZ05B153Calomatch = akVsSoftDropZ05B153CalobTagger.match
akVsSoftDropZ05B153Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B153CaloJets"), matched = cms.InputTag("genParticles"))
akVsSoftDropZ05B153CaloPatJetFlavourAssociationLegacy = akVsSoftDropZ05B153CalobTagger.PatJetFlavourAssociationLegacy
akVsSoftDropZ05B153CaloPatJetPartons = akVsSoftDropZ05B153CalobTagger.PatJetPartons
akVsSoftDropZ05B153CaloJetTracksAssociatorAtVertex = akVsSoftDropZ05B153CalobTagger.JetTracksAssociatorAtVertex
akVsSoftDropZ05B153CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropZ05B153CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B153CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B153CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B153CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B153CaloCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B153CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B153CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B153CalobTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B153CaloJetBProbabilityBJetTags = akVsSoftDropZ05B153CalobTagger.JetBProbabilityBJetTags
akVsSoftDropZ05B153CaloSoftPFMuonByPtBJetTags = akVsSoftDropZ05B153CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B153CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B153CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B153CaloTrackCountingHighEffBJetTags = akVsSoftDropZ05B153CalobTagger.TrackCountingHighEffBJetTags
akVsSoftDropZ05B153CaloTrackCountingHighPurBJetTags = akVsSoftDropZ05B153CalobTagger.TrackCountingHighPurBJetTags
akVsSoftDropZ05B153CaloPatJetPartonAssociationLegacy = akVsSoftDropZ05B153CalobTagger.PatJetPartonAssociationLegacy

akVsSoftDropZ05B153CaloImpactParameterTagInfos = akVsSoftDropZ05B153CalobTagger.ImpactParameterTagInfos
akVsSoftDropZ05B153CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B153CaloJetProbabilityBJetTags = akVsSoftDropZ05B153CalobTagger.JetProbabilityBJetTags

akVsSoftDropZ05B153CaloSecondaryVertexTagInfos = akVsSoftDropZ05B153CalobTagger.SecondaryVertexTagInfos
akVsSoftDropZ05B153CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B153CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B153CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B153CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B153CaloCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B153CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B153CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B153CalobTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B153CaloSecondaryVertexNegativeTagInfos = akVsSoftDropZ05B153CalobTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropZ05B153CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B153CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B153CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B153CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B153CaloNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B153CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B153CaloPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B153CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B153CaloNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B153CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B153CaloPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B153CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B153CaloSoftPFMuonsTagInfos = akVsSoftDropZ05B153CalobTagger.SoftPFMuonsTagInfos
akVsSoftDropZ05B153CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B153CaloSoftPFMuonBJetTags = akVsSoftDropZ05B153CalobTagger.SoftPFMuonBJetTags
akVsSoftDropZ05B153CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B153CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B153CaloSoftPFMuonByPtBJetTags = akVsSoftDropZ05B153CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B153CaloNegativeSoftPFMuonByPtBJetTags = akVsSoftDropZ05B153CalobTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropZ05B153CaloPositiveSoftPFMuonByPtBJetTags = akVsSoftDropZ05B153CalobTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropZ05B153CaloPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropZ05B153CaloPatJetPartonAssociationLegacy*akVsSoftDropZ05B153CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropZ05B153CaloPatJetFlavourAssociation = akVsSoftDropZ05B153CalobTagger.PatJetFlavourAssociation
#akVsSoftDropZ05B153CaloPatJetFlavourId = cms.Sequence(akVsSoftDropZ05B153CaloPatJetPartons*akVsSoftDropZ05B153CaloPatJetFlavourAssociation)

akVsSoftDropZ05B153CaloJetBtaggingIP       = cms.Sequence(akVsSoftDropZ05B153CaloImpactParameterTagInfos *
            (akVsSoftDropZ05B153CaloTrackCountingHighEffBJetTags +
             akVsSoftDropZ05B153CaloTrackCountingHighPurBJetTags +
             akVsSoftDropZ05B153CaloJetProbabilityBJetTags +
             akVsSoftDropZ05B153CaloJetBProbabilityBJetTags 
            )
            )

akVsSoftDropZ05B153CaloJetBtaggingSV = cms.Sequence(akVsSoftDropZ05B153CaloImpactParameterTagInfos
            *
            akVsSoftDropZ05B153CaloSecondaryVertexTagInfos
            * (akVsSoftDropZ05B153CaloSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B153CaloSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B153CaloCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B153CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B153CaloJetBtaggingNegSV = cms.Sequence(akVsSoftDropZ05B153CaloImpactParameterTagInfos
            *
            akVsSoftDropZ05B153CaloSecondaryVertexNegativeTagInfos
            * (akVsSoftDropZ05B153CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B153CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B153CaloNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B153CaloPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B153CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropZ05B153CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B153CaloJetBtaggingMu = cms.Sequence(akVsSoftDropZ05B153CaloSoftPFMuonsTagInfos * (akVsSoftDropZ05B153CaloSoftPFMuonBJetTags
                +
                akVsSoftDropZ05B153CaloSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropZ05B153CaloSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B153CaloNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B153CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropZ05B153CaloJetBtagging = cms.Sequence(akVsSoftDropZ05B153CaloJetBtaggingIP
            *akVsSoftDropZ05B153CaloJetBtaggingSV
            *akVsSoftDropZ05B153CaloJetBtaggingNegSV
#            *akVsSoftDropZ05B153CaloJetBtaggingMu
            )

akVsSoftDropZ05B153CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropZ05B153CaloJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropZ05B153Calomatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropZ05B153Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B153Calocorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropZ05B153CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropZ05B153CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropZ05B153CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B153CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B153CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropZ05B153CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropZ05B153CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropZ05B153CaloJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropZ05B153CaloJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B153CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B153CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropZ05B153CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B153CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropZ05B153CaloJetID"),
        addBTagInfo = True,
        addTagInfos = True,
        addDiscriminators = True,
        addAssociatedTracks = True,
        addJetCharge = False,
        addJetID = False,
        getJetMCFlavour = False,
        addGenPartonMatch = False,
        addGenJetMatch = False,
        embedGenJetMatch = False,
        embedGenPartonMatch = False,
        # embedCaloTowers = False,
        # embedPFCandidates = True
        )

akVsSoftDropZ05B153CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropZ05B153CaloJets"),
           	    R0  = cms.double( 0.3)
)
akVsSoftDropZ05B153CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B153CaloNjettiness:tau1','akVsSoftDropZ05B153CaloNjettiness:tau2','akVsSoftDropZ05B153CaloNjettiness:tau3']

akVsSoftDropZ05B153CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropZ05B153CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak3GenJets',
                                                             rParam = 0.3,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
							     doSubEvent = False,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akVsSoftDropZ05B153Calo"),
                                                             jetName = cms.untracked.string("akVsSoftDropZ05B153Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B153GenJets"),
                                                             doGenTaus = cms.untracked.bool(False),
                                                             genTau1 = cms.InputTag("akSoftDropZ05B153GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropZ05B153GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropZ05B153GenNjettiness","tau3"),
                                                             doGenSym = cms.untracked.bool(True),
                                                             genSym = cms.InputTag("akSoftDropZ05B153GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropZ05B153GenJets","droppedBranches")
                                                             )

akVsSoftDropZ05B153CaloJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropZ05B153Caloclean
                                                  #*
                                                  akVsSoftDropZ05B153Calomatch
                                                  #*
                                                  #akVsSoftDropZ05B153CalomatchGroomed
                                                  *
                                                  akVsSoftDropZ05B153Caloparton
                                                  *
                                                  akVsSoftDropZ05B153Calocorr
                                                  *
                                                  #akVsSoftDropZ05B153CaloJetID
                                                  #*
                                                  akVsSoftDropZ05B153CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropZ05B153CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropZ05B153CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropZ05B153CaloJetBtagging
                                                  *
                                                  akVsSoftDropZ05B153CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropZ05B153CalopatJetsWithBtagging
                                                  *
                                                  akVsSoftDropZ05B153CaloJetAnalyzer
                                                  )

akVsSoftDropZ05B153CaloJetSequence_data = cms.Sequence(akVsSoftDropZ05B153Calocorr
                                                    *
                                                    #akVsSoftDropZ05B153CaloJetID
                                                    #*
                                                    akVsSoftDropZ05B153CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropZ05B153CaloJetBtagging
                                                    *
                                                    akVsSoftDropZ05B153CaloNjettiness 
                                                    *
                                                    akVsSoftDropZ05B153CalopatJetsWithBtagging
                                                    *
                                                    akVsSoftDropZ05B153CaloJetAnalyzer
                                                    )

akVsSoftDropZ05B153CaloJetSequence_jec = cms.Sequence(akVsSoftDropZ05B153CaloJetSequence_mc)
akVsSoftDropZ05B153CaloJetSequence_mb = cms.Sequence(akVsSoftDropZ05B153CaloJetSequence_mc)

akVsSoftDropZ05B153CaloJetSequence = cms.Sequence(akVsSoftDropZ05B153CaloJetSequence_data)
akVsSoftDropZ05B153CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B153CaloJets:sym']
akVsSoftDropZ05B153CalopatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropZ05B153CaloJets:droppedBranches']
