import FWCore.ParameterSet.Config as cms

hiFJRhoFlowModulationProducer = cms.EDProducer('HiFJRhoFlowModulationProducer',
                                                   mapToRho = cms.InputTag('hiFJRhoProducer','mapToRho'),
                                                   mapToRhoM = cms.InputTag('hiFJRhoProducer','mapToRhoM'),
                                                   pfCandSource = cms.InputTag('particleFlowTmp'),
                                                   jetSource = cms.InputTag('kt4PFJets')
                                                   )

