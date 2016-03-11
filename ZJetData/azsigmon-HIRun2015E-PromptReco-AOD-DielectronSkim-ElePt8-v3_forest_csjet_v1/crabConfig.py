from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'azsigmon-HIRun2015E-PromptReco-AOD-DielectronSkim-ElePt8-v3_forest_csjet_v1'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_DATA_75X.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/HIPhoton40AndZ/azsigmon-HIRun2015E-PromptReco-AOD-DielectronSkim-ElePt8-v3-f8ca4a1d94c645c1a352f0d31009e079/USER'
config.Data.inputDBS = 'phys03'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 20
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'azsigmon-HIRun2015E-PromptReco-AOD-DielectronSkim-ElePt8-v3_forest_csjet_v1'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT', 'T2_HU_Budapest']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
