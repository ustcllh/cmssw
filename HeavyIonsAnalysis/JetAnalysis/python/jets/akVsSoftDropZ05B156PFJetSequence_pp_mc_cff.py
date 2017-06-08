

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropZ05B156PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropZ05B156PFJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akVsSoftDropZ05B156PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B156GenJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akVsSoftDropZ05B156PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B156PFJets")
                                                        )

akVsSoftDropZ05B156PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropZ05B156PFJets"),
    payload = "AK6PF_offline"
    )

akVsSoftDropZ05B156PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropZ05B156CaloJets'))

#akVsSoftDropZ05B156PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak6GenJets'))

akVsSoftDropZ05B156PFbTagger = bTaggers("akVsSoftDropZ05B156PF",0.6)

#create objects locally since they dont load properly otherwise
#akVsSoftDropZ05B156PFmatch = akVsSoftDropZ05B156PFbTagger.match
akVsSoftDropZ05B156PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B156PFJets"), matched = cms.InputTag("genParticles"))
akVsSoftDropZ05B156PFPatJetFlavourAssociationLegacy = akVsSoftDropZ05B156PFbTagger.PatJetFlavourAssociationLegacy
akVsSoftDropZ05B156PFPatJetPartons = akVsSoftDropZ05B156PFbTagger.PatJetPartons
akVsSoftDropZ05B156PFJetTracksAssociatorAtVertex = akVsSoftDropZ05B156PFbTagger.JetTracksAssociatorAtVertex
akVsSoftDropZ05B156PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B156PFCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B156PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B156PFbTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B156PFJetBProbabilityBJetTags = akVsSoftDropZ05B156PFbTagger.JetBProbabilityBJetTags
akVsSoftDropZ05B156PFSoftPFMuonByPtBJetTags = akVsSoftDropZ05B156PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B156PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B156PFTrackCountingHighEffBJetTags = akVsSoftDropZ05B156PFbTagger.TrackCountingHighEffBJetTags
akVsSoftDropZ05B156PFTrackCountingHighPurBJetTags = akVsSoftDropZ05B156PFbTagger.TrackCountingHighPurBJetTags
akVsSoftDropZ05B156PFPatJetPartonAssociationLegacy = akVsSoftDropZ05B156PFbTagger.PatJetPartonAssociationLegacy

akVsSoftDropZ05B156PFImpactParameterTagInfos = akVsSoftDropZ05B156PFbTagger.ImpactParameterTagInfos
akVsSoftDropZ05B156PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B156PFJetProbabilityBJetTags = akVsSoftDropZ05B156PFbTagger.JetProbabilityBJetTags

akVsSoftDropZ05B156PFSecondaryVertexTagInfos = akVsSoftDropZ05B156PFbTagger.SecondaryVertexTagInfos
akVsSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B156PFCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B156PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B156PFbTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B156PFSecondaryVertexNegativeTagInfos = akVsSoftDropZ05B156PFbTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B156PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B156PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B156PFNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B156PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B156PFPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B156PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B156PFNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B156PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B156PFPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B156PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B156PFSoftPFMuonsTagInfos = akVsSoftDropZ05B156PFbTagger.SoftPFMuonsTagInfos
akVsSoftDropZ05B156PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B156PFSoftPFMuonBJetTags = akVsSoftDropZ05B156PFbTagger.SoftPFMuonBJetTags
akVsSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B156PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B156PFSoftPFMuonByPtBJetTags = akVsSoftDropZ05B156PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B156PFNegativeSoftPFMuonByPtBJetTags = akVsSoftDropZ05B156PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropZ05B156PFPositiveSoftPFMuonByPtBJetTags = akVsSoftDropZ05B156PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropZ05B156PFPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropZ05B156PFPatJetPartonAssociationLegacy*akVsSoftDropZ05B156PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropZ05B156PFPatJetFlavourAssociation = akVsSoftDropZ05B156PFbTagger.PatJetFlavourAssociation
#akVsSoftDropZ05B156PFPatJetFlavourId = cms.Sequence(akVsSoftDropZ05B156PFPatJetPartons*akVsSoftDropZ05B156PFPatJetFlavourAssociation)

akVsSoftDropZ05B156PFJetBtaggingIP       = cms.Sequence(akVsSoftDropZ05B156PFImpactParameterTagInfos *
            (akVsSoftDropZ05B156PFTrackCountingHighEffBJetTags +
             akVsSoftDropZ05B156PFTrackCountingHighPurBJetTags +
             akVsSoftDropZ05B156PFJetProbabilityBJetTags +
             akVsSoftDropZ05B156PFJetBProbabilityBJetTags 
            )
            )

akVsSoftDropZ05B156PFJetBtaggingSV = cms.Sequence(akVsSoftDropZ05B156PFImpactParameterTagInfos
            *
            akVsSoftDropZ05B156PFSecondaryVertexTagInfos
            * (akVsSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B156PFCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B156PFJetBtaggingNegSV = cms.Sequence(akVsSoftDropZ05B156PFImpactParameterTagInfos
            *
            akVsSoftDropZ05B156PFSecondaryVertexNegativeTagInfos
            * (akVsSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B156PFNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B156PFPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B156PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropZ05B156PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B156PFJetBtaggingMu = cms.Sequence(akVsSoftDropZ05B156PFSoftPFMuonsTagInfos * (akVsSoftDropZ05B156PFSoftPFMuonBJetTags
                +
                akVsSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropZ05B156PFSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B156PFNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B156PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropZ05B156PFJetBtagging = cms.Sequence(akVsSoftDropZ05B156PFJetBtaggingIP
            *akVsSoftDropZ05B156PFJetBtaggingSV
            *akVsSoftDropZ05B156PFJetBtaggingNegSV
#            *akVsSoftDropZ05B156PFJetBtaggingMu
            )

akVsSoftDropZ05B156PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropZ05B156PFJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropZ05B156PFmatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropZ05B156PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B156PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropZ05B156PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropZ05B156PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropZ05B156PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropZ05B156PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropZ05B156PFJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropZ05B156PFJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B156PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropZ05B156PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B156PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropZ05B156PFJetID"),
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

akVsSoftDropZ05B156PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropZ05B156PFJets"),
           	    R0  = cms.double( 0.6)
)
akVsSoftDropZ05B156PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B156PFNjettiness:tau1','akVsSoftDropZ05B156PFNjettiness:tau2','akVsSoftDropZ05B156PFNjettiness:tau3']

akVsSoftDropZ05B156PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropZ05B156PFpatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropZ05B156PF"),
                                                             jetName = cms.untracked.string("akVsSoftDropZ05B156PF"),
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

akVsSoftDropZ05B156PFJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropZ05B156PFclean
                                                  #*
                                                  akVsSoftDropZ05B156PFmatch
                                                  #*
                                                  #akVsSoftDropZ05B156PFmatchGroomed
                                                  *
                                                  akVsSoftDropZ05B156PFparton
                                                  *
                                                  akVsSoftDropZ05B156PFcorr
                                                  *
                                                  #akVsSoftDropZ05B156PFJetID
                                                  #*
                                                  akVsSoftDropZ05B156PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropZ05B156PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropZ05B156PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropZ05B156PFJetBtagging
                                                  *
                                                  akVsSoftDropZ05B156PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropZ05B156PFpatJetsWithBtagging
                                                  *
                                                  akVsSoftDropZ05B156PFJetAnalyzer
                                                  )

akVsSoftDropZ05B156PFJetSequence_data = cms.Sequence(akVsSoftDropZ05B156PFcorr
                                                    *
                                                    #akVsSoftDropZ05B156PFJetID
                                                    #*
                                                    akVsSoftDropZ05B156PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropZ05B156PFJetBtagging
                                                    *
                                                    akVsSoftDropZ05B156PFNjettiness 
                                                    *
                                                    akVsSoftDropZ05B156PFpatJetsWithBtagging
                                                    *
                                                    akVsSoftDropZ05B156PFJetAnalyzer
                                                    )

akVsSoftDropZ05B156PFJetSequence_jec = cms.Sequence(akVsSoftDropZ05B156PFJetSequence_mc)
akVsSoftDropZ05B156PFJetSequence_mb = cms.Sequence(akVsSoftDropZ05B156PFJetSequence_mc)

akVsSoftDropZ05B156PFJetSequence = cms.Sequence(akVsSoftDropZ05B156PFJetSequence_mc)
akVsSoftDropZ05B156PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B156PFJets:sym']
akVsSoftDropZ05B156PFpatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropZ05B156PFJets:droppedBranches']
