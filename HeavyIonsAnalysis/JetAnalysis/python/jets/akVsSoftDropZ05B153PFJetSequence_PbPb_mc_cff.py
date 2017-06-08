

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropZ05B153PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropZ05B153PFJets"),
    matched = cms.InputTag("ak3HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akVsSoftDropZ05B153PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B153HiSignalGenJets"),
    matched = cms.InputTag("ak3HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akVsSoftDropZ05B153PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B153PFJets")
                                                        )

akVsSoftDropZ05B153PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropZ05B153PFJets"),
    payload = "AK3PF_offline"
    )

akVsSoftDropZ05B153PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropZ05B153CaloJets'))

#akVsSoftDropZ05B153PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak3HiSignalGenJets'))

akVsSoftDropZ05B153PFbTagger = bTaggers("akVsSoftDropZ05B153PF",0.3)

#create objects locally since they dont load properly otherwise
#akVsSoftDropZ05B153PFmatch = akVsSoftDropZ05B153PFbTagger.match
akVsSoftDropZ05B153PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B153PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropZ05B153PFPatJetFlavourAssociationLegacy = akVsSoftDropZ05B153PFbTagger.PatJetFlavourAssociationLegacy
akVsSoftDropZ05B153PFPatJetPartons = akVsSoftDropZ05B153PFbTagger.PatJetPartons
akVsSoftDropZ05B153PFJetTracksAssociatorAtVertex = akVsSoftDropZ05B153PFbTagger.JetTracksAssociatorAtVertex
akVsSoftDropZ05B153PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropZ05B153PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B153PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B153PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B153PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B153PFCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B153PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B153PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B153PFbTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B153PFJetBProbabilityBJetTags = akVsSoftDropZ05B153PFbTagger.JetBProbabilityBJetTags
akVsSoftDropZ05B153PFSoftPFMuonByPtBJetTags = akVsSoftDropZ05B153PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B153PFSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B153PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B153PFTrackCountingHighEffBJetTags = akVsSoftDropZ05B153PFbTagger.TrackCountingHighEffBJetTags
akVsSoftDropZ05B153PFTrackCountingHighPurBJetTags = akVsSoftDropZ05B153PFbTagger.TrackCountingHighPurBJetTags
akVsSoftDropZ05B153PFPatJetPartonAssociationLegacy = akVsSoftDropZ05B153PFbTagger.PatJetPartonAssociationLegacy

akVsSoftDropZ05B153PFImpactParameterTagInfos = akVsSoftDropZ05B153PFbTagger.ImpactParameterTagInfos
akVsSoftDropZ05B153PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B153PFJetProbabilityBJetTags = akVsSoftDropZ05B153PFbTagger.JetProbabilityBJetTags

akVsSoftDropZ05B153PFSecondaryVertexTagInfos = akVsSoftDropZ05B153PFbTagger.SecondaryVertexTagInfos
akVsSoftDropZ05B153PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B153PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B153PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B153PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B153PFCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B153PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B153PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B153PFbTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B153PFSecondaryVertexNegativeTagInfos = akVsSoftDropZ05B153PFbTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropZ05B153PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B153PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B153PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B153PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B153PFNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B153PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B153PFPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B153PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B153PFNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B153PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B153PFPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B153PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B153PFSoftPFMuonsTagInfos = akVsSoftDropZ05B153PFbTagger.SoftPFMuonsTagInfos
akVsSoftDropZ05B153PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B153PFSoftPFMuonBJetTags = akVsSoftDropZ05B153PFbTagger.SoftPFMuonBJetTags
akVsSoftDropZ05B153PFSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B153PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B153PFSoftPFMuonByPtBJetTags = akVsSoftDropZ05B153PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B153PFNegativeSoftPFMuonByPtBJetTags = akVsSoftDropZ05B153PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropZ05B153PFPositiveSoftPFMuonByPtBJetTags = akVsSoftDropZ05B153PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropZ05B153PFPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropZ05B153PFPatJetPartonAssociationLegacy*akVsSoftDropZ05B153PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropZ05B153PFPatJetFlavourAssociation = akVsSoftDropZ05B153PFbTagger.PatJetFlavourAssociation
#akVsSoftDropZ05B153PFPatJetFlavourId = cms.Sequence(akVsSoftDropZ05B153PFPatJetPartons*akVsSoftDropZ05B153PFPatJetFlavourAssociation)

akVsSoftDropZ05B153PFJetBtaggingIP       = cms.Sequence(akVsSoftDropZ05B153PFImpactParameterTagInfos *
            (akVsSoftDropZ05B153PFTrackCountingHighEffBJetTags +
             akVsSoftDropZ05B153PFTrackCountingHighPurBJetTags +
             akVsSoftDropZ05B153PFJetProbabilityBJetTags +
             akVsSoftDropZ05B153PFJetBProbabilityBJetTags 
            )
            )

akVsSoftDropZ05B153PFJetBtaggingSV = cms.Sequence(akVsSoftDropZ05B153PFImpactParameterTagInfos
            *
            akVsSoftDropZ05B153PFSecondaryVertexTagInfos
            * (akVsSoftDropZ05B153PFSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B153PFSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B153PFCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B153PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B153PFJetBtaggingNegSV = cms.Sequence(akVsSoftDropZ05B153PFImpactParameterTagInfos
            *
            akVsSoftDropZ05B153PFSecondaryVertexNegativeTagInfos
            * (akVsSoftDropZ05B153PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B153PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B153PFNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B153PFPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B153PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropZ05B153PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B153PFJetBtaggingMu = cms.Sequence(akVsSoftDropZ05B153PFSoftPFMuonsTagInfos * (akVsSoftDropZ05B153PFSoftPFMuonBJetTags
                +
                akVsSoftDropZ05B153PFSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropZ05B153PFSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B153PFNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B153PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropZ05B153PFJetBtagging = cms.Sequence(akVsSoftDropZ05B153PFJetBtaggingIP
            *akVsSoftDropZ05B153PFJetBtaggingSV
            *akVsSoftDropZ05B153PFJetBtaggingNegSV
#            *akVsSoftDropZ05B153PFJetBtaggingMu
            )

akVsSoftDropZ05B153PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropZ05B153PFJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropZ05B153PFmatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropZ05B153PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B153PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropZ05B153PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropZ05B153PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropZ05B153PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B153PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B153PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropZ05B153PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropZ05B153PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropZ05B153PFJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropZ05B153PFJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B153PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B153PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropZ05B153PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B153PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropZ05B153PFJetID"),
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

akVsSoftDropZ05B153PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropZ05B153PFJets"),
           	    R0  = cms.double( 0.3)
)
akVsSoftDropZ05B153PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B153PFNjettiness:tau1','akVsSoftDropZ05B153PFNjettiness:tau2','akVsSoftDropZ05B153PFNjettiness:tau3']

akVsSoftDropZ05B153PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropZ05B153PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak3HiSignalGenJets',
                                                             rParam = 0.3,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropZ05B153PF"),
                                                             jetName = cms.untracked.string("akVsSoftDropZ05B153PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
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

akVsSoftDropZ05B153PFJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropZ05B153PFclean
                                                  #*
                                                  akVsSoftDropZ05B153PFmatch
                                                  #*
                                                  #akVsSoftDropZ05B153PFmatchGroomed
                                                  *
                                                  akVsSoftDropZ05B153PFparton
                                                  *
                                                  akVsSoftDropZ05B153PFcorr
                                                  *
                                                  #akVsSoftDropZ05B153PFJetID
                                                  #*
                                                  akVsSoftDropZ05B153PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropZ05B153PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropZ05B153PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropZ05B153PFJetBtagging
                                                  *
                                                  akVsSoftDropZ05B153PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropZ05B153PFpatJetsWithBtagging
                                                  *
                                                  akVsSoftDropZ05B153PFJetAnalyzer
                                                  )

akVsSoftDropZ05B153PFJetSequence_data = cms.Sequence(akVsSoftDropZ05B153PFcorr
                                                    *
                                                    #akVsSoftDropZ05B153PFJetID
                                                    #*
                                                    akVsSoftDropZ05B153PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropZ05B153PFJetBtagging
                                                    *
                                                    akVsSoftDropZ05B153PFNjettiness 
                                                    *
                                                    akVsSoftDropZ05B153PFpatJetsWithBtagging
                                                    *
                                                    akVsSoftDropZ05B153PFJetAnalyzer
                                                    )

akVsSoftDropZ05B153PFJetSequence_jec = cms.Sequence(akVsSoftDropZ05B153PFJetSequence_mc)
akVsSoftDropZ05B153PFJetSequence_mb = cms.Sequence(akVsSoftDropZ05B153PFJetSequence_mc)

akVsSoftDropZ05B153PFJetSequence = cms.Sequence(akVsSoftDropZ05B153PFJetSequence_mc)
akVsSoftDropZ05B153PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B153PFJets:sym']
akVsSoftDropZ05B153PFpatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropZ05B153PFJets:droppedBranches']
