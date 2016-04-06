from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'Hydjet_Quenched_MinBias_5020GeV_750-HINPbPbWinter16DR-NoPU_75X_mcRun2_HeavyIon_forest_v2'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_MB_75X.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/Hydjet_Quenched_MinBias_5020GeV_750/HINPbPbWinter16DR-NoPU_75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v13-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = "LumiBased"
config.Data.unitsPerJob = 12
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'Hydjet_Quenched_MinBias_5020GeV_750-HINPbPbWinter16DR-NoPU_75X_mcRun2_HeavyIon_forest_v2'
config.section_('User')
config.section_('Site')
#config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
