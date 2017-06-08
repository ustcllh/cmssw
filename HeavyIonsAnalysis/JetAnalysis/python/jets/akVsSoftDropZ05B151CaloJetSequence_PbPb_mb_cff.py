

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropZ05B151Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropZ05B151CaloJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akVsSoftDropZ05B151CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B151HiSignalGenJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akVsSoftDropZ05B151Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B151CaloJets")
                                                        )

akVsSoftDropZ05B151Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropZ05B151CaloJets"),
    payload = "AK1Calo_offline"
    )

akVsSoftDropZ05B151CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropZ05B151CaloJets'))

#akVsSoftDropZ05B151Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak1HiCleanedGenJets'))

akVsSoftDropZ05B151CalobTagger = bTaggers("akVsSoftDropZ05B151Calo",0.1)

#create objects locally since they dont load properly otherwise
#akVsSoftDropZ05B151Calomatch = akVsSoftDropZ05B151CalobTagger.match
akVsSoftDropZ05B151Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B151CaloJets"), matched = cms.InputTag("selectedPartons"))
akVsSoftDropZ05B151CaloPatJetFlavourAssociationLegacy = akVsSoftDropZ05B151CalobTagger.PatJetFlavourAssociationLegacy
akVsSoftDropZ05B151CaloPatJetPartons = akVsSoftDropZ05B151CalobTagger.PatJetPartons
akVsSoftDropZ05B151CaloJetTracksAssociatorAtVertex = akVsSoftDropZ05B151CalobTagger.JetTracksAssociatorAtVertex
akVsSoftDropZ05B151CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropZ05B151CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B151CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B151CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B151CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B151CaloCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B151CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B151CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B151CalobTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B151CaloJetBProbabilityBJetTags = akVsSoftDropZ05B151CalobTagger.JetBProbabilityBJetTags
akVsSoftDropZ05B151CaloSoftPFMuonByPtBJetTags = akVsSoftDropZ05B151CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B151CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B151CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B151CaloTrackCountingHighEffBJetTags = akVsSoftDropZ05B151CalobTagger.TrackCountingHighEffBJetTags
akVsSoftDropZ05B151CaloTrackCountingHighPurBJetTags = akVsSoftDropZ05B151CalobTagger.TrackCountingHighPurBJetTags
akVsSoftDropZ05B151CaloPatJetPartonAssociationLegacy = akVsSoftDropZ05B151CalobTagger.PatJetPartonAssociationLegacy

akVsSoftDropZ05B151CaloImpactParameterTagInfos = akVsSoftDropZ05B151CalobTagger.ImpactParameterTagInfos
akVsSoftDropZ05B151CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B151CaloJetProbabilityBJetTags = akVsSoftDropZ05B151CalobTagger.JetProbabilityBJetTags

akVsSoftDropZ05B151CaloSecondaryVertexTagInfos = akVsSoftDropZ05B151CalobTagger.SecondaryVertexTagInfos
akVsSoftDropZ05B151CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B151CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B151CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B151CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B151CaloCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B151CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B151CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B151CalobTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B151CaloSecondaryVertexNegativeTagInfos = akVsSoftDropZ05B151CalobTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropZ05B151CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B151CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B151CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B151CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B151CaloNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B151CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B151CaloPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B151CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B151CaloNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B151CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B151CaloPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B151CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B151CaloSoftPFMuonsTagInfos = akVsSoftDropZ05B151CalobTagger.SoftPFMuonsTagInfos
akVsSoftDropZ05B151CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B151CaloSoftPFMuonBJetTags = akVsSoftDropZ05B151CalobTagger.SoftPFMuonBJetTags
akVsSoftDropZ05B151CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B151CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B151CaloSoftPFMuonByPtBJetTags = akVsSoftDropZ05B151CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B151CaloNegativeSoftPFMuonByPtBJetTags = akVsSoftDropZ05B151CalobTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropZ05B151CaloPositiveSoftPFMuonByPtBJetTags = akVsSoftDropZ05B151CalobTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropZ05B151CaloPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropZ05B151CaloPatJetPartonAssociationLegacy*akVsSoftDropZ05B151CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropZ05B151CaloPatJetFlavourAssociation = akVsSoftDropZ05B151CalobTagger.PatJetFlavourAssociation
#akVsSoftDropZ05B151CaloPatJetFlavourId = cms.Sequence(akVsSoftDropZ05B151CaloPatJetPartons*akVsSoftDropZ05B151CaloPatJetFlavourAssociation)

akVsSoftDropZ05B151CaloJetBtaggingIP       = cms.Sequence(akVsSoftDropZ05B151CaloImpactParameterTagInfos *
            (akVsSoftDropZ05B151CaloTrackCountingHighEffBJetTags +
             akVsSoftDropZ05B151CaloTrackCountingHighPurBJetTags +
             akVsSoftDropZ05B151CaloJetProbabilityBJetTags +
             akVsSoftDropZ05B151CaloJetBProbabilityBJetTags 
            )
            )

akVsSoftDropZ05B151CaloJetBtaggingSV = cms.Sequence(akVsSoftDropZ05B151CaloImpactParameterTagInfos
            *
            akVsSoftDropZ05B151CaloSecondaryVertexTagInfos
            * (akVsSoftDropZ05B151CaloSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B151CaloSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B151CaloCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B151CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B151CaloJetBtaggingNegSV = cms.Sequence(akVsSoftDropZ05B151CaloImpactParameterTagInfos
            *
            akVsSoftDropZ05B151CaloSecondaryVertexNegativeTagInfos
            * (akVsSoftDropZ05B151CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B151CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B151CaloNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B151CaloPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B151CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropZ05B151CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B151CaloJetBtaggingMu = cms.Sequence(akVsSoftDropZ05B151CaloSoftPFMuonsTagInfos * (akVsSoftDropZ05B151CaloSoftPFMuonBJetTags
                +
                akVsSoftDropZ05B151CaloSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropZ05B151CaloSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B151CaloNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B151CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropZ05B151CaloJetBtagging = cms.Sequence(akVsSoftDropZ05B151CaloJetBtaggingIP
            *akVsSoftDropZ05B151CaloJetBtaggingSV
            *akVsSoftDropZ05B151CaloJetBtaggingNegSV
#            *akVsSoftDropZ05B151CaloJetBtaggingMu
            )

akVsSoftDropZ05B151CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropZ05B151CaloJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropZ05B151Calomatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropZ05B151Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B151Calocorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropZ05B151CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropZ05B151CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropZ05B151CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B151CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B151CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropZ05B151CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropZ05B151CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropZ05B151CaloJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropZ05B151CaloJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B151CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B151CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropZ05B151CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B151CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropZ05B151CaloJetID"),
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

akVsSoftDropZ05B151CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropZ05B151CaloJets"),
           	    R0  = cms.double( 0.1)
)
akVsSoftDropZ05B151CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B151CaloNjettiness:tau1','akVsSoftDropZ05B151CaloNjettiness:tau2','akVsSoftDropZ05B151CaloNjettiness:tau3']

akVsSoftDropZ05B151CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropZ05B151CalopatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropZ05B151Calo"),
                                                             jetName = cms.untracked.string("akVsSoftDropZ05B151Calo"),
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

akVsSoftDropZ05B151CaloJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropZ05B151Caloclean
                                                  #*
                                                  akVsSoftDropZ05B151Calomatch
                                                  #*
                                                  #akVsSoftDropZ05B151CalomatchGroomed
                                                  *
                                                  akVsSoftDropZ05B151Caloparton
                                                  *
                                                  akVsSoftDropZ05B151Calocorr
                                                  *
                                                  #akVsSoftDropZ05B151CaloJetID
                                                  #*
                                                  akVsSoftDropZ05B151CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropZ05B151CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropZ05B151CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropZ05B151CaloJetBtagging
                                                  *
                                                  akVsSoftDropZ05B151CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropZ05B151CalopatJetsWithBtagging
                                                  *
                                                  akVsSoftDropZ05B151CaloJetAnalyzer
                                                  )

akVsSoftDropZ05B151CaloJetSequence_data = cms.Sequence(akVsSoftDropZ05B151Calocorr
                                                    *
                                                    #akVsSoftDropZ05B151CaloJetID
                                                    #*
                                                    akVsSoftDropZ05B151CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropZ05B151CaloJetBtagging
                                                    *
                                                    akVsSoftDropZ05B151CaloNjettiness 
                                                    *
                                                    akVsSoftDropZ05B151CalopatJetsWithBtagging
                                                    *
                                                    akVsSoftDropZ05B151CaloJetAnalyzer
                                                    )

akVsSoftDropZ05B151CaloJetSequence_jec = cms.Sequence(akVsSoftDropZ05B151CaloJetSequence_mc)
akVsSoftDropZ05B151CaloJetSequence_mb = cms.Sequence(akVsSoftDropZ05B151CaloJetSequence_mc)

akVsSoftDropZ05B151CaloJetSequence = cms.Sequence(akVsSoftDropZ05B151CaloJetSequence_mb)
akVsSoftDropZ05B151CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B151CaloJets:sym']
akVsSoftDropZ05B151CalopatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropZ05B151CaloJets:droppedBranches']
