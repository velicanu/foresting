from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'HIMinimumBias2-HIRun2015-PromptReco-v1_forest_csjet_v1'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_DATA_75X.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/HIMinimumBias2/HIRun2015-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.runRange = '263233-263293'
config.Data.splitting = "LumiBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'HIMinimumBias2-HIRun2015-PromptReco-v1_forest_csjet_v1'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT', 'T2_US_Vanderbilt']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
