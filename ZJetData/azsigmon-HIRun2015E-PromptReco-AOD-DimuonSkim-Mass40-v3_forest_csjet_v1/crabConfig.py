from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'azsigmon-HIRun2015E-PromptReco-AOD-DimuonSkim-Mass40-v3_forest_csjet_v1'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_DATA_75X.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/HIEWQExo/azsigmon-HIRun2015E-PromptReco-AOD-DimuonSkim-Mass40-v3-4f10cc0edb1df2aaccd97a62c3f32713/USER'
config.Data.inputDBS = 'phys03'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'azsigmon-HIRun2015E-PromptReco-AOD-DimuonSkim-Mass40-v3_forest_csjet_v1'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT', 'T2_HU_Budapest']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
