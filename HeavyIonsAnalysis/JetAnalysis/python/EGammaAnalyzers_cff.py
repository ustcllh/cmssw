import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.PhotonAnalysis.MultiPhotonAnalyzer_cfi import multiPhotonAnalyzer
multiPhotonAnalyzer.GenParticleProducer = cms.InputTag("hiGenParticles")
multiPhotonAnalyzer.PhotonProducer = cms.InputTag("selectedPatPhotons")
multiPhotonAnalyzer.VertexProducer = cms.InputTag("hiSelectedVertex")
multiPhotonAnalyzer.OutputFile = cms.string('mpa.root')
multiPhotonAnalyzer.doStoreCompCone = cms.untracked.bool(False)
multiPhotonAnalyzer.doStoreJets = cms.untracked.bool(False)

multiPhotonAnalyzer.gsfElectronCollection = cms.untracked.InputTag("ecalDrivenGsfElectrons")
multiPhotonAnalyzer.GammaEtaMax = cms.untracked.double(100)
multiPhotonAnalyzer.GammaPtMin = cms.untracked.double(10)

from edwenger.HiTrkEffAnalyzer.TrackSelections_cff import hiGoodTracks
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import photonMatch, patPhotons, selectedPatPhotons

hiGoodTracks.src = cms.InputTag("hiGeneralTracks")
photonMatch.matched = cms.InputTag("hiGenParticles")
patPhotons.addPhotonID = cms.bool(False)

photonStep = cms.Sequence(hiGoodTracks *
                          photonMatch *
                          patPhotons *
                          selectedPatPhotons * 
                          multiPhotonAnalyzer)
