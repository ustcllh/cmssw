

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropZ05B155PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropZ05B155PFJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akVsSoftDropZ05B155PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B155HiSignalGenJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akVsSoftDropZ05B155PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B155PFJets")
                                                        )

akVsSoftDropZ05B155PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropZ05B155PFJets"),
    payload = "AK5PF_offline"
    )

akVsSoftDropZ05B155PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropZ05B155CaloJets'))

#akVsSoftDropZ05B155PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak5HiSignalGenJets'))

akVsSoftDropZ05B155PFbTagger = bTaggers("akVsSoftDropZ05B155PF",0.5)

#create objects locally since they dont load properly otherwise
#akVsSoftDropZ05B155PFmatch = akVsSoftDropZ05B155PFbTagger.match
akVsSoftDropZ05B155PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B155PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropZ05B155PFPatJetFlavourAssociationLegacy = akVsSoftDropZ05B155PFbTagger.PatJetFlavourAssociationLegacy
akVsSoftDropZ05B155PFPatJetPartons = akVsSoftDropZ05B155PFbTagger.PatJetPartons
akVsSoftDropZ05B155PFJetTracksAssociatorAtVertex = akVsSoftDropZ05B155PFbTagger.JetTracksAssociatorAtVertex
akVsSoftDropZ05B155PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B155PFCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B155PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B155PFbTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B155PFJetBProbabilityBJetTags = akVsSoftDropZ05B155PFbTagger.JetBProbabilityBJetTags
akVsSoftDropZ05B155PFSoftPFMuonByPtBJetTags = akVsSoftDropZ05B155PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B155PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B155PFTrackCountingHighEffBJetTags = akVsSoftDropZ05B155PFbTagger.TrackCountingHighEffBJetTags
akVsSoftDropZ05B155PFTrackCountingHighPurBJetTags = akVsSoftDropZ05B155PFbTagger.TrackCountingHighPurBJetTags
akVsSoftDropZ05B155PFPatJetPartonAssociationLegacy = akVsSoftDropZ05B155PFbTagger.PatJetPartonAssociationLegacy

akVsSoftDropZ05B155PFImpactParameterTagInfos = akVsSoftDropZ05B155PFbTagger.ImpactParameterTagInfos
akVsSoftDropZ05B155PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B155PFJetProbabilityBJetTags = akVsSoftDropZ05B155PFbTagger.JetProbabilityBJetTags

akVsSoftDropZ05B155PFSecondaryVertexTagInfos = akVsSoftDropZ05B155PFbTagger.SecondaryVertexTagInfos
akVsSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B155PFCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B155PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B155PFbTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B155PFSecondaryVertexNegativeTagInfos = akVsSoftDropZ05B155PFbTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B155PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B155PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B155PFNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B155PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B155PFPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B155PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B155PFNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B155PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B155PFPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B155PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B155PFSoftPFMuonsTagInfos = akVsSoftDropZ05B155PFbTagger.SoftPFMuonsTagInfos
akVsSoftDropZ05B155PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B155PFSoftPFMuonBJetTags = akVsSoftDropZ05B155PFbTagger.SoftPFMuonBJetTags
akVsSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B155PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B155PFSoftPFMuonByPtBJetTags = akVsSoftDropZ05B155PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B155PFNegativeSoftPFMuonByPtBJetTags = akVsSoftDropZ05B155PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropZ05B155PFPositiveSoftPFMuonByPtBJetTags = akVsSoftDropZ05B155PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropZ05B155PFPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropZ05B155PFPatJetPartonAssociationLegacy*akVsSoftDropZ05B155PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropZ05B155PFPatJetFlavourAssociation = akVsSoftDropZ05B155PFbTagger.PatJetFlavourAssociation
#akVsSoftDropZ05B155PFPatJetFlavourId = cms.Sequence(akVsSoftDropZ05B155PFPatJetPartons*akVsSoftDropZ05B155PFPatJetFlavourAssociation)

akVsSoftDropZ05B155PFJetBtaggingIP       = cms.Sequence(akVsSoftDropZ05B155PFImpactParameterTagInfos *
            (akVsSoftDropZ05B155PFTrackCountingHighEffBJetTags +
             akVsSoftDropZ05B155PFTrackCountingHighPurBJetTags +
             akVsSoftDropZ05B155PFJetProbabilityBJetTags +
             akVsSoftDropZ05B155PFJetBProbabilityBJetTags 
            )
            )

akVsSoftDropZ05B155PFJetBtaggingSV = cms.Sequence(akVsSoftDropZ05B155PFImpactParameterTagInfos
            *
            akVsSoftDropZ05B155PFSecondaryVertexTagInfos
            * (akVsSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B155PFCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B155PFJetBtaggingNegSV = cms.Sequence(akVsSoftDropZ05B155PFImpactParameterTagInfos
            *
            akVsSoftDropZ05B155PFSecondaryVertexNegativeTagInfos
            * (akVsSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B155PFNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B155PFPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B155PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropZ05B155PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B155PFJetBtaggingMu = cms.Sequence(akVsSoftDropZ05B155PFSoftPFMuonsTagInfos * (akVsSoftDropZ05B155PFSoftPFMuonBJetTags
                +
                akVsSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropZ05B155PFSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B155PFNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B155PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropZ05B155PFJetBtagging = cms.Sequence(akVsSoftDropZ05B155PFJetBtaggingIP
            *akVsSoftDropZ05B155PFJetBtaggingSV
            *akVsSoftDropZ05B155PFJetBtaggingNegSV
#            *akVsSoftDropZ05B155PFJetBtaggingMu
            )

akVsSoftDropZ05B155PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropZ05B155PFJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropZ05B155PFmatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropZ05B155PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B155PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropZ05B155PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropZ05B155PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropZ05B155PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropZ05B155PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropZ05B155PFJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropZ05B155PFJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B155PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropZ05B155PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B155PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropZ05B155PFJetID"),
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

akVsSoftDropZ05B155PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropZ05B155PFJets"),
           	    R0  = cms.double( 0.5)
)
akVsSoftDropZ05B155PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B155PFNjettiness:tau1','akVsSoftDropZ05B155PFNjettiness:tau2','akVsSoftDropZ05B155PFNjettiness:tau3']

akVsSoftDropZ05B155PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropZ05B155PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak5HiSignalGenJets',
                                                             rParam = 0.5,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropZ05B155PF"),
                                                             jetName = cms.untracked.string("akVsSoftDropZ05B155PF"),
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

akVsSoftDropZ05B155PFJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropZ05B155PFclean
                                                  #*
                                                  akVsSoftDropZ05B155PFmatch
                                                  #*
                                                  #akVsSoftDropZ05B155PFmatchGroomed
                                                  *
                                                  akVsSoftDropZ05B155PFparton
                                                  *
                                                  akVsSoftDropZ05B155PFcorr
                                                  *
                                                  #akVsSoftDropZ05B155PFJetID
                                                  #*
                                                  akVsSoftDropZ05B155PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropZ05B155PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropZ05B155PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropZ05B155PFJetBtagging
                                                  *
                                                  akVsSoftDropZ05B155PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropZ05B155PFpatJetsWithBtagging
                                                  *
                                                  akVsSoftDropZ05B155PFJetAnalyzer
                                                  )

akVsSoftDropZ05B155PFJetSequence_data = cms.Sequence(akVsSoftDropZ05B155PFcorr
                                                    *
                                                    #akVsSoftDropZ05B155PFJetID
                                                    #*
                                                    akVsSoftDropZ05B155PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropZ05B155PFJetBtagging
                                                    *
                                                    akVsSoftDropZ05B155PFNjettiness 
                                                    *
                                                    akVsSoftDropZ05B155PFpatJetsWithBtagging
                                                    *
                                                    akVsSoftDropZ05B155PFJetAnalyzer
                                                    )

akVsSoftDropZ05B155PFJetSequence_jec = cms.Sequence(akVsSoftDropZ05B155PFJetSequence_mc)
akVsSoftDropZ05B155PFJetSequence_mb = cms.Sequence(akVsSoftDropZ05B155PFJetSequence_mc)

akVsSoftDropZ05B155PFJetSequence = cms.Sequence(akVsSoftDropZ05B155PFJetSequence_data)
akVsSoftDropZ05B155PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B155PFJets:sym']
akVsSoftDropZ05B155PFpatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropZ05B155PFJets:droppedBranches']
