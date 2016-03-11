from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'twang-Pythia8_Zmu10mu10Jet_m60120_pthat0_TuneCUETP8M1_5020GeV_step3_forest_csjet_v1'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/Pythia8_Zmu10mu10Jet_m60120_pthat0_TuneCUETP8M1_5020GeV_GEN_SIM_PU_20160110/twang-Pythia8_Zmu10mu10Jet_m60120_pthat0_TuneCUETP8M1_5020GeV_step3_20160110-7268d177294694b3762cc51e73fbc45b/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'twang-Pythia8_Zmu10mu10Jet_m60120_pthat0_TuneCUETP8M1_5020GeV_step3_forest_csjet_v1'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
