from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'DYJetsToLL_TuneCUETP8M1_5020GeV-amcatnloFXFX-pythia8_HINppWinter16DR-75X_mcRun2_forest_v1'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_pp_MC_75X.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/DYJetsToLL_TuneCUETP8M1_5020GeV-amcatnloFXFX-pythia8/HINppWinter16DR-75X_mcRun2_asymptotic_ppAt5TeV_v3-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'DYJetsToLL_TuneCUETP8M1_5020GeV-amcatnloFXFX-pythia8_HINppWinter16DR-75X_mcRun2_forest_v1'
config.section_('User')
config.section_('Site')
#config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
