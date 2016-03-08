from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'gsfs-Pythia8_Photon50_pp_RECO_forest_v28'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_pp_MC_75X.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/Pythia8_Photon50_pp502_TuneCUETP8M1/gsfs-Pythia8_Photon50_pp_RECO_20160306-0564587735dfa98972125c928a8975ef/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'gsfs-Pythia8_Photon50_pp_RECO_forest_v28'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
