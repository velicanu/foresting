from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'gsfs-Pythia8_Photon120_Hydjet_RECO_20160306_forest_v28_2'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/Pythia8_Photon120_Hydjet_MB/gsfs-Pythia8_Photon120_Hydjet_RECO_20160306-a78b3072e46c33a0fe1fffcdcc303b7d/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'gsfs-Pythia8_Photon120_Hydjet_RECO_20160306_forest_v28_2'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
