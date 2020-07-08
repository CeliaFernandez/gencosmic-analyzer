from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferLogs = True
config.General.requestName = 'HXX'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runGenNtupleproducer_cfg.py'
config.JobType.disableAutomaticOutputCollection = True
config.JobType.outputFiles = ['output.root']
config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.inputDataset = '/H2ToLLPXToLeptons_MH_400_MX_150_ctau_400mm_TuneCP2_13TeV_pythia8_80X_13082019-1313/fernance-H2ToLLPXToLeptons_MH_400_MX_150_ctau_400mm_TuneCP2_13TeV_pythia8_80X_13082019-1313-ef2621b02f2b5d29bc3a862b28195ada/USER'
config.Data.publication = False
config.Data.outLFNDirBase = '/store/user/fernance/' 

config.section_('Site')
config.Site.storageSite = 'T2_ES_IFCA'
