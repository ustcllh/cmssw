import FWCore.ParameterSet.Config as cms

import RecoTracker.FinalTrackSelectors.trackListMerger_cfi
hiGeneralTracks = RecoTracker.FinalTrackSelectors.trackListMerger_cfi.trackListMerger.clone(
    TrackProducers = (cms.InputTag('hiGlobalPrimTracks'),
                      cms.InputTag('hiSecondPixelTripletGlobalPrimTracks'),
                      cms.InputTag('hiPixelPairGlobalPrimTracks'),
#                      cms.InputTag('hiLowPtPixelTripletGlobalPrimTracks'),
                       cms.InputTag('hiPixel3PrimTracks'),
                     ),
    hasSelector=cms.vint32(1,1,1,0),
    selectedTrackQuals = cms.VInputTag(
    cms.InputTag("hiInitialStepSelector","hiInitialStep"),
    cms.InputTag("hiSecondPixelTripletStepSelector","hiSecondPixelTripletStep"),
    cms.InputTag("hiPixelPairStepSelector","hiPixelPairStep"),
#    cms.InputTag("hiLowPtPixelTripletStepSelector","hiLowPtPixelTripletStep"),
    ),                    
    setsToMerge = cms.VPSet( cms.PSet( tLists=cms.vint32(0,1,2,3), pQual=cms.bool(True)),  # should this be False?
                             ),
    copyExtras = True,
    makeReKeyedSeeds = cms.untracked.bool(False)
    )
