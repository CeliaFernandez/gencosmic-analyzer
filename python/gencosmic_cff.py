import FWCore.ParameterSet.Config as cms

gencosmicproducer = cms.EDAnalyzer('gencosmicproducer',
    nameOfOutput = cms.string('output.root'),
    EventInfo = cms.InputTag("generator"),
    RunInfo = cms.InputTag("generator"),
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    GenParticleCollection = cms.InputTag("genParticles"),
    #PrimaryVertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices"),
    #bits = cms.InputTag("TriggerResults","","HLT"),
    theGenEventInfoProduct = cms.InputTag("generator"),
)


