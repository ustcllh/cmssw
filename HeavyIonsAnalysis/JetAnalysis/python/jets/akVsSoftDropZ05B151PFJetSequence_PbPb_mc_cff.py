

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropZ05B151PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropZ05B151PFJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akVsSoftDropZ05B151PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B151HiSignalGenJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akVsSoftDropZ05B151PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B151PFJets")
                                                        )

akVsSoftDropZ05B151PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropZ05B151PFJets"),
    payload = "AK1PF_offline"
    )

akVsSoftDropZ05B151PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropZ05B151CaloJets'))

#akVsSoftDropZ05B151PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak1HiSignalGenJets'))

akVsSoftDropZ05B151PFbTagger = bTaggers("akVsSoftDropZ05B151PF",0.1)

#create objects locally since they dont load properly otherwise
#akVsSoftDropZ05B151PFmatch = akVsSoftDropZ05B151PFbTagger.match
akVsSoftDropZ05B151PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B151PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropZ05B151PFPatJetFlavourAssociationLegacy = akVsSoftDropZ05B151PFbTagger.PatJetFlavourAssociationLegacy
akVsSoftDropZ05B151PFPatJetPartons = akVsSoftDropZ05B151PFbTagger.PatJetPartons
akVsSoftDropZ05B151PFJetTracksAssociatorAtVertex = akVsSoftDropZ05B151PFbTagger.JetTracksAssociatorAtVertex
akVsSoftDropZ05B151PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B151PFCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B151PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B151PFbTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B151PFJetBProbabilityBJetTags = akVsSoftDropZ05B151PFbTagger.JetBProbabilityBJetTags
akVsSoftDropZ05B151PFSoftPFMuonByPtBJetTags = akVsSoftDropZ05B151PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B151PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B151PFTrackCountingHighEffBJetTags = akVsSoftDropZ05B151PFbTagger.TrackCountingHighEffBJetTags
akVsSoftDropZ05B151PFTrackCountingHighPurBJetTags = akVsSoftDropZ05B151PFbTagger.TrackCountingHighPurBJetTags
akVsSoftDropZ05B151PFPatJetPartonAssociationLegacy = akVsSoftDropZ05B151PFbTagger.PatJetPartonAssociationLegacy

akVsSoftDropZ05B151PFImpactParameterTagInfos = akVsSoftDropZ05B151PFbTagger.ImpactParameterTagInfos
akVsSoftDropZ05B151PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B151PFJetProbabilityBJetTags = akVsSoftDropZ05B151PFbTagger.JetProbabilityBJetTags

akVsSoftDropZ05B151PFSecondaryVertexTagInfos = akVsSoftDropZ05B151PFbTagger.SecondaryVertexTagInfos
akVsSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B151PFCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B151PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B151PFbTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B151PFSecondaryVertexNegativeTagInfos = akVsSoftDropZ05B151PFbTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B151PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B151PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B151PFNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B151PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B151PFPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B151PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B151PFNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B151PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B151PFPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B151PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B151PFSoftPFMuonsTagInfos = akVsSoftDropZ05B151PFbTagger.SoftPFMuonsTagInfos
akVsSoftDropZ05B151PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B151PFSoftPFMuonBJetTags = akVsSoftDropZ05B151PFbTagger.SoftPFMuonBJetTags
akVsSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B151PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B151PFSoftPFMuonByPtBJetTags = akVsSoftDropZ05B151PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B151PFNegativeSoftPFMuonByPtBJetTags = akVsSoftDropZ05B151PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropZ05B151PFPositiveSoftPFMuonByPtBJetTags = akVsSoftDropZ05B151PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropZ05B151PFPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropZ05B151PFPatJetPartonAssociationLegacy*akVsSoftDropZ05B151PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropZ05B151PFPatJetFlavourAssociation = akVsSoftDropZ05B151PFbTagger.PatJetFlavourAssociation
#akVsSoftDropZ05B151PFPatJetFlavourId = cms.Sequence(akVsSoftDropZ05B151PFPatJetPartons*akVsSoftDropZ05B151PFPatJetFlavourAssociation)

akVsSoftDropZ05B151PFJetBtaggingIP       = cms.Sequence(akVsSoftDropZ05B151PFImpactParameterTagInfos *
            (akVsSoftDropZ05B151PFTrackCountingHighEffBJetTags +
             akVsSoftDropZ05B151PFTrackCountingHighPurBJetTags +
             akVsSoftDropZ05B151PFJetProbabilityBJetTags +
             akVsSoftDropZ05B151PFJetBProbabilityBJetTags 
            )
            )

akVsSoftDropZ05B151PFJetBtaggingSV = cms.Sequence(akVsSoftDropZ05B151PFImpactParameterTagInfos
            *
            akVsSoftDropZ05B151PFSecondaryVertexTagInfos
            * (akVsSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B151PFCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B151PFJetBtaggingNegSV = cms.Sequence(akVsSoftDropZ05B151PFImpactParameterTagInfos
            *
            akVsSoftDropZ05B151PFSecondaryVertexNegativeTagInfos
            * (akVsSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B151PFNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B151PFPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B151PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropZ05B151PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B151PFJetBtaggingMu = cms.Sequence(akVsSoftDropZ05B151PFSoftPFMuonsTagInfos * (akVsSoftDropZ05B151PFSoftPFMuonBJetTags
                +
                akVsSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropZ05B151PFSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B151PFNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B151PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropZ05B151PFJetBtagging = cms.Sequence(akVsSoftDropZ05B151PFJetBtaggingIP
            *akVsSoftDropZ05B151PFJetBtaggingSV
            *akVsSoftDropZ05B151PFJetBtaggingNegSV
#            *akVsSoftDropZ05B151PFJetBtaggingMu
            )

akVsSoftDropZ05B151PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropZ05B151PFJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropZ05B151PFmatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropZ05B151PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B151PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropZ05B151PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropZ05B151PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropZ05B151PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropZ05B151PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropZ05B151PFJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropZ05B151PFJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B151PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropZ05B151PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B151PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropZ05B151PFJetID"),
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

akVsSoftDropZ05B151PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropZ05B151PFJets"),
           	    R0  = cms.double( 0.1)
)
akVsSoftDropZ05B151PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B151PFNjettiness:tau1','akVsSoftDropZ05B151PFNjettiness:tau2','akVsSoftDropZ05B151PFNjettiness:tau3']

akVsSoftDropZ05B151PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropZ05B151PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak1HiSignalGenJets',
                                                             rParam = 0.1,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropZ05B151PF"),
                                                             jetName = cms.untracked.string("akVsSoftDropZ05B151PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B151GenJets"),
                                                             doGenTaus = cms.untracked.bool(False),
                                                             genTau1 = cms.InputTag("akSoftDropZ05B151GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropZ05B151GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropZ05B151GenNjettiness","tau3"),
                                                             doGenSym = cms.untracked.bool(True),
                                                             genSym = cms.InputTag("akSoftDropZ05B151GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropZ05B151GenJets","droppedBranches")
                                                             )

akVsSoftDropZ05B151PFJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropZ05B151PFclean
                                                  #*
                                                  akVsSoftDropZ05B151PFmatch
                                                  #*
                                                  #akVsSoftDropZ05B151PFmatchGroomed
                                                  *
                                                  akVsSoftDropZ05B151PFparton
                                                  *
                                                  akVsSoftDropZ05B151PFcorr
                                                  *
                                                  #akVsSoftDropZ05B151PFJetID
                                                  #*
                                                  akVsSoftDropZ05B151PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropZ05B151PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropZ05B151PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropZ05B151PFJetBtagging
                                                  *
                                                  akVsSoftDropZ05B151PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropZ05B151PFpatJetsWithBtagging
                                                  *
                                                  akVsSoftDropZ05B151PFJetAnalyzer
                                                  )

akVsSoftDropZ05B151PFJetSequence_data = cms.Sequence(akVsSoftDropZ05B151PFcorr
                                                    *
                                                    #akVsSoftDropZ05B151PFJetID
                                                    #*
                                                    akVsSoftDropZ05B151PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropZ05B151PFJetBtagging
                                                    *
                                                    akVsSoftDropZ05B151PFNjettiness 
                                                    *
                                                    akVsSoftDropZ05B151PFpatJetsWithBtagging
                                                    *
                                                    akVsSoftDropZ05B151PFJetAnalyzer
                                                    )

akVsSoftDropZ05B151PFJetSequence_jec = cms.Sequence(akVsSoftDropZ05B151PFJetSequence_mc)
akVsSoftDropZ05B151PFJetSequence_mb = cms.Sequence(akVsSoftDropZ05B151PFJetSequence_mc)

akVsSoftDropZ05B151PFJetSequence = cms.Sequence(akVsSoftDropZ05B151PFJetSequence_mc)
akVsSoftDropZ05B151PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B151PFJets:sym']
akVsSoftDropZ05B151PFpatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropZ05B151PFJets:droppedBranches']
