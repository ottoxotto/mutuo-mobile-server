import eurostat
import pandas as pd

# title = "Distribution of population by tenure status, type of household and income group - EU-SILC survey"
# code = 'ilc_lvho02'
# pars = eurostat.get_pars(code)
# my_filter_pars = {"geo" : "IT", "hhtyp" : "TOTAL", "tenure" : ["OWN","OWN_L","RENT"], "incgrp" : "TOTAL", 'startPeriod': 2011}
# data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
# print(title)
# print(data)
# # print(data.iloc[:,len(pars):data.size])

# title = "House price index (2015 = 100) - annual data"
# code = 'PRC_HPI_A'
# pars = eurostat.get_pars(code)
# my_filter_pars = {"geo" : "IT", "purchase" : "TOTAL", "unit": ["I10_A_AVG","I15_A_AVG","RCH_A_AVG"], 'startPeriod': 2011}
# data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
# print(title)
# print(data)
# # print(data.iloc[:,len(pars):data.size])
 
# title = "Arrears (mortgage or rent, utility bills or hire purchase) from 2003 onwards - EU-SILC survey"
# code = 'ILC_MDES05'
# pars = eurostat.get_pars(code)
# my_filter_pars = {"geo" : "IT", "incgrp" : "TOTAL", "hhtyp": "TOTAL", 'startPeriod': 2011}
# data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
# print(title)
# print(data)
# # print(data.iloc[:,len(pars):data.size])

# title = "Share of housing costs in disposable household income, by type of household and income group - EU-SILC survey"
# code = 'ILC_MDED01'
# pars = eurostat.get_pars(code)
# my_filter_pars = {"geo" : "IT", "hhtyp": "TOTAL", 'startPeriod': 2011}
# data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
# print(title)
# print(data)
# # print(data.iloc[:,len(pars):data.size])

title = "HICP - monthly data (annual rate of change)"
code = 'PRC_HICP_MANR'
pars = eurostat.get_pars(code)
my_filter_pars = {"geo" : "IT", "coicop": "CP00",  'startPeriod': "2011-01"}
data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
print(title)
print(data)
# print(data.iloc[:,len(pars):data.size])
dummy=1

import numpy as np
import pandas as pd

UserData = {
    "Finanziamento": "400000",
    "Rimborso Capitale": "2.85",
    "Tasso di Interesse": "3.75",
    "Durata Anni Tasso Fisso": "20",
}

for key in UserData:
    UserData[key] = UserData[key].strip("€")
    UserData[key] = UserData[key].strip("%")
    UserData[key] = UserData[key].replace(",","")

TotFinanziamento = float(UserData["Finanziamento"])
In_Tilgung = float(UserData["Rimborso Capitale"])
In_Tasso = float(UserData["Tasso di Interesse"])
TassoTot = float(In_Tasso/100)
In_AnniTotTasso = int(UserData["Durata Anni Tasso Fisso"])
In_AnniTotCalc = In_AnniTotTasso
RateTotali = int(In_AnniTotCalc*12)
RataFinale = int(In_AnniTotTasso*12)

# Inizializza liste
NumRata = [i for i in range(0,RateTotali+1)]
AnniRata = ["" for i in range(0,RateTotali+1)]
Rata = ["" for i in range(0,RateTotali+1)]
InteressePerRata = ["" for i in range(0,RateTotali+1)]
CapitalePerRata = ["" for i in range(0,RateTotali+1)]
TotCapRimanente = ["" for i in range(0,RateTotali+1)]
TotInteressi = ["" for i in range(0,RateTotali+1)]

RataMediaAnnua = ["" for i in range(0,In_AnniTotCalc+1)]
CapitaleMedioAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
InteresseMedioAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
TotCapRimanenteAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
TotInteressiAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
AnniRataAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]

AnniMediaTot = []
CapitaleMedioAnniTot  = []
InteresseMedioAnniTot  = []

TotFinanziamentoList = []
In_AnniTotTassoList = []

for idx in range(0, RateTotali+1):
    if idx == 0 :
        Rata[idx] = 0
        AnniRata[idx] = 0
        InteressePerRata[idx] = 0
        CapitalePerRata[idx] = 0
        TotCapRimanente[idx] = TotFinanziamento
        TotInteressi[idx] = 0
        RataMediaAnnua[idx] = 0

        RataMediaAnnua[idx] = Rata[idx]
        CapitaleMedioAnnuo[idx] = CapitalePerRata[idx]
        InteresseMedioAnnuo[idx] = InteressePerRata[idx]
        TotCapRimanenteAnnuo[idx] = TotCapRimanente[idx]
        TotInteressiAnnuo[idx] = TotInteressi[idx]
        AnniRataAnnuo[idx] = AnniRata[idx]
    else:
        Rata[idx] = float((TotFinanziamento/12)*(In_Tilgung+In_Tasso)/100)
        InteressePerRata[idx] = TotCapRimanente[idx-1]*TassoTot/12
        CapitalePerRata[idx] = Rata[idx]-InteressePerRata[idx]
        TotCapRimanente[idx] = TotCapRimanente[idx-1]-CapitalePerRata[idx]
        TotInteressi[idx] = TotInteressi[idx-1]+InteressePerRata[idx]

        AnniRata[idx] = int((idx-1)/12)+1
        
        if (AnniRata[idx]> AnniRata[idx-1] and AnniRata[idx-1]>0) or (idx == RateTotali) :
            RataMediaAnnua[AnniRata[idx-1]] = np.mean(Rata[idx-11:idx+1])
            CapitaleMedioAnnuo[AnniRata[idx-1]] = np.mean(CapitalePerRata[idx-11:idx+1]) 
            InteresseMedioAnnuo[AnniRata[idx-1]] = np.mean(InteressePerRata[idx-11:idx+1])
            TotCapRimanenteAnnuo[AnniRata[idx-1]] = TotCapRimanente[idx]
            TotInteressiAnnuo[AnniRata[idx-1]] = TotInteressi[idx]
            AnniRataAnnuo[AnniRata[idx-1]] = AnniRata[idx-1]


if In_AnniTotCalc>=5:
    CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[1:5]))
    InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[1:5]))
    AnniMediaTot.append("1-5")
    if In_AnniTotCalc>=10:
        CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[1:10]))
        InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[1:10]))
        AnniMediaTot.append("1-10")
        if In_AnniTotCalc>10:
            CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[11:In_AnniTotTasso]))
            InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[1:In_AnniTotTasso]))
            AnniMediaTot.append("11-" + UserData["Durata Anni Tasso Fisso"] )


MaxiRataFinale = float(TotCapRimanente[RataFinale])

OutputsMutuo = pd.DataFrame(list(zip(NumRata, AnniRata, Rata, CapitalePerRata, InteressePerRata, TotCapRimanente, TotInteressi)),
    columns =["N° Rata", "Anno", "Rata €", "Capitale €", "Interesse €", "Tot. Capitale da ripagare €", "Tot. Interessi pagati €" ])
        
OutputsMutuo = OutputsMutuo.round(1)

OutputsAnnuoMutuo = pd.DataFrame(list(zip(AnniRataAnnuo, CapitaleMedioAnnuo, InteresseMedioAnnuo, TotCapRimanenteAnnuo, TotInteressiAnnuo)),
    columns =["Anno", "Capitale medio annuo €", "Interesse medio annuo €", "Tot. Capitale rimanente €", "Tot. Interessi pagati €"])

OutputsAnnuoMutuo = OutputsAnnuoMutuo.round(1)

OutputAvgMutuo = pd.DataFrame(list(zip(AnniMediaTot, CapitaleMedioAnniTot, InteresseMedioAnniTot)),
    columns =["Anni", "Capitale medio €", "Interesse medio €"])

OutputAvgMutuo = OutputAvgMutuo.round(1)

OVdata = {
    "Finanziamento €" : round(TotFinanziamento,0),
    "Anni Tasso Fisso " : In_AnniTotTasso,
    "Tasso %" : round(TassoTot*100,2),
    "Rimborso Capitale %" : round(In_Tilgung,2),
    "Rata €" : round(Rata[1],1),
    "Capitale Rimanente €" : round(MaxiRataFinale,0)
}

TotFinanziamentoList = ["Finanziamento €" , round(TotFinanziamento,0)]
In_AnniTotTassoList = ["Anni Tasso Fisso " , In_AnniTotTasso]
TassoTotList = ["Tasso %" , round(TassoTot*100,2)]
TilgungList = ["Rimborso Capitale %" , round(In_Tilgung,2)]
RataList = ["Rata €", round(Rata[1],1)]
MaxiRataFinaleList = ["Capitale Rimanente €" , round(MaxiRataFinale,0)]


OutputOverviewMutuo = pd.DataFrame(list(zip(TotFinanziamentoList, In_AnniTotTassoList, TassoTotList, TilgungList, RataList, MaxiRataFinaleList )),
    columns =["Finanziamento €", "Anni Tasso Fisso", "Tasso %", "Rimborso %", "Rata €", "Capitale Rimanente €" ])

OutputOverviewMutuo2 = pd.DataFrame(OVdata, index=["Val"])
OutputOverviewMutuo = OutputOverviewMutuo.T
# OutputOverviewMutuo = OutputOverviewMutuo.round(1)    
dummy=1