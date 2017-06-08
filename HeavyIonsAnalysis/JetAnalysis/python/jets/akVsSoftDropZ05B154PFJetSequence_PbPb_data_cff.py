

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropZ05B154PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropZ05B154PFJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akVsSoftDropZ05B154PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B154HiSignalGenJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akVsSoftDropZ05B154PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B154PFJets")
                                                        )

akVsSoftDropZ05B154PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropZ05B154PFJets"),
    payload = "AK4PF_offline"
    )

akVsSoftDropZ05B154PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropZ05B154CaloJets'))

#akVsSoftDropZ05B154PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak4HiSignalGenJets'))

akVsSoftDropZ05B154PFbTagger = bTaggers("akVsSoftDropZ05B154PF",0.4)

#create objects locally since they dont load properly otherwise
#akVsSoftDropZ05B154PFmatch = akVsSoftDropZ05B154PFbTagger.match
akVsSoftDropZ05B154PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B154PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropZ05B154PFPatJetFlavourAssociationLegacy = akVsSoftDropZ05B154PFbTagger.PatJetFlavourAssociationLegacy
akVsSoftDropZ05B154PFPatJetPartons = akVsSoftDropZ05B154PFbTagger.PatJetPartons
akVsSoftDropZ05B154PFJetTracksAssociatorAtVertex = akVsSoftDropZ05B154PFbTagger.JetTracksAssociatorAtVertex
akVsSoftDropZ05B154PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropZ05B154PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B154PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B154PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B154PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B154PFCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B154PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B154PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B154PFbTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B154PFJetBProbabilityBJetTags = akVsSoftDropZ05B154PFbTagger.JetBProbabilityBJetTags
akVsSoftDropZ05B154PFSoftPFMuonByPtBJetTags = akVsSoftDropZ05B154PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B154PFSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B154PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B154PFTrackCountingHighEffBJetTags = akVsSoftDropZ05B154PFbTagger.TrackCountingHighEffBJetTags
akVsSoftDropZ05B154PFTrackCountingHighPurBJetTags = akVsSoftDropZ05B154PFbTagger.TrackCountingHighPurBJetTags
akVsSoftDropZ05B154PFPatJetPartonAssociationLegacy = akVsSoftDropZ05B154PFbTagger.PatJetPartonAssociationLegacy

akVsSoftDropZ05B154PFImpactParameterTagInfos = akVsSoftDropZ05B154PFbTagger.ImpactParameterTagInfos
akVsSoftDropZ05B154PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B154PFJetProbabilityBJetTags = akVsSoftDropZ05B154PFbTagger.JetProbabilityBJetTags

akVsSoftDropZ05B154PFSecondaryVertexTagInfos = akVsSoftDropZ05B154PFbTagger.SecondaryVertexTagInfos
akVsSoftDropZ05B154PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B154PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B154PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B154PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B154PFCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B154PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B154PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B154PFbTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B154PFSecondaryVertexNegativeTagInfos = akVsSoftDropZ05B154PFbTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropZ05B154PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B154PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B154PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B154PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B154PFNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B154PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B154PFPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B154PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B154PFNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B154PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B154PFPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B154PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B154PFSoftPFMuonsTagInfos = akVsSoftDropZ05B154PFbTagger.SoftPFMuonsTagInfos
akVsSoftDropZ05B154PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B154PFSoftPFMuonBJetTags = akVsSoftDropZ05B154PFbTagger.SoftPFMuonBJetTags
akVsSoftDropZ05B154PFSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B154PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B154PFSoftPFMuonByPtBJetTags = akVsSoftDropZ05B154PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B154PFNegativeSoftPFMuonByPtBJetTags = akVsSoftDropZ05B154PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropZ05B154PFPositiveSoftPFMuonByPtBJetTags = akVsSoftDropZ05B154PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropZ05B154PFPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropZ05B154PFPatJetPartonAssociationLegacy*akVsSoftDropZ05B154PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropZ05B154PFPatJetFlavourAssociation = akVsSoftDropZ05B154PFbTagger.PatJetFlavourAssociation
#akVsSoftDropZ05B154PFPatJetFlavourId = cms.Sequence(akVsSoftDropZ05B154PFPatJetPartons*akVsSoftDropZ05B154PFPatJetFlavourAssociation)

akVsSoftDropZ05B154PFJetBtaggingIP       = cms.Sequence(akVsSoftDropZ05B154PFImpactParameterTagInfos *
            (akVsSoftDropZ05B154PFTrackCountingHighEffBJetTags +
             akVsSoftDropZ05B154PFTrackCountingHighPurBJetTags +
             akVsSoftDropZ05B154PFJetProbabilityBJetTags +
             akVsSoftDropZ05B154PFJetBProbabilityBJetTags 
            )
            )

akVsSoftDropZ05B154PFJetBtaggingSV = cms.Sequence(akVsSoftDropZ05B154PFImpactParameterTagInfos
            *
            akVsSoftDropZ05B154PFSecondaryVertexTagInfos
            * (akVsSoftDropZ05B154PFSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B154PFSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B154PFCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B154PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B154PFJetBtaggingNegSV = cms.Sequence(akVsSoftDropZ05B154PFImpactParameterTagInfos
            *
            akVsSoftDropZ05B154PFSecondaryVertexNegativeTagInfos
            * (akVsSoftDropZ05B154PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B154PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B154PFNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B154PFPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B154PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropZ05B154PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B154PFJetBtaggingMu = cms.Sequence(akVsSoftDropZ05B154PFSoftPFMuonsTagInfos * (akVsSoftDropZ05B154PFSoftPFMuonBJetTags
                +
                akVsSoftDropZ05B154PFSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropZ05B154PFSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B154PFNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B154PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropZ05B154PFJetBtagging = cms.Sequence(akVsSoftDropZ05B154PFJetBtaggingIP
            *akVsSoftDropZ05B154PFJetBtaggingSV
            *akVsSoftDropZ05B154PFJetBtaggingNegSV
#            *akVsSoftDropZ05B154PFJetBtaggingMu
            )

akVsSoftDropZ05B154PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropZ05B154PFJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropZ05B154PFmatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropZ05B154PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B154PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropZ05B154PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropZ05B154PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropZ05B154PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B154PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B154PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropZ05B154PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropZ05B154PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropZ05B154PFJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropZ05B154PFJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B154PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B154PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropZ05B154PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B154PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropZ05B154PFJetID"),
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

akVsSoftDropZ05B154PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropZ05B154PFJets"),
           	    R0  = cms.double( 0.4)
)
akVsSoftDropZ05B154PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B154PFNjettiness:tau1','akVsSoftDropZ05B154PFNjettiness:tau2','akVsSoftDropZ05B154PFNjettiness:tau3']

akVsSoftDropZ05B154PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropZ05B154PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak4HiSignalGenJets',
                                                             rParam = 0.4,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
							     doSubEvent = False,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akVsSoftDropZ05B154PF"),
                                                             jetName = cms.untracked.string("akVsSoftDropZ05B154PF"),
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

akVsSoftDropZ05B154PFJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropZ05B154PFclean
                                                  #*
                                                  akVsSoftDropZ05B154PFmatch
                                                  #*
                                                  #akVsSoftDropZ05B154PFmatchGroomed
                                                  *
                                                  akVsSoftDropZ05B154PFparton
                                                  *
                                                  akVsSoftDropZ05B154PFcorr
                                                  *
                                                  #akVsSoftDropZ05B154PFJetID
                                                  #*
                                                  akVsSoftDropZ05B154PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropZ05B154PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropZ05B154PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropZ05B154PFJetBtagging
                                                  *
                                                  akVsSoftDropZ05B154PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropZ05B154PFpatJetsWithBtagging
                                                  *
                                                  akVsSoftDropZ05B154PFJetAnalyzer
                                                  )

akVsSoftDropZ05B154PFJetSequence_data = cms.Sequence(akVsSoftDropZ05B154PFcorr
                                                    *
                                                    #akVsSoftDropZ05B154PFJetID
                                                    #*
                                                    akVsSoftDropZ05B154PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropZ05B154PFJetBtagging
                                                    *
                                                    akVsSoftDropZ05B154PFNjettiness 
                                                    *
                                                    akVsSoftDropZ05B154PFpatJetsWithBtagging
                                                    *
                                                    akVsSoftDropZ05B154PFJetAnalyzer
                                                    )

akVsSoftDropZ05B154PFJetSequence_jec = cms.Sequence(akVsSoftDropZ05B154PFJetSequence_mc)
akVsSoftDropZ05B154PFJetSequence_mb = cms.Sequence(akVsSoftDropZ05B154PFJetSequence_mc)

akVsSoftDropZ05B154PFJetSequence = cms.Sequence(akVsSoftDropZ05B154PFJetSequence_data)
akVsSoftDropZ05B154PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B154PFJets:sym']
akVsSoftDropZ05B154PFpatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropZ05B154PFJets:droppedBranches']
