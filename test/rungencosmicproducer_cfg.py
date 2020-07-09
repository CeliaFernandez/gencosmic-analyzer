import FWCore.ParameterSet.Config as cms


process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("MyAnalysis.gencosmic-analyzer.gencosmic_cff")
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'  # or some other global tag depending on your CMSSW release and sample. 
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(5000) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       [
'file:/afs/cern.ch/work/f/fernance/private/Long_Lived_Analysis/CMSSW_8_0_21/src/MyAnalysis/gencosmic-analyzer/test/EXO-RunIISummer15GS_LooseMuCosmic_38T_p10_3000.root'
       ]
    )
)

process.p = cms.Path(process.gencosmicproducer)


