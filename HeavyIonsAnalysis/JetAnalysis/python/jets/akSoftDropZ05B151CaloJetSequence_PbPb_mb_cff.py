

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropZ05B151Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B151CaloJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akSoftDropZ05B151CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B151HiGenJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akSoftDropZ05B151Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropZ05B151CaloJets")
                                                        )

akSoftDropZ05B151Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropZ05B151CaloJets"),
    payload = "AK1Calo_offline"
    )

akSoftDropZ05B151CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropZ05B151CaloJets'))

#akSoftDropZ05B151Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak1HiCleanedGenJets'))

akSoftDropZ05B151CalobTagger = bTaggers("akSoftDropZ05B151Calo",0.1)

#create objects locally since they dont load properly otherwise
#akSoftDropZ05B151Calomatch = akSoftDropZ05B151CalobTagger.match
akSoftDropZ05B151Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropZ05B151CaloJets"), matched = cms.InputTag("selectedPartons"))
akSoftDropZ05B151CaloPatJetFlavourAssociationLegacy = akSoftDropZ05B151CalobTagger.PatJetFlavourAssociationLegacy
akSoftDropZ05B151CaloPatJetPartons = akSoftDropZ05B151CalobTagger.PatJetPartons
akSoftDropZ05B151CaloJetTracksAssociatorAtVertex = akSoftDropZ05B151CalobTagger.JetTracksAssociatorAtVertex
akSoftDropZ05B151CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropZ05B151CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B151CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B151CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B151CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B151CaloCombinedSecondaryVertexBJetTags = akSoftDropZ05B151CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B151CaloCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B151CalobTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropZ05B151CaloJetBProbabilityBJetTags = akSoftDropZ05B151CalobTagger.JetBProbabilityBJetTags
akSoftDropZ05B151CaloSoftPFMuonByPtBJetTags = akSoftDropZ05B151CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B151CaloSoftPFMuonByIP3dBJetTags = akSoftDropZ05B151CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B151CaloTrackCountingHighEffBJetTags = akSoftDropZ05B151CalobTagger.TrackCountingHighEffBJetTags
akSoftDropZ05B151CaloTrackCountingHighPurBJetTags = akSoftDropZ05B151CalobTagger.TrackCountingHighPurBJetTags
akSoftDropZ05B151CaloPatJetPartonAssociationLegacy = akSoftDropZ05B151CalobTagger.PatJetPartonAssociationLegacy

akSoftDropZ05B151CaloImpactParameterTagInfos = akSoftDropZ05B151CalobTagger.ImpactParameterTagInfos
akSoftDropZ05B151CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B151CaloJetProbabilityBJetTags = akSoftDropZ05B151CalobTagger.JetProbabilityBJetTags

akSoftDropZ05B151CaloSecondaryVertexTagInfos = akSoftDropZ05B151CalobTagger.SecondaryVertexTagInfos
akSoftDropZ05B151CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B151CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B151CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B151CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B151CaloCombinedSecondaryVertexBJetTags = akSoftDropZ05B151CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B151CaloCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B151CalobTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropZ05B151CaloSecondaryVertexNegativeTagInfos = akSoftDropZ05B151CalobTagger.SecondaryVertexNegativeTagInfos
akSoftDropZ05B151CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B151CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B151CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B151CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B151CaloNegativeCombinedSecondaryVertexBJetTags = akSoftDropZ05B151CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropZ05B151CaloPositiveCombinedSecondaryVertexBJetTags = akSoftDropZ05B151CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropZ05B151CaloNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B151CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropZ05B151CaloPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B151CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropZ05B151CaloSoftPFMuonsTagInfos = akSoftDropZ05B151CalobTagger.SoftPFMuonsTagInfos
akSoftDropZ05B151CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B151CaloSoftPFMuonBJetTags = akSoftDropZ05B151CalobTagger.SoftPFMuonBJetTags
akSoftDropZ05B151CaloSoftPFMuonByIP3dBJetTags = akSoftDropZ05B151CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B151CaloSoftPFMuonByPtBJetTags = akSoftDropZ05B151CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B151CaloNegativeSoftPFMuonByPtBJetTags = akSoftDropZ05B151CalobTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropZ05B151CaloPositiveSoftPFMuonByPtBJetTags = akSoftDropZ05B151CalobTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropZ05B151CaloPatJetFlavourIdLegacy = cms.Sequence(akSoftDropZ05B151CaloPatJetPartonAssociationLegacy*akSoftDropZ05B151CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropZ05B151CaloPatJetFlavourAssociation = akSoftDropZ05B151CalobTagger.PatJetFlavourAssociation
#akSoftDropZ05B151CaloPatJetFlavourId = cms.Sequence(akSoftDropZ05B151CaloPatJetPartons*akSoftDropZ05B151CaloPatJetFlavourAssociation)

akSoftDropZ05B151CaloJetBtaggingIP       = cms.Sequence(akSoftDropZ05B151CaloImpactParameterTagInfos *
            (akSoftDropZ05B151CaloTrackCountingHighEffBJetTags +
             akSoftDropZ05B151CaloTrackCountingHighPurBJetTags +
             akSoftDropZ05B151CaloJetProbabilityBJetTags +
             akSoftDropZ05B151CaloJetBProbabilityBJetTags 
            )
            )

akSoftDropZ05B151CaloJetBtaggingSV = cms.Sequence(akSoftDropZ05B151CaloImpactParameterTagInfos
            *
            akSoftDropZ05B151CaloSecondaryVertexTagInfos
            * (akSoftDropZ05B151CaloSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropZ05B151CaloSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropZ05B151CaloCombinedSecondaryVertexBJetTags+
                akSoftDropZ05B151CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropZ05B151CaloJetBtaggingNegSV = cms.Sequence(akSoftDropZ05B151CaloImpactParameterTagInfos
            *
            akSoftDropZ05B151CaloSecondaryVertexNegativeTagInfos
            * (akSoftDropZ05B151CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropZ05B151CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropZ05B151CaloNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropZ05B151CaloPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropZ05B151CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropZ05B151CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropZ05B151CaloJetBtaggingMu = cms.Sequence(akSoftDropZ05B151CaloSoftPFMuonsTagInfos * (akSoftDropZ05B151CaloSoftPFMuonBJetTags
                +
                akSoftDropZ05B151CaloSoftPFMuonByIP3dBJetTags
                +
                akSoftDropZ05B151CaloSoftPFMuonByPtBJetTags
                +
                akSoftDropZ05B151CaloNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropZ05B151CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropZ05B151CaloJetBtagging = cms.Sequence(akSoftDropZ05B151CaloJetBtaggingIP
            *akSoftDropZ05B151CaloJetBtaggingSV
            *akSoftDropZ05B151CaloJetBtaggingNegSV
#            *akSoftDropZ05B151CaloJetBtaggingMu
            )

akSoftDropZ05B151CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropZ05B151CaloJets"),
        genJetMatch          = cms.InputTag("akSoftDropZ05B151Calomatch"),
        genPartonMatch       = cms.InputTag("akSoftDropZ05B151Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropZ05B151Calocorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropZ05B151CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropZ05B151CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropZ05B151CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropZ05B151CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropZ05B151CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropZ05B151CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropZ05B151CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropZ05B151CaloJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropZ05B151CaloJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropZ05B151CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropZ05B151CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropZ05B151CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropZ05B151CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropZ05B151CaloJetID"),
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

akSoftDropZ05B151CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropZ05B151CaloJets"),
           	    R0  = cms.double( 0.1)
)
akSoftDropZ05B151CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropZ05B151CaloNjettiness:tau1','akSoftDropZ05B151CaloNjettiness:tau2','akSoftDropZ05B151CaloNjettiness:tau3']

akSoftDropZ05B151CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropZ05B151CalopatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akSoftDropZ05B151Calo"),
                                                             jetName = cms.untracked.string("akSoftDropZ05B151Calo"),
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

akSoftDropZ05B151CaloJetSequence_mc = cms.Sequence(
                                                  #akSoftDropZ05B151Caloclean
                                                  #*
                                                  akSoftDropZ05B151Calomatch
                                                  #*
                                                  #akSoftDropZ05B151CalomatchGroomed
                                                  *
                                                  akSoftDropZ05B151Caloparton
                                                  *
                                                  akSoftDropZ05B151Calocorr
                                                  *
                                                  #akSoftDropZ05B151CaloJetID
                                                  #*
                                                  akSoftDropZ05B151CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropZ05B151CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropZ05B151CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropZ05B151CaloJetBtagging
                                                  *
                                                  akSoftDropZ05B151CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropZ05B151CalopatJetsWithBtagging
                                                  *
                                                  akSoftDropZ05B151CaloJetAnalyzer
                                                  )

akSoftDropZ05B151CaloJetSequence_data = cms.Sequence(akSoftDropZ05B151Calocorr
                                                    *
                                                    #akSoftDropZ05B151CaloJetID
                                                    #*
                                                    akSoftDropZ05B151CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropZ05B151CaloJetBtagging
                                                    *
                                                    akSoftDropZ05B151CaloNjettiness 
                                                    *
                                                    akSoftDropZ05B151CalopatJetsWithBtagging
                                                    *
                                                    akSoftDropZ05B151CaloJetAnalyzer
                                                    )

akSoftDropZ05B151CaloJetSequence_jec = cms.Sequence(akSoftDropZ05B151CaloJetSequence_mc)
akSoftDropZ05B151CaloJetSequence_mb = cms.Sequence(akSoftDropZ05B151CaloJetSequence_mc)

akSoftDropZ05B151CaloJetSequence = cms.Sequence(akSoftDropZ05B151CaloJetSequence_mb)
akSoftDropZ05B151CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropZ05B151CaloJets:sym']
akSoftDropZ05B151CalopatJetsWithBtagging.userData.userInts.src += ['akSoftDropZ05B151CaloJets:droppedBranches']
