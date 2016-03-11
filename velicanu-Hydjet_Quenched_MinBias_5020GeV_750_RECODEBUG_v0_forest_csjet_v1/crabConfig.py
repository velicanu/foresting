from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'velicanu-Hydjet_Quenched_MinBias_5020GeV_750_RECODEBUG_v0_forest_csjet_v1'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_MB_75X.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/Hydjet_Quenched_MinBias_5020GeV_750/velicanu-Hydjet_Quenched_MinBias_5020GeV_750_RECODEBUG_v0-eb8cf5655150b59e96d879ea397567ad/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'velicanu-Hydjet_Quenched_MinBias_5020GeV_750_RECODEBUG_v0_forest_csjet_v1'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
