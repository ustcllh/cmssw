import FWCore.ParameterSet.Config as cms

# Pat 
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *



# Photons

makeHeavyIonPhotons.remove(interestingTrackEcalDetIds)
photonMatch.matched = cms.InputTag("hiGenParticles")

patPhotons.addPhotonID = cms.bool(False)
makeHeavyIonPhotons *= selectedPatPhotons


# Jets


patJets.jetSource  = cms.InputTag("iterativeConePu5CaloJets")
patJets.addBTagInfo         = False
patJets.addTagInfos         = False
patJets.addDiscriminators   = False
patJets.addAssociatedTracks = False
patJets.addJetCharge        = False
patJets.addJetID            = True
patJets.getJetMCFlavour     = False
patJets.addGenPartonMatch   = True
patJets.addGenJetMatch      = True
patJets.embedGenJetMatch    = True
patJets.embedGenPartonMatch = True
patJets.embedCaloTowers	    = False


patJetCorrFactors.useNPV = False
# full reco

#icPu5patJets = patJets.clone(
#  jetSource = cms.InputTag("iterativeConePu5CaloJets"),
#  genJetMatch = cms.InputTag("icPu5match"),
#  genPartonMatch = cms.InputTag("icPu5parton"),
#  jetCorrFactorsSource = cms.VInputTag(cms.InputTag("icPu5corr"))
#  )
icPu5corr    = patJetCorrFactors.clone(src      = cms.InputTag("iterativeConePu5CaloJets"),
                                       levels   = cms.vstring('L2Relative','L3Absolute'),
                                       payload  = cms.string('IC5Calo_2760GeV'))

akPu5PFcorr = icPu5corr.clone(
  src = cms.InputTag("akPu5PFJets")
  )
akPu5PFpatJets = patJets.clone(
  jetSource = cms.InputTag("akPu5PFJets"),
  genJetMatch = cms.InputTag("akPu5PFmatch"),
  genPartonMatch = cms.InputTag("akPu5PFparton"),
  jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5PFcorr"))
  )

akPu3PFcorr = icPu5corr.clone()
akPu3corr = icPu5corr.clone()

# mc matching
patJetPartonMatch.matched = cms.InputTag("hiPartons")

icPu5clean = heavyIonCleanedGenJets.clone( src = cms.InputTag('iterativeCone5HiGenJets') )
icPu5match = patJetGenJetMatch.clone(
  src = cms.InputTag("iterativeConePu5CaloJets"),
  matched = cms.InputTag("icPu5clean")
  )
icPu5parton = patJetPartonMatch.clone(
  src = cms.InputTag("iterativeConePu5CaloJets")
	)


akPu5PFclean = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak5HiGenJets') ) 
akPu5PFmatch = patJetGenJetMatch.clone(
  src = cms.InputTag("akPu5PFJets"),
  matched = cms.InputTag("akPu5PFclean")
  )
akPu5PFparton = patJetPartonMatch.clone(
  src = cms.InputTag("akPu5PFJets")
	)

akPu3PFclean = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak3HiGenJets') ) 
akPu3PFmatch = patJetGenJetMatch.clone(
  src = cms.InputTag("akPu3PFJets"),
  matched = cms.InputTag("akPu3PFclean")
  )
akPu3PFparton = patJetPartonMatch.clone(
  src = cms.InputTag("akPu3PFJets")
	)

akPu5match = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu5CaloJets"),
    matched = cms.InputTag("akPu5PFclean")
    )
akPu5parton = patJetPartonMatch.clone(
    src = cms.InputTag("akPu5CaloJets")
    )

akPu3match = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu3CaloJets"),
    matched = cms.InputTag("akPu3PFclean")
    )
akPu3parton = patJetPartonMatch.clone(
    src = cms.InputTag("akPu3CaloJets")
    )


### btagging moved to bTaggers_cff.py

# === data sequences ===
# Note still need to use enableData function in cfg to remove mc dep of patjet

# All corrections

#akPu1PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu1PFJets"),payload = cms.string('AK1PF_hiIterativeTracks'))
#akPu2PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu2PFJets"),payload = cms.string('AK2PF_hiIterativeTracks'))
#akPu3PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu3PFJets"),payload = cms.string('AK3PF_hiIterativeTracks'))
#akPu4PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu4PFJets"),payload = cms.string('AK4PF_hiIterativeTracks'))
#akPu5PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu5PFJets"),payload = cms.string('AK5PF_hiIterativeTracks'))
#akPu6PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu6PFJets"),payload = cms.string('AK6PF_hiIterativeTracks'))

#ak1PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak1PFJets"),payload = cms.string('AK1PF_hiIterativeTracks'))
#ak2PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak2PFJets"),payload = cms.string('AK2PF_hiIterativeTracks'))
#ak3PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak3PFJets"),payload = cms.string('AK3PF_hiIterativeTracks'))
#ak4PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak4PFJets"),payload = cms.string('AK4PF_hiIterativeTracks'))
#ak5PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak5PFJets"),payload = cms.string('AK5PF_hiIterativeTracks'))
#ak6PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak6PFJets"),payload = cms.string('AK6PF_hiIterativeTracks'))

akPu1PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu1PFJets"),payload = cms.string('AKPu1PF_generalTracks'))
akPu2PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu2PFJets"),payload = cms.string('AKPu2PF_generalTracks'))
akPu3PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu3PFJets"),payload = cms.string('AKPu3PF_generalTracks'))
akPu4PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu4PFJets"),payload = cms.string('AKPu4PF_generalTracks'))
akPu5PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu5PFJets"),payload = cms.string('AKPu5PF_generalTracks'))
akPu6PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu6PFJets"),payload = cms.string('AKPu6PF_generalTracks'))

ak1PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak1PFJets"),payload = cms.string('AK1PF_generalTracks'))
ak2PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak2PFJets"),payload = cms.string('AK2PF_generalTracks'))
ak3PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak3PFJets"),payload = cms.string('AK3PF_generalTracks'))
ak4PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak4PFJets"),payload = cms.string('AK4PF_generalTracks'))
ak5PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak5PFJets"),payload = cms.string('AK5PF_generalTracks'))
ak6PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak6PFJets"),payload = cms.string('AK6PF_generalTracks'))

akPu1Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akPu1CaloJets"),payload = cms.string('AKPu1Calo_HI'))
akPu2Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akPu2CaloJets"),payload = cms.string('AKPu2Calo_HI'))
akPu3Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akPu3CaloJets"),payload = cms.string('AKPu3Calo_HI'))
akPu4Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akPu4CaloJets"),payload = cms.string('AKPu4Calo_HI'))
akPu5Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akPu5CaloJets"),payload = cms.string('AKPu5Calo_HI'))
# We don't have corrections for ak6calo. This algorithm will be kept for debugging
akPu6Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akPu6CaloJets"),payload = cms.string('AKPu5Calo_HI'))

ak1Calocorr = akPu3PFcorr.clone(src = cms.InputTag("ak1CaloJets"),payload = cms.string('AK1Calo_HI'))
ak2Calocorr = akPu3PFcorr.clone(src = cms.InputTag("ak2CaloJets"),payload = cms.string('AK2Calo_HI'))
ak3Calocorr = akPu3PFcorr.clone(src = cms.InputTag("ak3CaloJets"),payload = cms.string('AK3Calo_HI'))
ak4Calocorr = akPu3PFcorr.clone(src = cms.InputTag("ak4CaloJets"),payload = cms.string('AK4Calo_HI'))
ak5Calocorr = akPu3PFcorr.clone(src = cms.InputTag("ak5CaloJets"),payload = cms.string('AK5Calo_HI'))
# We don't have corrections for ak6calo. This algorithm will be kept for debugging
ak6Calocorr = akPu3PFcorr.clone(src = cms.InputTag("ak6CaloJets"),payload = cms.string('AK5Calo_HI'))

#akVs3PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akVs3PFJets"),payload = cms.string('AKPu3PF_generalTracks'))
#akVs3Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akVs3CaloJets"),payload = cms.string('AKPu3Calo_HI'))
akVs3PFcorr = icPu5corr.clone(src = cms.InputTag("akVs3PFJets"))
akVs3Calocorr = icPu5corr.clone(src = cms.InputTag("akVs3CaloJets"))

# Gen stuff

ak1clean = akPu3PFclean.clone(src = cms.InputTag("ak1HiGenJets"))
ak2clean = akPu3PFclean.clone(src = cms.InputTag("ak2HiGenJets"))
ak3clean = akPu3PFclean.clone(src = cms.InputTag("ak3HiGenJets"))
ak4clean = akPu3PFclean.clone(src = cms.InputTag("ak4HiGenJets"))
ak5clean = akPu3PFclean.clone(src = cms.InputTag("ak5HiGenJets"))
ak6clean = akPu3PFclean.clone(src = cms.InputTag("ak6HiGenJets"))


akPu1PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akPu1PFJets"), matched = cms.InputTag("ak1clean"))
akPu2PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akPu2PFJets"), matched = cms.InputTag("ak2clean"))
akPu3PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akPu3PFJets"), matched = cms.InputTag("ak3clean"))
akPu4PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akPu4PFJets"), matched = cms.InputTag("ak4clean"))
akPu5PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akPu5PFJets"), matched = cms.InputTag("ak5clean"))
akPu6PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akPu6PFJets"), matched = cms.InputTag("ak6clean"))
akVs3PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akVs3PFJets"), matched = cms.InputTag("ak3clean"))
akPu1Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akPu1CaloJets"), matched = cms.InputTag("ak1clean"))
akPu2Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akPu2CaloJets"), matched = cms.InputTag("ak2clean"))
akPu3Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akPu3CaloJets"), matched = cms.InputTag("ak3clean"))
akPu4Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akPu4CaloJets"), matched = cms.InputTag("ak4clean"))
akPu5Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akPu5CaloJets"), matched = cms.InputTag("ak5clean"))
akPu6Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akPu6CaloJets"), matched = cms.InputTag("ak6clean"))
akVs3Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akVs3CaloJets"), matched = cms.InputTag("ak3clean"))
ak1PFmatch = akPu3PFmatch.clone(src = cms.InputTag("ak1PFJets"), matched = cms.InputTag("ak1clean"))
ak2PFmatch = akPu3PFmatch.clone(src = cms.InputTag("ak2PFJets"), matched = cms.InputTag("ak2clean"))
ak3PFmatch = akPu3PFmatch.clone(src = cms.InputTag("ak3PFJets"), matched = cms.InputTag("ak3clean"))
ak4PFmatch = akPu3PFmatch.clone(src = cms.InputTag("ak4PFJets"), matched = cms.InputTag("ak4clean"))
ak5PFmatch = akPu3PFmatch.clone(src = cms.InputTag("ak5PFJets"), matched = cms.InputTag("ak5clean"))
ak6PFmatch = akPu3PFmatch.clone(src = cms.InputTag("ak6PFJets"), matched = cms.InputTag("ak6clean"))
ak1Calomatch = akPu3PFmatch.clone(src = cms.InputTag("ak1CaloJets"), matched = cms.InputTag("ak1clean"))
ak2Calomatch = akPu3PFmatch.clone(src = cms.InputTag("ak2CaloJets"), matched = cms.InputTag("ak2clean"))
ak3Calomatch = akPu3PFmatch.clone(src = cms.InputTag("ak3CaloJets"), matched = cms.InputTag("ak3clean"))
ak4Calomatch = akPu3PFmatch.clone(src = cms.InputTag("ak4CaloJets"), matched = cms.InputTag("ak4clean"))
ak5Calomatch = akPu3PFmatch.clone(src = cms.InputTag("ak5CaloJets"), matched = cms.InputTag("ak5clean"))
ak6Calomatch = akPu3PFmatch.clone(src = cms.InputTag("ak6CaloJets"), matched = cms.InputTag("ak6clean"))
akPu1PFparton = akPu3PFparton.clone(src = cms.InputTag("akPu1PFJets"))
akPu2PFparton = akPu3PFparton.clone(src = cms.InputTag("akPu2PFJets"))
akPu3PFparton = akPu3PFparton.clone(src = cms.InputTag("akPu3PFJets"))
akVs3PFparton = akPu3PFparton.clone(src = cms.InputTag("akVs3PFJets"),matched = cms.InputTag("hiGenParticles"))
akPu4PFparton = akPu3PFparton.clone(src = cms.InputTag("akPu4PFJets"))
akPu5PFparton = akPu3PFparton.clone(src = cms.InputTag("akPu5PFJets"))
akPu6PFparton = akPu3PFparton.clone(src = cms.InputTag("akPu6PFJets"))
akPu1Caloparton = akPu3PFparton.clone(src = cms.InputTag("akPu1CaloJets"))
akPu2Caloparton = akPu3PFparton.clone(src = cms.InputTag("akPu2CaloJets"))
akPu3Caloparton = akPu3PFparton.clone(src = cms.InputTag("akPu3CaloJets"))
akPu4Caloparton = akPu3PFparton.clone(src = cms.InputTag("akPu4CaloJets"))
akPu5Caloparton = akPu3PFparton.clone(src = cms.InputTag("akPu5CaloJets"))
akPu6Caloparton = akPu3PFparton.clone(src = cms.InputTag("akPu6CaloJets"))
akVs3Caloparton = akPu3PFparton.clone(src = cms.InputTag("akVs3CaloJets"),matched = cms.InputTag("hiGenParticles"))
ak1PFparton = akPu3PFparton.clone(src = cms.InputTag("ak1PFJets"))
ak2PFparton = akPu3PFparton.clone(src = cms.InputTag("ak2PFJets"))
ak3PFparton = akPu3PFparton.clone(src = cms.InputTag("ak3PFJets"))
ak4PFparton = akPu3PFparton.clone(src = cms.InputTag("ak4PFJets"))
ak5PFparton = akPu3PFparton.clone(src = cms.InputTag("ak5PFJets"))
ak6PFparton = akPu3PFparton.clone(src = cms.InputTag("ak6PFJets"))
ak1Caloparton = akPu3PFparton.clone(src = cms.InputTag("ak1CaloJets"))
ak2Caloparton = akPu3PFparton.clone(src = cms.InputTag("ak2CaloJets"))
ak3Caloparton = akPu3PFparton.clone(src = cms.InputTag("ak3CaloJets"))
ak4Caloparton = akPu3PFparton.clone(src = cms.InputTag("ak4CaloJets"))
ak5Caloparton = akPu3PFparton.clone(src = cms.InputTag("ak5CaloJets"))
ak6Caloparton = akPu3PFparton.clone(src = cms.InputTag("ak6CaloJets"))


# PAT Maker

akPu1PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu1PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu1PFcorr")), genJetMatch = cms.InputTag("akPu1PFmatch"), genPartonMatch = cms.InputTag("akPu1PFparton"),jetIDMap = cms.InputTag("akPu1PFJetID"))
akPu2PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu2PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2PFcorr")), genJetMatch = cms.InputTag("akPu2PFmatch"), genPartonMatch = cms.InputTag("akPu2PFparton"),jetIDMap = cms.InputTag("akPu2PFJetID"))
akPu3PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu3PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr")), genJetMatch = cms.InputTag("akPu3PFmatch"), genPartonMatch = cms.InputTag("akPu3PFparton"),jetIDMap = cms.InputTag("akPu3PFJetID"))
akPu4PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu4PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4PFcorr")), genJetMatch = cms.InputTag("akPu4PFmatch"), genPartonMatch = cms.InputTag("akPu4PFparton"),jetIDMap = cms.InputTag("akPu4PFJetID"))
akPu5PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu5PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5PFcorr")), genJetMatch = cms.InputTag("akPu5PFmatch"), genPartonMatch = cms.InputTag("akPu5PFparton"),jetIDMap = cms.InputTag("akPu5PFJetID"))
akPu6PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu6PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu6PFcorr")), genJetMatch = cms.InputTag("akPu6PFmatch"), genPartonMatch = cms.InputTag("akPu6PFparton"),jetIDMap = cms.InputTag("akPu6PFJetID"))
akPu1CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu1CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu1Calocorr")), genJetMatch = cms.InputTag("akPu1Calomatch"), genPartonMatch = cms.InputTag("akPu1Caloparton"),jetIDMap = cms.InputTag("akPu1CaloJetID"))
akPu2CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu2CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2Calocorr")), genJetMatch = cms.InputTag("akPu2Calomatch"), genPartonMatch = cms.InputTag("akPu2Caloparton"),jetIDMap = cms.InputTag("akPu2CaloJetID"))
akPu3CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu3CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3Calocorr")), genJetMatch = cms.InputTag("akPu3Calomatch"), genPartonMatch = cms.InputTag("akPu3Caloparton"),jetIDMap = cms.InputTag("akPu3CaloJetID"))
akPu4CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu4CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4Calocorr")), genJetMatch = cms.InputTag("akPu4Calomatch"), genPartonMatch = cms.InputTag("akPu4Caloparton"),jetIDMap = cms.InputTag("akPu4CaloJetID"))
akPu5CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu5CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5Calocorr")), genJetMatch = cms.InputTag("akPu5Calomatch"), genPartonMatch = cms.InputTag("akPu5Caloparton"),jetIDMap = cms.InputTag("akPu5CaloJetID"))
akPu6CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu6CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu6Calocorr")), genJetMatch = cms.InputTag("akPu6Calomatch"), genPartonMatch = cms.InputTag("akPu6Caloparton"),jetIDMap = cms.InputTag("akPu6CaloJetID"))
ak1PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak1PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak1PFcorr")), genJetMatch = cms.InputTag("ak1PFmatch"), genPartonMatch = cms.InputTag("ak1PFparton"),jetIDMap = cms.InputTag("ak1PFJetID"))
ak2PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak2PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak2PFcorr")), genJetMatch = cms.InputTag("ak2PFmatch"), genPartonMatch = cms.InputTag("ak2PFparton"),jetIDMap = cms.InputTag("ak2PFJetID"))
ak3PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak3PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak3PFcorr")), genJetMatch = cms.InputTag("ak3PFmatch"), genPartonMatch = cms.InputTag("ak3PFparton"),jetIDMap = cms.InputTag("ak3PFJetID"))
ak4PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak4PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak4PFcorr")), genJetMatch = cms.InputTag("ak4PFmatch"), genPartonMatch = cms.InputTag("ak4PFparton"),jetIDMap = cms.InputTag("ak4PFJetID"))
ak5PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak5PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak5PFcorr")), genJetMatch = cms.InputTag("ak5PFmatch"), genPartonMatch = cms.InputTag("ak5PFparton"),jetIDMap = cms.InputTag("ak5PFJetID"))
ak6PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak6PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak6PFcorr")), genJetMatch = cms.InputTag("ak6PFmatch"), genPartonMatch = cms.InputTag("ak6PFparton"),jetIDMap = cms.InputTag("ak6PFJetID"))
ak1CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak1CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak1Calocorr")), genJetMatch = cms.InputTag("ak1Calomatch"), genPartonMatch = cms.InputTag("ak1Caloparton"),jetIDMap = cms.InputTag("ak1CaloJetID"))
ak2CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak2CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak2Calocorr")), genJetMatch = cms.InputTag("ak2Calomatch"), genPartonMatch = cms.InputTag("ak2Caloparton"),jetIDMap = cms.InputTag("ak2CaloJetID"))
ak3CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak3CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak3Calocorr")), genJetMatch = cms.InputTag("ak3Calomatch"), genPartonMatch = cms.InputTag("ak3Caloparton"),jetIDMap = cms.InputTag("ak3CaloJetID"))
ak4CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak4CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak4Calocorr")), genJetMatch = cms.InputTag("ak4Calomatch"), genPartonMatch = cms.InputTag("ak4Caloparton"),jetIDMap = cms.InputTag("ak4CaloJetID"))
ak5CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak5CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak5Calocorr")), genJetMatch = cms.InputTag("ak5Calomatch"), genPartonMatch = cms.InputTag("ak5Caloparton"),jetIDMap = cms.InputTag("ak5CaloJetID"))
ak6CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak6CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak6Calocorr")), genJetMatch = cms.InputTag("ak6Calomatch"), genPartonMatch = cms.InputTag("ak6Caloparton"),jetIDMap = cms.InputTag("ak6CaloJetID"))

akVs3PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akVs3PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs3PFcorr")), genJetMatch = cms.InputTag("akVs3PFmatch"), genPartonMatch = cms.InputTag("akVs3PFparton"),jetIDMap = cms.InputTag("akVs3PFJetID"))
akVs3CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akVs3CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs3Calocorr")), genJetMatch = cms.InputTag("akVs3Calomatch"), genPartonMatch = cms.InputTag("akVs3Caloparton"),jetIDMap = cms.InputTag("akVs3CaloJetID"))

icPu5patSequence = cms.Sequence(icPu5corr * icPu5clean * icPu5match * icPu5parton  *  icPu5patJets)

akPu1PFpatSequence = cms.Sequence(akPu1PFcorr+ak1clean+akPu1PFmatch+akPu1PFparton+akPu1PFpatJets)
akPu2PFpatSequence = cms.Sequence(akPu2PFcorr+ak2clean+akPu2PFmatch+akPu2PFparton+akPu2PFpatJets)
akPu3PFpatSequence = cms.Sequence(akPu3PFcorr+ak3clean+akPu3PFmatch+akPu3PFparton+akPu3PFpatJets)
akPu4PFpatSequence = cms.Sequence(akPu4PFcorr+ak4clean+akPu4PFmatch+akPu4PFparton+akPu4PFpatJets)
akPu5PFpatSequence = cms.Sequence(akPu5PFcorr+ak5clean+akPu5PFmatch+akPu5PFparton+akPu5PFpatJets)
akPu6PFpatSequence = cms.Sequence(akPu6PFcorr+ak6clean+akPu6PFmatch+akPu6PFparton+akPu6PFpatJets)
akVs3PFpatSequence = cms.Sequence(akVs3PFcorr+ak3clean+akVs3PFmatch+akVs3PFparton+akVs3PFpatJets)

akPu1CalopatSequence = cms.Sequence(akPu1Calocorr+ak1clean+akPu1Calomatch+akPu1Caloparton+akPu1CalopatJets)
akPu2CalopatSequence = cms.Sequence(akPu2Calocorr+ak2clean+akPu2Calomatch+akPu2Caloparton+akPu2CalopatJets)
akPu3CalopatSequence = cms.Sequence(akPu3Calocorr+ak3clean+akPu3Calomatch+akPu3Caloparton+akPu3CalopatJets)
akPu4CalopatSequence = cms.Sequence(akPu4Calocorr+ak4clean+akPu4Calomatch+akPu4Caloparton+akPu4CalopatJets)
akPu5CalopatSequence = cms.Sequence(akPu5Calocorr+ak5clean+akPu5Calomatch+akPu5Caloparton+akPu5CalopatJets)
akPu6CalopatSequence = cms.Sequence(akPu6Calocorr+ak6clean+akPu6Calomatch+akPu6Caloparton+akPu6CalopatJets)
akVs3CalopatSequence = cms.Sequence(akVs3Calocorr+ak3clean+akVs3Calomatch+akVs3Caloparton+akVs3CalopatJets)

ak1PFpatSequence = cms.Sequence(ak1PFcorr+ak1clean+ak1PFmatch+ak1PFparton+ak1PFpatJets)
ak2PFpatSequence = cms.Sequence(ak2PFcorr+ak2clean+ak2PFmatch+ak2PFparton+ak2PFpatJets)
ak3PFpatSequence = cms.Sequence(ak3PFcorr+ak3clean+ak3PFmatch+ak3PFparton+ak3PFpatJets)
ak4PFpatSequence = cms.Sequence(ak4PFcorr+ak4clean+ak4PFmatch+ak4PFparton+ak4PFpatJets)
ak5PFpatSequence = cms.Sequence(ak5PFcorr+ak5clean+ak5PFmatch+ak5PFparton+ak5PFpatJets)
ak6PFpatSequence = cms.Sequence(ak6PFcorr+ak6clean+ak6PFmatch+ak6PFparton+ak6PFpatJets)

ak1CalopatSequence = cms.Sequence(ak1Calocorr+ak1clean+ak1Calomatch+ak1Caloparton+ak1CalopatJets)
ak2CalopatSequence = cms.Sequence(ak2Calocorr+ak2clean+ak2Calomatch+ak2Caloparton+ak2CalopatJets)
ak3CalopatSequence = cms.Sequence(ak3Calocorr+ak3clean+ak3Calomatch+ak3Caloparton+ak3CalopatJets)
ak4CalopatSequence = cms.Sequence(ak4Calocorr+ak4clean+ak4Calomatch+ak4Caloparton+ak4CalopatJets)
ak5CalopatSequence = cms.Sequence(ak5Calocorr+ak5clean+ak5Calomatch+ak5Caloparton+ak5CalopatJets)
ak6CalopatSequence = cms.Sequence(ak6Calocorr+ak6clean+ak6Calomatch+ak6Caloparton+ak6CalopatJets)

akPu3PFpatSequence_withBtagging = cms.Sequence(akPu3PFcorr * akPu3PFclean * akPu3PFbTagger.match * akPu3PFbTagger.parton * akPu3PFbTagger.PatJetFlavourId * akPu3PFbTagger.JetTracksAssociator * akPu3PFbTagger.JetBtagging * akPu3PFpatJets)
akPu4PFpatSequence_withBtagging = cms.Sequence(akPu4PFcorr * akPu4PFclean * akPu4PFbTagger.match * akPu4PFbTagger.parton * akPu4PFbTagger.PatJetFlavourId * akPu4PFbTagger.JetTracksAssociator * akPu4PFbTagger.JetBtagging * akPu4PFpatJets)
akPu5PFpatSequence_withBtagging = cms.Sequence(akPu5PFcorr * akPu5PFclean * akPu5PFbTagger.match * akPu5PFbTagger.parton * akPu5PFbTagger.PatJetFlavourId * akPu5PFbTagger.JetTracksAssociator * akPu5PFbTagger.JetBtagging * akPu5PFpatJets)

makeHeavyIonJets = cms.Sequence(
                                akPu1PFpatSequence +
                                akPu2PFpatSequence +
                                akPu3PFpatSequence +
                                akPu4PFpatSequence +
                                akPu5PFpatSequence +
                                akPu6PFpatSequence +

                                akPu1CalopatSequence +
                                akPu2CalopatSequence +
                                akPu3CalopatSequence +
                                akPu4CalopatSequence +
                                akPu5CalopatSequence +
                                akPu6CalopatSequence +
                                
                                ak1PFpatSequence +
                                ak2PFpatSequence +
                                ak3PFpatSequence +
                                ak4PFpatSequence +
                                ak5PFpatSequence +
                                ak6PFpatSequence +
                                
                                ak1CalopatSequence +
                                ak2CalopatSequence +
                                ak3CalopatSequence +
                                ak4CalopatSequence +
                                ak5CalopatSequence +
                                ak6CalopatSequence
                                
                                )

makeHeavyIonJets2to5 = cms.Sequence(
                                akPu2PFpatSequence +
                                akPu3PFpatSequence +
                                akPu4PFpatSequence +
                                akPu5PFpatSequence +

                                akPu2CalopatSequence +
                                akPu3CalopatSequence +
                                akPu4CalopatSequence +
                                akPu5CalopatSequence +
                                
                                ak2PFpatSequence +
                                ak3PFpatSequence +
                                ak4PFpatSequence +
                                ak5PFpatSequence +
                                
                                ak2CalopatSequence +
                                ak3CalopatSequence +
                                ak4CalopatSequence +
                                ak5CalopatSequence 
                                
                                )

makeBTaggedHeavyIonJets = cms.Sequence(
                                akPu3PFpatSequence_withBtagging +
                                akPu4PFpatSequence_withBtagging +
                                akPu5PFpatSequence_withBtagging
                                )

makeHeavyIonVsJets = cms.Sequence(
    akVs3PFpatSequence 
    #+ akVs3CalopatJets
)
                               
akPu3PFpatSequence_withBtagging = cms.Sequence(akPu3PFcorr * akPu3PFclean * akPu3PFmatch * akPu3PFparton * akPu3PFPatJetFlavourId * akPu3PFJetTracksAssociator *akPu3PFJetBtagging * akPu3PFpatJets)







