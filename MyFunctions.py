from operator import mod
import pandas as pd
import numpy as np

def CalcolaMutuoAPI(UserData) :
    
    TotFinanziamento = float(UserData["Finanziamento"])
    In_AnniTotCalc = int(UserData["Anni per Calcolo Mutuo"])
    RateTotali = int(In_AnniTotCalc*12)
    In_Tasso = float(UserData["Tasso di Interesse"])
    TassoTot = float(In_Tasso/100)
    In_AnniTotTasso = int(UserData["Durata Anni Tasso Fisso"])
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
            Rata[idx] = (TotFinanziamento*TassoTot/12)/(1-(1/(1+TassoTot/12)**(RateTotali)))
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

    Tilgung = float((Rata[1]-TassoTot*TotFinanziamento/12)*12/TotFinanziamento)
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
        "Rimborso Capitale %" : round(Tilgung*100,2),
        "Rata €" : round(Rata[1],1),
        "Capitale Rimanente €" : round(MaxiRataFinale,0)
    }

    TotFinanziamentoList = ["Finanziamento €" , round(TotFinanziamento,0)]
    In_AnniTotTassoList = ["Anni Tasso Fisso " , In_AnniTotTasso]
    TassoTotList = ["Tasso %" , round(TassoTot*100,2)]
    TilgungList = ["Rimborso Capitale %" , round(Tilgung*100,2)]
    RataList = ["Rata €", round(Rata[1],1)]
    MaxiRataFinaleList = ["Capitale Rimanente €" , round(MaxiRataFinale,0)]


    OutputOverviewMutuo = pd.DataFrame(list(zip(TotFinanziamentoList, In_AnniTotTassoList, TassoTotList, TilgungList, RataList, MaxiRataFinaleList )),
        columns =["Finanziamento €", "Anni Tasso Fisso", "Tasso %", "Rimborso %", "Rata €", "Capitale Rimanente €" ])

    OutputOverviewMutuo2 = pd.DataFrame(OVdata, index=["Val"])
    OutputOverviewMutuo = OutputOverviewMutuo.T
    # OutputOverviewMutuo = OutputOverviewMutuo.round(1)    
    dummy=1
    return OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo

def CalcolaCashIniziale(InputsSpeseIniziali, InputsCasa, InputsMutuo) :

    SpeseIniziali = {
        "CostoAgenzia" : InputsSpeseIniziali["Agenzia"]*0.01*InputsCasa["Offerta"],
        "CostoNotaio" : InputsSpeseIniziali["Notaio"],
        "CostoIstruttoria" : InputsSpeseIniziali["Istruttoria"]*0.01*InputsCasa["Offerta"],
        "CostoSostituitiva" : InputsSpeseIniziali["Sostituitiva"]*0.01*InputsCasa["Offerta"],
        "CostoPerizia" : InputsSpeseIniziali["Perizia"]
    }

    SpeseIniziali["TotCosti"] = SpeseIniziali["CostoAgenzia"] + SpeseIniziali["CostoNotaio"] + SpeseIniziali["CostoIstruttoria"] + SpeseIniziali["CostoSostituitiva"] + SpeseIniziali["CostoPerizia"]
    SpeseIniziali["AnticipoMutuo"] = InputsCasa["Offerta"]*(100-InputsMutuo["PercFinanziata"])*0.01
    SpeseIniziali["SpesaTotIniziale"] = SpeseIniziali["TotCosti"] + SpeseIniziali["AnticipoMutuo"]
    
    
    # CostoAgenzia = InputsSpeseIniziali["Agenzia"]*0.01*InputsCasa["Offerta"]
    # CostoNotaio = InputsSpeseIniziali["Notaio"]
    # CostoIstruttoria = InputsSpeseIniziali["Istruttoria"]*0.01*InputsCasa["Offerta"]
    # CostoSostituitiva = InputsSpeseIniziali["Sostituitiva"]*0.01*InputsCasa["Offerta"]
    # CostoPerizia = InputsSpeseIniziali["Perizia"]
    # Costi = CostoAgenzia + CostoNotaio + CostoIstruttoria + CostoSostituitiva + CostoPerizia
    # AnticipoMutuo = InputsCasa["Offerta"]*(100-InputsMutuo["PercFinanziata"])*0.01
    # SpesaTotIniziale = Costi + AnticipoMutuo

    OutputsSpeseIniziali = pd.DataFrame(data=SpeseIniziali, index=[0])
    OutputsSpeseIniziali.round(2)

    return OutputsSpeseIniziali

def CalcolaIMU(InputsCasa) : 

    CoeffRivalutazione = 5
    if InputsCasa["CatCatastale"] == ("A/1" or "A/2" or "A/3" or "A/4" or "A/5" or "A/6" or "A/7" or "A/8" or "A/9" or "A/11") :
        CoeffCatastale = 160
    elif InputsCasa["CatCatastale"] == "A/10" :
        CoeffCatastale = 80
    else :
        CoeffCatastale = 160
    
    if InputsCasa["PrimaCasa"] == "No" :
        AliquotaIMU = 1.14
    elif InputsCasa["PrimaCasa"] == "Si" :
        AliquotaIMU = 0.6
    else :
        AliquotaIMU = 0.6

    ValoreCatastale = (InputsCasa["RenditaCatastale"]*(1+(CoeffRivalutazione*0.01)))*CoeffCatastale
    IMU = ValoreCatastale*(AliquotaIMU*0.01)

    return IMU

