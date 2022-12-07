import eurostat
import pandas as pd

title = "Distribution of population by tenure status, type of household and income group - EU-SILC survey"
code = 'ilc_lvho02'
pars = eurostat.get_pars(code)
my_filter_pars = {"geo" : "IT", "hhtyp" : "TOTAL", "tenure" : ["OWN","OWN_L","RENT"], "incgrp" : "TOTAL", 'startPeriod': 2011}
data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
print(title)
print(data)
# print(data.iloc[:,len(pars):data.size])

title = "House price index (2015 = 100) - annual data"
code = 'PRC_HPI_A'
pars = eurostat.get_pars(code)
my_filter_pars = {"geo" : "IT", "purchase" : "TOTAL", "unit": ["I10_A_AVG","I15_A_AVG","RCH_A_AVG"], 'startPeriod': 2011}
data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
print(title)
print(data)
# print(data.iloc[:,len(pars):data.size])
 
title = "Arrears (mortgage or rent, utility bills or hire purchase) from 2003 onwards - EU-SILC survey"
code = 'ILC_MDES05'
pars = eurostat.get_pars(code)
my_filter_pars = {"geo" : "IT", "incgrp" : "TOTAL", "hhtyp": "TOTAL", 'startPeriod': 2011}
data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
print(title)
print(data)
# print(data.iloc[:,len(pars):data.size])

title = "Share of housing costs in disposable household income, by type of household and income group - EU-SILC survey"
code = 'ILC_MDED01'
pars = eurostat.get_pars(code)
my_filter_pars = {"geo" : "IT", "hhtyp": "TOTAL", 'startPeriod': 2011}
data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
print(title)
print(data)
# print(data.iloc[:,len(pars):data.size])

title = "HICP - monthly data (annual rate of change)"
code = 'PRC_HICP_MANR'
pars = eurostat.get_pars(code)
my_filter_pars = {"geo" : "IT", 'startPeriod': "2011-01"}
data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
print(title)
print(data)
# print(data.iloc[:,len(pars):data.size])
dummy=1