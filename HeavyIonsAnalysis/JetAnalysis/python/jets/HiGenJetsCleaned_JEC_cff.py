import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *

ak2HiGenJetsCleaned_JEC = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak2HiGenJets') , ptCut = 1)

ak3HiGenJetsCleaned_JEC = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak3HiGenJets') , ptCut = 1)

ak4HiGenJetsCleaned_JEC = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak4HiGenJets') , ptCut = 1)

ak5HiGenJetsCleaned_JEC = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak5HiGenJets') , ptCut = 1)

ak6HiGenJetsCleaned_JEC = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak6HiGenJets') , ptCut = 1)

ak7HiGenJetsCleaned_JEC = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak7HiGenJets') , ptCut = 1)

hiGenJetsCleaned_JEC = cms.Sequence(
ak2HiGenJetsCleaned_JEC
+
ak3HiGenJetsCleaned_JEC
+
ak4HiGenJetsCleaned_JEC
+
ak5HiGenJetsCleaned_JEC
+
ak6HiGenJetsCleaned_JEC
+
ak7HiGenJetsCleaned_JEC
)
