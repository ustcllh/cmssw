

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropZ05B151Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropZ05B151CaloJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPuSoftDropZ05B151CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B151HiGenJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPuSoftDropZ05B151Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropZ05B151CaloJets")
                                                        )

akPuSoftDropZ05B151Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropZ05B151CaloJets"),
    payload = "AKPu1Calo_offline"
    )

akPuSoftDropZ05B151CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropZ05B151CaloJets'))

#akPuSoftDropZ05B151Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak1HiCleanedGenJets'))

akPuSoftDropZ05B151CalobTagger = bTaggers("akPuSoftDropZ05B151Calo",0.1)

#create objects locally since they dont load properly otherwise
#akPuSoftDropZ05B151Calomatch = akPuSoftDropZ05B151CalobTagger.match
akPuSoftDropZ05B151Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropZ05B151CaloJets"), matched = cms.InputTag("selectedPartons"))
akPuSoftDropZ05B151CaloPatJetFlavourAssociationLegacy = akPuSoftDropZ05B151CalobTagger.PatJetFlavourAssociationLegacy
akPuSoftDropZ05B151CaloPatJetPartons = akPuSoftDropZ05B151CalobTagger.PatJetPartons
akPuSoftDropZ05B151CaloJetTracksAssociatorAtVertex = akPuSoftDropZ05B151CalobTagger.JetTracksAssociatorAtVertex
akPuSoftDropZ05B151CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropZ05B151CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B151CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B151CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B151CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B151CaloCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B151CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropZ05B151CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B151CalobTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropZ05B151CaloJetBProbabilityBJetTags = akPuSoftDropZ05B151CalobTagger.JetBProbabilityBJetTags
akPuSoftDropZ05B151CaloSoftPFMuonByPtBJetTags = akPuSoftDropZ05B151CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropZ05B151CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropZ05B151CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropZ05B151CaloTrackCountingHighEffBJetTags = akPuSoftDropZ05B151CalobTagger.TrackCountingHighEffBJetTags
akPuSoftDropZ05B151CaloTrackCountingHighPurBJetTags = akPuSoftDropZ05B151CalobTagger.TrackCountingHighPurBJetTags
akPuSoftDropZ05B151CaloPatJetPartonAssociationLegacy = akPuSoftDropZ05B151CalobTagger.PatJetPartonAssociationLegacy

akPuSoftDropZ05B151CaloImpactParameterTagInfos = akPuSoftDropZ05B151CalobTagger.ImpactParameterTagInfos
akPuSoftDropZ05B151CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropZ05B151CaloJetProbabilityBJetTags = akPuSoftDropZ05B151CalobTagger.JetProbabilityBJetTags

akPuSoftDropZ05B151CaloSecondaryVertexTagInfos = akPuSoftDropZ05B151CalobTagger.SecondaryVertexTagInfos
akPuSoftDropZ05B151CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B151CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B151CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B151CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B151CaloCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B151CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropZ05B151CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B151CalobTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropZ05B151CaloSecondaryVertexNegativeTagInfos = akPuSoftDropZ05B151CalobTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropZ05B151CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B151CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B151CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B151CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B151CaloNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B151CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropZ05B151CaloPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B151CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropZ05B151CaloNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B151CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropZ05B151CaloPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B151CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropZ05B151CaloSoftPFMuonsTagInfos = akPuSoftDropZ05B151CalobTagger.SoftPFMuonsTagInfos
akPuSoftDropZ05B151CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropZ05B151CaloSoftPFMuonBJetTags = akPuSoftDropZ05B151CalobTagger.SoftPFMuonBJetTags
akPuSoftDropZ05B151CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropZ05B151CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropZ05B151CaloSoftPFMuonByPtBJetTags = akPuSoftDropZ05B151CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropZ05B151CaloNegativeSoftPFMuonByPtBJetTags = akPuSoftDropZ05B151CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropZ05B151CaloPositiveSoftPFMuonByPtBJetTags = akPuSoftDropZ05B151CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropZ05B151CaloPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropZ05B151CaloPatJetPartonAssociationLegacy*akPuSoftDropZ05B151CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropZ05B151CaloPatJetFlavourAssociation = akPuSoftDropZ05B151CalobTagger.PatJetFlavourAssociation
#akPuSoftDropZ05B151CaloPatJetFlavourId = cms.Sequence(akPuSoftDropZ05B151CaloPatJetPartons*akPuSoftDropZ05B151CaloPatJetFlavourAssociation)

akPuSoftDropZ05B151CaloJetBtaggingIP       = cms.Sequence(akPuSoftDropZ05B151CaloImpactParameterTagInfos *
            (akPuSoftDropZ05B151CaloTrackCountingHighEffBJetTags +
             akPuSoftDropZ05B151CaloTrackCountingHighPurBJetTags +
             akPuSoftDropZ05B151CaloJetProbabilityBJetTags +
             akPuSoftDropZ05B151CaloJetBProbabilityBJetTags 
            )
            )

akPuSoftDropZ05B151CaloJetBtaggingSV = cms.Sequence(akPuSoftDropZ05B151CaloImpactParameterTagInfos
            *
            akPuSoftDropZ05B151CaloSecondaryVertexTagInfos
            * (akPuSoftDropZ05B151CaloSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropZ05B151CaloSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropZ05B151CaloCombinedSecondaryVertexBJetTags+
                akPuSoftDropZ05B151CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropZ05B151CaloJetBtaggingNegSV = cms.Sequence(akPuSoftDropZ05B151CaloImpactParameterTagInfos
            *
            akPuSoftDropZ05B151CaloSecondaryVertexNegativeTagInfos
            * (akPuSoftDropZ05B151CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropZ05B151CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropZ05B151CaloNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropZ05B151CaloPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropZ05B151CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropZ05B151CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropZ05B151CaloJetBtaggingMu = cms.Sequence(akPuSoftDropZ05B151CaloSoftPFMuonsTagInfos * (akPuSoftDropZ05B151CaloSoftPFMuonBJetTags
                +
                akPuSoftDropZ05B151CaloSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropZ05B151CaloSoftPFMuonByPtBJetTags
                +
                akPuSoftDropZ05B151CaloNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropZ05B151CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropZ05B151CaloJetBtagging = cms.Sequence(akPuSoftDropZ05B151CaloJetBtaggingIP
            *akPuSoftDropZ05B151CaloJetBtaggingSV
            *akPuSoftDropZ05B151CaloJetBtaggingNegSV
#            *akPuSoftDropZ05B151CaloJetBtaggingMu
            )

akPuSoftDropZ05B151CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropZ05B151CaloJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropZ05B151Calomatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropZ05B151Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropZ05B151Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropZ05B151CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropZ05B151CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropZ05B151CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropZ05B151CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropZ05B151CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropZ05B151CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropZ05B151CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropZ05B151CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropZ05B151CaloJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropZ05B151CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropZ05B151CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropZ05B151CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropZ05B151CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropZ05B151CaloJetID"),
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

akPuSoftDropZ05B151CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropZ05B151CaloJets"),
           	    R0  = cms.double( 0.1)
)
akPuSoftDropZ05B151CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropZ05B151CaloNjettiness:tau1','akPuSoftDropZ05B151CaloNjettiness:tau2','akPuSoftDropZ05B151CaloNjettiness:tau3']

akPuSoftDropZ05B151CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropZ05B151CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak1HiGenJets',
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
                                                             bTagJetName = cms.untracked.string("akPuSoftDropZ05B151Calo"),
                                                             jetName = cms.untracked.string("akPuSoftDropZ05B151Calo"),
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

akPuSoftDropZ05B151CaloJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropZ05B151Caloclean
                                                  #*
                                                  akPuSoftDropZ05B151Calomatch
                                                  #*
                                                  #akPuSoftDropZ05B151CalomatchGroomed
                                                  *
                                                  akPuSoftDropZ05B151Caloparton
                                                  *
                                                  akPuSoftDropZ05B151Calocorr
                                                  *
                                                  #akPuSoftDropZ05B151CaloJetID
                                                  #*
                                                  akPuSoftDropZ05B151CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropZ05B151CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropZ05B151CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropZ05B151CaloJetBtagging
                                                  *
                                                  akPuSoftDropZ05B151CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropZ05B151CalopatJetsWithBtagging
                                                  *
                                                  akPuSoftDropZ05B151CaloJetAnalyzer
                                                  )

akPuSoftDropZ05B151CaloJetSequence_data = cms.Sequence(akPuSoftDropZ05B151Calocorr
                                                    *
                                                    #akPuSoftDropZ05B151CaloJetID
                                                    #*
                                                    akPuSoftDropZ05B151CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropZ05B151CaloJetBtagging
                                                    *
                                                    akPuSoftDropZ05B151CaloNjettiness 
                                                    *
                                                    akPuSoftDropZ05B151CalopatJetsWithBtagging
                                                    *
                                                    akPuSoftDropZ05B151CaloJetAnalyzer
                                                    )

akPuSoftDropZ05B151CaloJetSequence_jec = cms.Sequence(akPuSoftDropZ05B151CaloJetSequence_mc)
akPuSoftDropZ05B151CaloJetSequence_mb = cms.Sequence(akPuSoftDropZ05B151CaloJetSequence_mc)

akPuSoftDropZ05B151CaloJetSequence = cms.Sequence(akPuSoftDropZ05B151CaloJetSequence_mb)
akPuSoftDropZ05B151CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropZ05B151CaloJets:sym']
akPuSoftDropZ05B151CalopatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropZ05B151CaloJets:droppedBranches']
