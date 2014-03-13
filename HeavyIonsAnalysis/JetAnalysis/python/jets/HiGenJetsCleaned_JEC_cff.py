import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *

ak2HiGenJetsCleaned = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak2HiGenJets') , ptCut = 1)

ak3HiGenJetsCleaned = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak3HiGenJets') , ptCut = 1)

ak4HiGenJetsCleaned = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak4HiGenJets') , ptCut = 1)

ak5HiGenJetsCleaned = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak5HiGenJets') , ptCut = 1)

ak6HiGenJetsCleaned = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak6HiGenJets') , ptCut = 1)

ak7HiGenJetsCleaned = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak7HiGenJets') , ptCut = 1)

hiGenJetsCleanedJEC = cms.Sequence(
ak2HiGenJetsCleaned
+
ak3HiGenJetsCleaned
+
ak4HiGenJetsCleaned
+
ak5HiGenJetsCleaned
+
ak6HiGenJetsCleaned
+
ak7HiGenJetsCleaned
)
