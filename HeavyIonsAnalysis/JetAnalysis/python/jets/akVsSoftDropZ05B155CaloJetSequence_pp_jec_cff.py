

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropZ05B155Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropZ05B155CaloJets"),
    matched = cms.InputTag("ak5GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akVsSoftDropZ05B155CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B155GenJets"),
    matched = cms.InputTag("ak5GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akVsSoftDropZ05B155Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B155CaloJets")
                                                        )

akVsSoftDropZ05B155Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropZ05B155CaloJets"),
    payload = "AK5Calo_offline"
    )

akVsSoftDropZ05B155CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropZ05B155CaloJets'))

#akVsSoftDropZ05B155Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak5GenJets'))

akVsSoftDropZ05B155CalobTagger = bTaggers("akVsSoftDropZ05B155Calo",0.5)

#create objects locally since they dont load properly otherwise
#akVsSoftDropZ05B155Calomatch = akVsSoftDropZ05B155CalobTagger.match
akVsSoftDropZ05B155Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropZ05B155CaloJets"), matched = cms.InputTag("genParticles"))
akVsSoftDropZ05B155CaloPatJetFlavourAssociationLegacy = akVsSoftDropZ05B155CalobTagger.PatJetFlavourAssociationLegacy
akVsSoftDropZ05B155CaloPatJetPartons = akVsSoftDropZ05B155CalobTagger.PatJetPartons
akVsSoftDropZ05B155CaloJetTracksAssociatorAtVertex = akVsSoftDropZ05B155CalobTagger.JetTracksAssociatorAtVertex
akVsSoftDropZ05B155CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropZ05B155CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B155CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B155CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B155CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B155CaloCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B155CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B155CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B155CalobTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B155CaloJetBProbabilityBJetTags = akVsSoftDropZ05B155CalobTagger.JetBProbabilityBJetTags
akVsSoftDropZ05B155CaloSoftPFMuonByPtBJetTags = akVsSoftDropZ05B155CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B155CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B155CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B155CaloTrackCountingHighEffBJetTags = akVsSoftDropZ05B155CalobTagger.TrackCountingHighEffBJetTags
akVsSoftDropZ05B155CaloTrackCountingHighPurBJetTags = akVsSoftDropZ05B155CalobTagger.TrackCountingHighPurBJetTags
akVsSoftDropZ05B155CaloPatJetPartonAssociationLegacy = akVsSoftDropZ05B155CalobTagger.PatJetPartonAssociationLegacy

akVsSoftDropZ05B155CaloImpactParameterTagInfos = akVsSoftDropZ05B155CalobTagger.ImpactParameterTagInfos
akVsSoftDropZ05B155CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B155CaloJetProbabilityBJetTags = akVsSoftDropZ05B155CalobTagger.JetProbabilityBJetTags

akVsSoftDropZ05B155CaloSecondaryVertexTagInfos = akVsSoftDropZ05B155CalobTagger.SecondaryVertexTagInfos
akVsSoftDropZ05B155CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B155CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B155CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B155CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B155CaloCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B155CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropZ05B155CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B155CalobTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B155CaloSecondaryVertexNegativeTagInfos = akVsSoftDropZ05B155CalobTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropZ05B155CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropZ05B155CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropZ05B155CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropZ05B155CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropZ05B155CaloNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B155CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B155CaloPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropZ05B155CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropZ05B155CaloNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B155CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropZ05B155CaloPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropZ05B155CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropZ05B155CaloSoftPFMuonsTagInfos = akVsSoftDropZ05B155CalobTagger.SoftPFMuonsTagInfos
akVsSoftDropZ05B155CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropZ05B155CaloSoftPFMuonBJetTags = akVsSoftDropZ05B155CalobTagger.SoftPFMuonBJetTags
akVsSoftDropZ05B155CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropZ05B155CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropZ05B155CaloSoftPFMuonByPtBJetTags = akVsSoftDropZ05B155CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropZ05B155CaloNegativeSoftPFMuonByPtBJetTags = akVsSoftDropZ05B155CalobTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropZ05B155CaloPositiveSoftPFMuonByPtBJetTags = akVsSoftDropZ05B155CalobTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropZ05B155CaloPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropZ05B155CaloPatJetPartonAssociationLegacy*akVsSoftDropZ05B155CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropZ05B155CaloPatJetFlavourAssociation = akVsSoftDropZ05B155CalobTagger.PatJetFlavourAssociation
#akVsSoftDropZ05B155CaloPatJetFlavourId = cms.Sequence(akVsSoftDropZ05B155CaloPatJetPartons*akVsSoftDropZ05B155CaloPatJetFlavourAssociation)

akVsSoftDropZ05B155CaloJetBtaggingIP       = cms.Sequence(akVsSoftDropZ05B155CaloImpactParameterTagInfos *
            (akVsSoftDropZ05B155CaloTrackCountingHighEffBJetTags +
             akVsSoftDropZ05B155CaloTrackCountingHighPurBJetTags +
             akVsSoftDropZ05B155CaloJetProbabilityBJetTags +
             akVsSoftDropZ05B155CaloJetBProbabilityBJetTags 
            )
            )

akVsSoftDropZ05B155CaloJetBtaggingSV = cms.Sequence(akVsSoftDropZ05B155CaloImpactParameterTagInfos
            *
            akVsSoftDropZ05B155CaloSecondaryVertexTagInfos
            * (akVsSoftDropZ05B155CaloSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B155CaloSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B155CaloCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B155CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B155CaloJetBtaggingNegSV = cms.Sequence(akVsSoftDropZ05B155CaloImpactParameterTagInfos
            *
            akVsSoftDropZ05B155CaloSecondaryVertexNegativeTagInfos
            * (akVsSoftDropZ05B155CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropZ05B155CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropZ05B155CaloNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B155CaloPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropZ05B155CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropZ05B155CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropZ05B155CaloJetBtaggingMu = cms.Sequence(akVsSoftDropZ05B155CaloSoftPFMuonsTagInfos * (akVsSoftDropZ05B155CaloSoftPFMuonBJetTags
                +
                akVsSoftDropZ05B155CaloSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropZ05B155CaloSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B155CaloNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropZ05B155CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropZ05B155CaloJetBtagging = cms.Sequence(akVsSoftDropZ05B155CaloJetBtaggingIP
            *akVsSoftDropZ05B155CaloJetBtaggingSV
            *akVsSoftDropZ05B155CaloJetBtaggingNegSV
#            *akVsSoftDropZ05B155CaloJetBtaggingMu
            )

akVsSoftDropZ05B155CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropZ05B155CaloJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropZ05B155Calomatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropZ05B155Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B155Calocorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropZ05B155CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropZ05B155CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropZ05B155CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropZ05B155CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B155CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropZ05B155CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropZ05B155CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropZ05B155CaloJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropZ05B155CaloJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B155CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropZ05B155CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropZ05B155CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropZ05B155CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropZ05B155CaloJetID"),
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

akVsSoftDropZ05B155CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropZ05B155CaloJets"),
           	    R0  = cms.double( 0.5)
)
akVsSoftDropZ05B155CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B155CaloNjettiness:tau1','akVsSoftDropZ05B155CaloNjettiness:tau2','akVsSoftDropZ05B155CaloNjettiness:tau3']

akVsSoftDropZ05B155CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropZ05B155CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak5GenJets',
                                                             rParam = 0.5,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropZ05B155Calo"),
                                                             jetName = cms.untracked.string("akVsSoftDropZ05B155Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
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

akVsSoftDropZ05B155CaloJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropZ05B155Caloclean
                                                  #*
                                                  akVsSoftDropZ05B155Calomatch
                                                  #*
                                                  #akVsSoftDropZ05B155CalomatchGroomed
                                                  *
                                                  akVsSoftDropZ05B155Caloparton
                                                  *
                                                  akVsSoftDropZ05B155Calocorr
                                                  *
                                                  #akVsSoftDropZ05B155CaloJetID
                                                  #*
                                                  akVsSoftDropZ05B155CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropZ05B155CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropZ05B155CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropZ05B155CaloJetBtagging
                                                  *
                                                  akVsSoftDropZ05B155CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropZ05B155CalopatJetsWithBtagging
                                                  *
                                                  akVsSoftDropZ05B155CaloJetAnalyzer
                                                  )

akVsSoftDropZ05B155CaloJetSequence_data = cms.Sequence(akVsSoftDropZ05B155Calocorr
                                                    *
                                                    #akVsSoftDropZ05B155CaloJetID
                                                    #*
                                                    akVsSoftDropZ05B155CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropZ05B155CaloJetBtagging
                                                    *
                                                    akVsSoftDropZ05B155CaloNjettiness 
                                                    *
                                                    akVsSoftDropZ05B155CalopatJetsWithBtagging
                                                    *
                                                    akVsSoftDropZ05B155CaloJetAnalyzer
                                                    )

akVsSoftDropZ05B155CaloJetSequence_jec = cms.Sequence(akVsSoftDropZ05B155CaloJetSequence_mc)
akVsSoftDropZ05B155CaloJetSequence_mb = cms.Sequence(akVsSoftDropZ05B155CaloJetSequence_mc)

akVsSoftDropZ05B155CaloJetSequence = cms.Sequence(akVsSoftDropZ05B155CaloJetSequence_jec)
akVsSoftDropZ05B155CaloJetAnalyzer.genPtMin = cms.untracked.double(1)
akVsSoftDropZ05B155CaloJetAnalyzer.jetPtMin = cms.double(1)
akVsSoftDropZ05B155CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropZ05B155CaloJets:sym']
akVsSoftDropZ05B155CalopatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropZ05B155CaloJets:droppedBranches']
