from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'Pythia8_EmEnrDijet30_Hydjet_MB-HINPbPbWinter16DR-75X_mcRun2_HeavyIon_forest_v1'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/Pythia8_EmEnrDijet30_Hydjet_MB/HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v13-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = "LumiBased"
config.Data.unitsPerJob = 15
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'Pythia8_EmEnrDijet30_Hydjet_MB-HINPbPbWinter16DR-75X_mcRun2_HeavyIon_forest_v1'
config.section_('User')
config.section_('Site')
#config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
