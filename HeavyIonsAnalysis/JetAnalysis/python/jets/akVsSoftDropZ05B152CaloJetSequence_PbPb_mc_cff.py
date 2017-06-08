

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropZ05B152Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropZ05B152CaloJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akVsSoftDropZ05B152CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B152HiSignalGenJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akVsSoftDropZ05B152Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B152CaloJets")
                                                        )

akVsSoftDropZ05B152Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropZ05B152CaloJets"),
    payload = "AK2Calo_offline"
    )

akVsSoftDropZ05B152CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropZ05B152CaloJets'))

#akVsSoftDropZ05B152Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak2HiSignalGenJets'))

akVsSoftDropZ05B152CalobTagger = bTaggers("akVsSoftDropZ05B152Calo",0.2)

#create objects locally since they dont load properly otherwise
#akVsSoftDropZ05B152Calomatch = akVsSoftDropZ05B152CalobTagger.match
akVsSoftDropZ05B152Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B152CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropZ05B152CaloPatJetFlavourAssociationLegacy = akVsSoftDropZ05B152CalobTagger.PatJetFlavourAssociationLegacy
akVsSoftDropZ05B152CaloPatJetPartons = akVsSoftDropZ05B152CalobTagger.PatJetPartons
akVsSoftDropZ05B152CaloJetTracksAssociatorAtVertex = akVsSoftDropZ05B152CalobTagger.JetTracksAssociatorAtVertex
akVsSoftDropZ05B152CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropZ05B152CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B152CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B152CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B152CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B152CaloCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B152CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B152CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B152CalobTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B152CaloJetBProbabilityBJetTags = akVsSoftDropZ05B152CalobTagger.JetBProbabilityBJetTags
akVsSoftDropZ05B152CaloSoftPFMuonByPtBJetTags = akVsSoftDropZ05B152CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B152CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B152CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B152CaloTrackCountingHighEffBJetTags = akVsSoftDropZ05B152CalobTagger.TrackCountingHighEffBJetTags
akVsSoftDropZ05B152CaloTrackCountingHighPurBJetTags = akVsSoftDropZ05B152CalobTagger.TrackCountingHighPurBJetTags
akVsSoftDropZ05B152CaloPatJetPartonAssociationLegacy = akVsSoftDropZ05B152CalobTagger.PatJetPartonAssociationLegacy

akVsSoftDropZ05B152CaloImpactParameterTagInfos = akVsSoftDropZ05B152CalobTagger.ImpactParameterTagInfos
akVsSoftDropZ05B152CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B152CaloJetProbabilityBJetTags = akVsSoftDropZ05B152CalobTagger.JetProbabilityBJetTags

akVsSoftDropZ05B152CaloSecondaryVertexTagInfos = akVsSoftDropZ05B152CalobTagger.SecondaryVertexTagInfos
akVsSoftDropZ05B152CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B152CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B152CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B152CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B152CaloCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B152CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B152CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B152CalobTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B152CaloSecondaryVertexNegativeTagInfos = akVsSoftDropZ05B152CalobTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropZ05B152CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B152CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B152CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B152CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B152CaloNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B152CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B152CaloPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B152CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B152CaloNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B152CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B152CaloPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B152CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B152CaloSoftPFMuonsTagInfos = akVsSoftDropZ05B152CalobTagger.SoftPFMuonsTagInfos
akVsSoftDropZ05B152CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B152CaloSoftPFMuonBJetTags = akVsSoftDropZ05B152CalobTagger.SoftPFMuonBJetTags
akVsSoftDropZ05B152CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B152CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B152CaloSoftPFMuonByPtBJetTags = akVsSoftDropZ05B152CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B152CaloNegativeSoftPFMuonByPtBJetTags = akVsSoftDropZ05B152CalobTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropZ05B152CaloPositiveSoftPFMuonByPtBJetTags = akVsSoftDropZ05B152CalobTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropZ05B152CaloPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropZ05B152CaloPatJetPartonAssociationLegacy*akVsSoftDropZ05B152CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropZ05B152CaloPatJetFlavourAssociation = akVsSoftDropZ05B152CalobTagger.PatJetFlavourAssociation
#akVsSoftDropZ05B152CaloPatJetFlavourId = cms.Sequence(akVsSoftDropZ05B152CaloPatJetPartons*akVsSoftDropZ05B152CaloPatJetFlavourAssociation)

akVsSoftDropZ05B152CaloJetBtaggingIP       = cms.Sequence(akVsSoftDropZ05B152CaloImpactParameterTagInfos *
            (akVsSoftDropZ05B152CaloTrackCountingHighEffBJetTags +
             akVsSoftDropZ05B152CaloTrackCountingHighPurBJetTags +
             akVsSoftDropZ05B152CaloJetProbabilityBJetTags +
             akVsSoftDropZ05B152CaloJetBProbabilityBJetTags 
            )
            )

akVsSoftDropZ05B152CaloJetBtaggingSV = cms.Sequence(akVsSoftDropZ05B152CaloImpactParameterTagInfos
            *
            akVsSoftDropZ05B152CaloSecondaryVertexTagInfos
            * (akVsSoftDropZ05B152CaloSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B152CaloSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B152CaloCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B152CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B152CaloJetBtaggingNegSV = cms.Sequence(akVsSoftDropZ05B152CaloImpactParameterTagInfos
            *
            akVsSoftDropZ05B152CaloSecondaryVertexNegativeTagInfos
            * (akVsSoftDropZ05B152CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B152CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B152CaloNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B152CaloPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B152CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropZ05B152CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B152CaloJetBtaggingMu = cms.Sequence(akVsSoftDropZ05B152CaloSoftPFMuonsTagInfos * (akVsSoftDropZ05B152CaloSoftPFMuonBJetTags
                +
                akVsSoftDropZ05B152CaloSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropZ05B152CaloSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B152CaloNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B152CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropZ05B152CaloJetBtagging = cms.Sequence(akVsSoftDropZ05B152CaloJetBtaggingIP
            *akVsSoftDropZ05B152CaloJetBtaggingSV
            *akVsSoftDropZ05B152CaloJetBtaggingNegSV
#            *akVsSoftDropZ05B152CaloJetBtaggingMu
            )

akVsSoftDropZ05B152CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropZ05B152CaloJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropZ05B152Calomatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropZ05B152Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B152Calocorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropZ05B152CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropZ05B152CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropZ05B152CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B152CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B152CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropZ05B152CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropZ05B152CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropZ05B152CaloJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropZ05B152CaloJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B152CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B152CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropZ05B152CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B152CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropZ05B152CaloJetID"),
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

akVsSoftDropZ05B152CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropZ05B152CaloJets"),
           	    R0  = cms.double( 0.2)
)
akVsSoftDropZ05B152CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B152CaloNjettiness:tau1','akVsSoftDropZ05B152CaloNjettiness:tau2','akVsSoftDropZ05B152CaloNjettiness:tau3']

akVsSoftDropZ05B152CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropZ05B152CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak2HiSignalGenJets',
                                                             rParam = 0.2,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropZ05B152Calo"),
                                                             jetName = cms.untracked.string("akVsSoftDropZ05B152Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
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

akVsSoftDropZ05B152CaloJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropZ05B152Caloclean
                                                  #*
                                                  akVsSoftDropZ05B152Calomatch
                                                  #*
                                                  #akVsSoftDropZ05B152CalomatchGroomed
                                                  *
                                                  akVsSoftDropZ05B152Caloparton
                                                  *
                                                  akVsSoftDropZ05B152Calocorr
                                                  *
                                                  #akVsSoftDropZ05B152CaloJetID
                                                  #*
                                                  akVsSoftDropZ05B152CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropZ05B152CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropZ05B152CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropZ05B152CaloJetBtagging
                                                  *
                                                  akVsSoftDropZ05B152CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropZ05B152CalopatJetsWithBtagging
                                                  *
                                                  akVsSoftDropZ05B152CaloJetAnalyzer
                                                  )

akVsSoftDropZ05B152CaloJetSequence_data = cms.Sequence(akVsSoftDropZ05B152Calocorr
                                                    *
                                                    #akVsSoftDropZ05B152CaloJetID
                                                    #*
                                                    akVsSoftDropZ05B152CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropZ05B152CaloJetBtagging
                                                    *
                                                    akVsSoftDropZ05B152CaloNjettiness 
                                                    *
                                                    akVsSoftDropZ05B152CalopatJetsWithBtagging
                                                    *
                                                    akVsSoftDropZ05B152CaloJetAnalyzer
                                                    )

akVsSoftDropZ05B152CaloJetSequence_jec = cms.Sequence(akVsSoftDropZ05B152CaloJetSequence_mc)
akVsSoftDropZ05B152CaloJetSequence_mb = cms.Sequence(akVsSoftDropZ05B152CaloJetSequence_mc)

akVsSoftDropZ05B152CaloJetSequence = cms.Sequence(akVsSoftDropZ05B152CaloJetSequence_mc)
akVsSoftDropZ05B152CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B152CaloJets:sym']
akVsSoftDropZ05B152CalopatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropZ05B152CaloJets:droppedBranches']
