import FWCore.ParameterSet.Config as cms

from RecoHI.HiTracking.HighPtTracking_PbPb_cff import *

hiPixel3PrimTracks.OrderedHitsFactoryPSet.GeneratorPSet.maxElement=10000000
hiPixel3PrimTracks.RegionFactoryPSet.RegionPSet.ptMin = 0.4
hiPixel3PrimTracks.RegionFactoryPSet.RegionPSet.originRadius = 1
hiPixel3PrimTracks.FilterPSet.ptMin = 0.4
ckfBaseTrajectoryFilter.filterPset.minPt = 0.4




