import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.rechitanalyzer_pp_cfi import *

rechitanalyzer.vtxSrc = cms.untracked.InputTag("offlinePrimaryVerticesWithBS")

