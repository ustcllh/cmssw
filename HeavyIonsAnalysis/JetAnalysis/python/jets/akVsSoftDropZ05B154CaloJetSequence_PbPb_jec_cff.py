

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropZ05B154Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropZ05B154CaloJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akVsSoftDropZ05B154CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B154HiSignalGenJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akVsSoftDropZ05B154Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B154CaloJets")
                                                        )

akVsSoftDropZ05B154Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropZ05B154CaloJets"),
    payload = "AK4Calo_offline"
    )

akVsSoftDropZ05B154CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropZ05B154CaloJets'))

#akVsSoftDropZ05B154Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak4HiSignalGenJets'))

akVsSoftDropZ05B154CalobTagger = bTaggers("akVsSoftDropZ05B154Calo",0.4)

#create objects locally since they dont load properly otherwise
#akVsSoftDropZ05B154Calomatch = akVsSoftDropZ05B154CalobTagger.match
akVsSoftDropZ05B154Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B154CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropZ05B154CaloPatJetFlavourAssociationLegacy = akVsSoftDropZ05B154CalobTagger.PatJetFlavourAssociationLegacy
akVsSoftDropZ05B154CaloPatJetPartons = akVsSoftDropZ05B154CalobTagger.PatJetPartons
akVsSoftDropZ05B154CaloJetTracksAssociatorAtVertex = akVsSoftDropZ05B154CalobTagger.JetTracksAssociatorAtVertex
akVsSoftDropZ05B154CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropZ05B154CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B154CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B154CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B154CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B154CaloCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B154CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B154CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B154CalobTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B154CaloJetBProbabilityBJetTags = akVsSoftDropZ05B154CalobTagger.JetBProbabilityBJetTags
akVsSoftDropZ05B154CaloSoftPFMuonByPtBJetTags = akVsSoftDropZ05B154CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B154CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B154CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B154CaloTrackCountingHighEffBJetTags = akVsSoftDropZ05B154CalobTagger.TrackCountingHighEffBJetTags
akVsSoftDropZ05B154CaloTrackCountingHighPurBJetTags = akVsSoftDropZ05B154CalobTagger.TrackCountingHighPurBJetTags
akVsSoftDropZ05B154CaloPatJetPartonAssociationLegacy = akVsSoftDropZ05B154CalobTagger.PatJetPartonAssociationLegacy

akVsSoftDropZ05B154CaloImpactParameterTagInfos = akVsSoftDropZ05B154CalobTagger.ImpactParameterTagInfos
akVsSoftDropZ05B154CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B154CaloJetProbabilityBJetTags = akVsSoftDropZ05B154CalobTagger.JetProbabilityBJetTags

akVsSoftDropZ05B154CaloSecondaryVertexTagInfos = akVsSoftDropZ05B154CalobTagger.SecondaryVertexTagInfos
akVsSoftDropZ05B154CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B154CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B154CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B154CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B154CaloCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B154CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B154CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B154CalobTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B154CaloSecondaryVertexNegativeTagInfos = akVsSoftDropZ05B154CalobTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropZ05B154CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B154CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B154CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B154CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B154CaloNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B154CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B154CaloPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B154CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B154CaloNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B154CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B154CaloPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B154CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B154CaloSoftPFMuonsTagInfos = akVsSoftDropZ05B154CalobTagger.SoftPFMuonsTagInfos
akVsSoftDropZ05B154CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B154CaloSoftPFMuonBJetTags = akVsSoftDropZ05B154CalobTagger.SoftPFMuonBJetTags
akVsSoftDropZ05B154CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B154CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B154CaloSoftPFMuonByPtBJetTags = akVsSoftDropZ05B154CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B154CaloNegativeSoftPFMuonByPtBJetTags = akVsSoftDropZ05B154CalobTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropZ05B154CaloPositiveSoftPFMuonByPtBJetTags = akVsSoftDropZ05B154CalobTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropZ05B154CaloPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropZ05B154CaloPatJetPartonAssociationLegacy*akVsSoftDropZ05B154CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropZ05B154CaloPatJetFlavourAssociation = akVsSoftDropZ05B154CalobTagger.PatJetFlavourAssociation
#akVsSoftDropZ05B154CaloPatJetFlavourId = cms.Sequence(akVsSoftDropZ05B154CaloPatJetPartons*akVsSoftDropZ05B154CaloPatJetFlavourAssociation)

akVsSoftDropZ05B154CaloJetBtaggingIP       = cms.Sequence(akVsSoftDropZ05B154CaloImpactParameterTagInfos *
            (akVsSoftDropZ05B154CaloTrackCountingHighEffBJetTags +
             akVsSoftDropZ05B154CaloTrackCountingHighPurBJetTags +
             akVsSoftDropZ05B154CaloJetProbabilityBJetTags +
             akVsSoftDropZ05B154CaloJetBProbabilityBJetTags 
            )
            )

akVsSoftDropZ05B154CaloJetBtaggingSV = cms.Sequence(akVsSoftDropZ05B154CaloImpactParameterTagInfos
            *
            akVsSoftDropZ05B154CaloSecondaryVertexTagInfos
            * (akVsSoftDropZ05B154CaloSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B154CaloSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B154CaloCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B154CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B154CaloJetBtaggingNegSV = cms.Sequence(akVsSoftDropZ05B154CaloImpactParameterTagInfos
            *
            akVsSoftDropZ05B154CaloSecondaryVertexNegativeTagInfos
            * (akVsSoftDropZ05B154CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B154CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B154CaloNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B154CaloPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B154CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropZ05B154CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B154CaloJetBtaggingMu = cms.Sequence(akVsSoftDropZ05B154CaloSoftPFMuonsTagInfos * (akVsSoftDropZ05B154CaloSoftPFMuonBJetTags
                +
                akVsSoftDropZ05B154CaloSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropZ05B154CaloSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B154CaloNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B154CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropZ05B154CaloJetBtagging = cms.Sequence(akVsSoftDropZ05B154CaloJetBtaggingIP
            *akVsSoftDropZ05B154CaloJetBtaggingSV
            *akVsSoftDropZ05B154CaloJetBtaggingNegSV
#            *akVsSoftDropZ05B154CaloJetBtaggingMu
            )

akVsSoftDropZ05B154CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropZ05B154CaloJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropZ05B154Calomatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropZ05B154Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B154Calocorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropZ05B154CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropZ05B154CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropZ05B154CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B154CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B154CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropZ05B154CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropZ05B154CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropZ05B154CaloJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropZ05B154CaloJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B154CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B154CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropZ05B154CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B154CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropZ05B154CaloJetID"),
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

akVsSoftDropZ05B154CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropZ05B154CaloJets"),
           	    R0  = cms.double( 0.4)
)
akVsSoftDropZ05B154CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B154CaloNjettiness:tau1','akVsSoftDropZ05B154CaloNjettiness:tau2','akVsSoftDropZ05B154CaloNjettiness:tau3']

akVsSoftDropZ05B154CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropZ05B154CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak4HiSignalGenJets',
                                                             rParam = 0.4,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropZ05B154Calo"),
                                                             jetName = cms.untracked.string("akVsSoftDropZ05B154Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B154GenJets"),
                                                             doGenTaus = cms.untracked.bool(False),
                                                             genTau1 = cms.InputTag("akSoftDropZ05B154GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropZ05B154GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropZ05B154GenNjettiness","tau3"),
                                                             doGenSym = cms.untracked.bool(True),
                                                             genSym = cms.InputTag("akSoftDropZ05B154GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropZ05B154GenJets","droppedBranches")
                                                             )

akVsSoftDropZ05B154CaloJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropZ05B154Caloclean
                                                  #*
                                                  akVsSoftDropZ05B154Calomatch
                                                  #*
                                                  #akVsSoftDropZ05B154CalomatchGroomed
                                                  *
                                                  akVsSoftDropZ05B154Caloparton
                                                  *
                                                  akVsSoftDropZ05B154Calocorr
                                                  *
                                                  #akVsSoftDropZ05B154CaloJetID
                                                  #*
                                                  akVsSoftDropZ05B154CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropZ05B154CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropZ05B154CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropZ05B154CaloJetBtagging
                                                  *
                                                  akVsSoftDropZ05B154CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropZ05B154CalopatJetsWithBtagging
                                                  *
                                                  akVsSoftDropZ05B154CaloJetAnalyzer
                                                  )

akVsSoftDropZ05B154CaloJetSequence_data = cms.Sequence(akVsSoftDropZ05B154Calocorr
                                                    *
                                                    #akVsSoftDropZ05B154CaloJetID
                                                    #*
                                                    akVsSoftDropZ05B154CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropZ05B154CaloJetBtagging
                                                    *
                                                    akVsSoftDropZ05B154CaloNjettiness 
                                                    *
                                                    akVsSoftDropZ05B154CalopatJetsWithBtagging
                                                    *
                                                    akVsSoftDropZ05B154CaloJetAnalyzer
                                                    )

akVsSoftDropZ05B154CaloJetSequence_jec = cms.Sequence(akVsSoftDropZ05B154CaloJetSequence_mc)
akVsSoftDropZ05B154CaloJetSequence_mb = cms.Sequence(akVsSoftDropZ05B154CaloJetSequence_mc)

akVsSoftDropZ05B154CaloJetSequence = cms.Sequence(akVsSoftDropZ05B154CaloJetSequence_jec)
akVsSoftDropZ05B154CaloJetAnalyzer.genPtMin = cms.untracked.double(1)
akVsSoftDropZ05B154CaloJetAnalyzer.jetPtMin = cms.double(1)
akVsSoftDropZ05B154CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B154CaloJets:sym']
akVsSoftDropZ05B154CalopatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropZ05B154CaloJets:droppedBranches']
