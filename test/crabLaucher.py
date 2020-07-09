from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferLogs = True
config.General.requestName = 'cosmicTuples_2'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'rungencosmicproducer_cfg.py'
config.JobType.disableAutomaticOutputCollection = True
config.JobType.outputFiles = ['output.root']
config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.inputDataset = '/CosmicMuonsMCPrivate2016_smallVolume/fernance-CosmicMuonsMCPrivate2016_smallVolume-6682ed0fefa7599ce7b37d4a2b3d10aa/USER'
config.Data.publication = False
config.Data.outLFNDirBase = '/store/user/fernance/' 

config.section_('Site')
config.Site.storageSite = 'T2_ES_IFCA'
