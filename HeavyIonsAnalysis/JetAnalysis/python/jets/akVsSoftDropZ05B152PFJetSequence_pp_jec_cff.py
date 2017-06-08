

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropZ05B152PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropZ05B152PFJets"),
    matched = cms.InputTag("ak2GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akVsSoftDropZ05B152PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B152GenJets"),
    matched = cms.InputTag("ak2GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akVsSoftDropZ05B152PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B152PFJets")
                                                        )

akVsSoftDropZ05B152PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropZ05B152PFJets"),
    payload = "AK2PF_offline"
    )

akVsSoftDropZ05B152PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropZ05B152CaloJets'))

#akVsSoftDropZ05B152PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak2GenJets'))

akVsSoftDropZ05B152PFbTagger = bTaggers("akVsSoftDropZ05B152PF",0.2)

#create objects locally since they dont load properly otherwise
#akVsSoftDropZ05B152PFmatch = akVsSoftDropZ05B152PFbTagger.match
akVsSoftDropZ05B152PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B152PFJets"), matched = cms.InputTag("genParticles"))
akVsSoftDropZ05B152PFPatJetFlavourAssociationLegacy = akVsSoftDropZ05B152PFbTagger.PatJetFlavourAssociationLegacy
akVsSoftDropZ05B152PFPatJetPartons = akVsSoftDropZ05B152PFbTagger.PatJetPartons
akVsSoftDropZ05B152PFJetTracksAssociatorAtVertex = akVsSoftDropZ05B152PFbTagger.JetTracksAssociatorAtVertex
akVsSoftDropZ05B152PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropZ05B152PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B152PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B152PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B152PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B152PFCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B152PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B152PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B152PFbTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B152PFJetBProbabilityBJetTags = akVsSoftDropZ05B152PFbTagger.JetBProbabilityBJetTags
akVsSoftDropZ05B152PFSoftPFMuonByPtBJetTags = akVsSoftDropZ05B152PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B152PFSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B152PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B152PFTrackCountingHighEffBJetTags = akVsSoftDropZ05B152PFbTagger.TrackCountingHighEffBJetTags
akVsSoftDropZ05B152PFTrackCountingHighPurBJetTags = akVsSoftDropZ05B152PFbTagger.TrackCountingHighPurBJetTags
akVsSoftDropZ05B152PFPatJetPartonAssociationLegacy = akVsSoftDropZ05B152PFbTagger.PatJetPartonAssociationLegacy

akVsSoftDropZ05B152PFImpactParameterTagInfos = akVsSoftDropZ05B152PFbTagger.ImpactParameterTagInfos
akVsSoftDropZ05B152PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B152PFJetProbabilityBJetTags = akVsSoftDropZ05B152PFbTagger.JetProbabilityBJetTags

akVsSoftDropZ05B152PFSecondaryVertexTagInfos = akVsSoftDropZ05B152PFbTagger.SecondaryVertexTagInfos
akVsSoftDropZ05B152PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B152PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B152PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B152PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B152PFCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B152PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B152PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B152PFbTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B152PFSecondaryVertexNegativeTagInfos = akVsSoftDropZ05B152PFbTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropZ05B152PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B152PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B152PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B152PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B152PFNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B152PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B152PFPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B152PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B152PFNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B152PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B152PFPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B152PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B152PFSoftPFMuonsTagInfos = akVsSoftDropZ05B152PFbTagger.SoftPFMuonsTagInfos
akVsSoftDropZ05B152PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B152PFSoftPFMuonBJetTags = akVsSoftDropZ05B152PFbTagger.SoftPFMuonBJetTags
akVsSoftDropZ05B152PFSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B152PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B152PFSoftPFMuonByPtBJetTags = akVsSoftDropZ05B152PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B152PFNegativeSoftPFMuonByPtBJetTags = akVsSoftDropZ05B152PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropZ05B152PFPositiveSoftPFMuonByPtBJetTags = akVsSoftDropZ05B152PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropZ05B152PFPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropZ05B152PFPatJetPartonAssociationLegacy*akVsSoftDropZ05B152PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropZ05B152PFPatJetFlavourAssociation = akVsSoftDropZ05B152PFbTagger.PatJetFlavourAssociation
#akVsSoftDropZ05B152PFPatJetFlavourId = cms.Sequence(akVsSoftDropZ05B152PFPatJetPartons*akVsSoftDropZ05B152PFPatJetFlavourAssociation)

akVsSoftDropZ05B152PFJetBtaggingIP       = cms.Sequence(akVsSoftDropZ05B152PFImpactParameterTagInfos *
            (akVsSoftDropZ05B152PFTrackCountingHighEffBJetTags +
             akVsSoftDropZ05B152PFTrackCountingHighPurBJetTags +
             akVsSoftDropZ05B152PFJetProbabilityBJetTags +
             akVsSoftDropZ05B152PFJetBProbabilityBJetTags 
            )
            )

akVsSoftDropZ05B152PFJetBtaggingSV = cms.Sequence(akVsSoftDropZ05B152PFImpactParameterTagInfos
            *
            akVsSoftDropZ05B152PFSecondaryVertexTagInfos
            * (akVsSoftDropZ05B152PFSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B152PFSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B152PFCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B152PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B152PFJetBtaggingNegSV = cms.Sequence(akVsSoftDropZ05B152PFImpactParameterTagInfos
            *
            akVsSoftDropZ05B152PFSecondaryVertexNegativeTagInfos
            * (akVsSoftDropZ05B152PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B152PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B152PFNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B152PFPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B152PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropZ05B152PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B152PFJetBtaggingMu = cms.Sequence(akVsSoftDropZ05B152PFSoftPFMuonsTagInfos * (akVsSoftDropZ05B152PFSoftPFMuonBJetTags
                +
                akVsSoftDropZ05B152PFSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropZ05B152PFSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B152PFNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B152PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropZ05B152PFJetBtagging = cms.Sequence(akVsSoftDropZ05B152PFJetBtaggingIP
            *akVsSoftDropZ05B152PFJetBtaggingSV
            *akVsSoftDropZ05B152PFJetBtaggingNegSV
#            *akVsSoftDropZ05B152PFJetBtaggingMu
            )

akVsSoftDropZ05B152PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropZ05B152PFJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropZ05B152PFmatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropZ05B152PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B152PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropZ05B152PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropZ05B152PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropZ05B152PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B152PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B152PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropZ05B152PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropZ05B152PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropZ05B152PFJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropZ05B152PFJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B152PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B152PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropZ05B152PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B152PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropZ05B152PFJetID"),
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

akVsSoftDropZ05B152PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropZ05B152PFJets"),
           	    R0  = cms.double( 0.2)
)
akVsSoftDropZ05B152PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B152PFNjettiness:tau1','akVsSoftDropZ05B152PFNjettiness:tau2','akVsSoftDropZ05B152PFNjettiness:tau3']

akVsSoftDropZ05B152PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropZ05B152PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak2GenJets',
                                                             rParam = 0.2,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropZ05B152PF"),
                                                             jetName = cms.untracked.string("akVsSoftDropZ05B152PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B152GenJets"),
                                                             doGenTaus = cms.untracked.bool(False),
                                                             genTau1 = cms.InputTag("akSoftDropZ05B152GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropZ05B152GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropZ05B152GenNjettiness","tau3"),
                                                             doGenSym = cms.untracked.bool(True),
                                                             genSym = cms.InputTag("akSoftDropZ05B152GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropZ05B152GenJets","droppedBranches")
                                                             )

akVsSoftDropZ05B152PFJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropZ05B152PFclean
                                                  #*
                                                  akVsSoftDropZ05B152PFmatch
                                                  #*
                                                  #akVsSoftDropZ05B152PFmatchGroomed
                                                  *
                                                  akVsSoftDropZ05B152PFparton
                                                  *
                                                  akVsSoftDropZ05B152PFcorr
                                                  *
                                                  #akVsSoftDropZ05B152PFJetID
                                                  #*
                                                  akVsSoftDropZ05B152PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropZ05B152PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropZ05B152PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropZ05B152PFJetBtagging
                                                  *
                                                  akVsSoftDropZ05B152PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropZ05B152PFpatJetsWithBtagging
                                                  *
                                                  akVsSoftDropZ05B152PFJetAnalyzer
                                                  )

akVsSoftDropZ05B152PFJetSequence_data = cms.Sequence(akVsSoftDropZ05B152PFcorr
                                                    *
                                                    #akVsSoftDropZ05B152PFJetID
                                                    #*
                                                    akVsSoftDropZ05B152PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropZ05B152PFJetBtagging
                                                    *
                                                    akVsSoftDropZ05B152PFNjettiness 
                                                    *
                                                    akVsSoftDropZ05B152PFpatJetsWithBtagging
                                                    *
                                                    akVsSoftDropZ05B152PFJetAnalyzer
                                                    )

akVsSoftDropZ05B152PFJetSequence_jec = cms.Sequence(akVsSoftDropZ05B152PFJetSequence_mc)
akVsSoftDropZ05B152PFJetSequence_mb = cms.Sequence(akVsSoftDropZ05B152PFJetSequence_mc)

akVsSoftDropZ05B152PFJetSequence = cms.Sequence(akVsSoftDropZ05B152PFJetSequence_jec)
akVsSoftDropZ05B152PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akVsSoftDropZ05B152PFJetAnalyzer.jetPtMin = cms.double(1)
akVsSoftDropZ05B152PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B152PFJets:sym']
akVsSoftDropZ05B152PFpatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropZ05B152PFJets:droppedBranches']
