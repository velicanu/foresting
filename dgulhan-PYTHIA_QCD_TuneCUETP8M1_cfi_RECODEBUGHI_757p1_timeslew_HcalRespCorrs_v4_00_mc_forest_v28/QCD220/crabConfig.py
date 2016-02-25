from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'dgulhan-PYTHIA_QCD220_TuneCUETP8M1_cfi_RECODEBUGHI_757p1_timeslew_HcalRespCorrs_v4_00_mc_forest_v28'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-PYTHIA_QCD220_TuneCUETP8M1_cfi_RECODEBUGHI_757p1_timeslew_HcalRespCorrs_v4_00_mc-0c2cabf082becbca738f32b000cf9a7a/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'dgulhan-PYTHIA_QCD220_TuneCUETP8M1_cfi_RECODEBUGHI_757p1_timeslew_HcalRespCorrs_v4_00_mc_forest_v28'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
