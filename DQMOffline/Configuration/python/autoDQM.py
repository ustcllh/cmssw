autoDQM = { 'common' : ['DQMOfflineCommon',
                        'PostDQMOffline',
                        'DQMHarvestCommon+DQMCertCommon'],
            'commonSiStripZeroBias' : ['DQMOfflineCommonSiStripZeroBias',
                                       'PostDQMOffline',
                                       'DQMHarvestCommonSiStripZeroBias+DQMCertCommon'],
            'trackingOnlyDQM' : ["DQMOfflineTracking",
                             "DQMHarvestTracking"],
            'muon': ['DQMOfflineMuon',
                     'PostDQMOffline',
                     'DQMHarvestMuon+DQMCertMuon'],
            'hcal':     ['DQMOfflineHcal',
                         'PostDQMOffline',
                         'DQMHarvestHcal+DQMCertHcal'],
            'jetmet':  ['DQMOfflineJetMET',
                        'PostDQMOffline',
                        'DQMHarvestJetMET+DQMCertJetMET'],
            'ecal':       ['DQMOfflineEcal',
                           'PostDQMOffline',
                           'DQMHarvestEcal+DQMCertEcal'],
            'egamma':       ['DQMOfflineEGamma',
                             'PostDQMOffline',
                           'DQMHarvestEGamma'],
            'btag':       ['DQMOfflineBTag',
                           'PostDQMOffline',
                           'DQMHarvestBTag'],
            'HLTMon':     ['HLTMonitoring',
                           'PostDQMOffline',
                           'HLTMonitoringClient'],
            'HLTMonPA' :  ['HLTMonitoringPA', 'PostDQMOffline', 'HLTMonitoringClientPA'],
            'express':       ['@commonSiStripZeroBias+@muon+@hcal+@jetmet+@ecal',
                              'PostDQMOffline',
                              '@commonSiStripZeroBias+@muon+@hcal+@jetmet+@ecal'],
            'allForPrompt':  ['@common+@muon+@hcal+@jetmet+@ecal',
                              'PostDQMOffline',
                              '@common+@muon+@hcal+@jetmet+@ecal'],

            'miniAODDQM': ['DQMOfflineMiniAOD',
                           'PostDQMOfflineMiniAOD',
                           'DQMHarvestMiniAOD'],
            'standardDQM': ['DQMOffline',
                            'PostDQMOffline',
                            'dqmHarvesting'],
            'standardDQMFakeHLT': ['DQMOfflineFakeHLT',
                                   'PostDQMOffline',
                                   'dqmHarvestingFakeHLT'],
            'liteDQMHI': ['liteDQMOfflineHeavyIons',
                          'PostDQMOffline',
                          'dqmHarvesting']
            }

