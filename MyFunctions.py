from operator import mod
import eurostat
import pandas as pd
import numpy as np

def CalcolaMutuoAnniCalcAPI(UserData) :
    
    for key in UserData:
        UserData[key] = UserData[key].strip("€")
        UserData[key] = UserData[key].strip("%")
        UserData[key] = UserData[key].replace(",","")

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

def CalcolaMutuoRataFissaAPI(UserData) :
    
    for key in UserData:
        UserData[key] = UserData[key].strip("€")
        UserData[key] = UserData[key].strip("%")
        UserData[key] = UserData[key].replace(",","")

    TotFinanziamento = float(UserData["Finanziamento"])
    In_Rata = float(UserData["Rata"])
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
            Rata[idx] = In_Rata
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

def CalcolaMutuoTilgungAPI(UserData) :

    for key in UserData:
        UserData[key] = UserData[key].strip("€")
        UserData[key] = UserData[key].strip("%")
        UserData[key] = UserData[key].replace(",","")

    TotFinanziamento = float(UserData["Finanziamento"])
    In_Tilgung = float(UserData["Tilgung"])
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

def CalcolaCashIniziale(UserData) :

    for key in UserData:
        UserData[key] = UserData[key].strip("€")
        UserData[key] = UserData[key].strip("%")
        UserData[key] = UserData[key].replace(",","")
        
    Finanziamento = float(UserData["Prezzo Immobile"])*float(UserData["Percentuale Mutuo"])*0.01

    if float(UserData["Spese di Istruttoria"])>=0 and float(UserData["Spese di Istruttoria"])<=2:
        IstruttoriaType = "percentuale"
        Istruttoria = float(UserData["Spese di Istruttoria"])*0.01*(Finanziamento)
    elif float(UserData["Spese di Istruttoria"])>=50:
        IstruttoriaType = "fissa"
        Istruttoria = float(UserData["Spese di Istruttoria"])
    else:
        IstruttoriaType = "fissa"
        Istruttoria = 0.0

    if "Prima" in UserData["Tipologia Acquisto"]:
        Sostitutiva = 0.25
        SpesaSostitutiva = Sostitutiva*Finanziamento*0.01
        if "Privato" in UserData["Tipologia Acquisto"]:
            Registro = 2
            SpesaRegistro = Registro*0.01*float(UserData["Prezzo Immobile"])
            if SpesaRegistro <1000:
                SpesaRegistro = 1000
            SpesaIpotecaria = 50
            SpesaCatastale = 50
            IVA = 0
            SpesaIVA = IVA*float(UserData["Prezzo Immobile"])*0.01
        elif "Costruttore" in UserData["Tipologia Acquisto"]:
            SpesaRegistro = 200
            SpesaIpotecaria = 200
            SpesaCatastale = 200
            IVA = 4
            SpesaIVA = IVA*float(UserData["Prezzo Immobile"])*0.01
    elif "Seconda" in UserData["Tipologia Acquisto"]:
        Sostitutiva = 2
        SpesaSostitutiva = Sostitutiva*Finanziamento*0.01
        if "Privato" in UserData["Tipologia Acquisto"]:
            Registro = 9
            SpesaRegistro = Registro*0.01*float(UserData["Prezzo Immobile"])
            if SpesaRegistro <1000:
                SpesaRegistro = 1000
            SpesaIpotecaria = 50
            SpesaCatastale = 50
            IVA = 0
            SpesaIVA = IVA*float(UserData["Prezzo Immobile"])*0.01
        elif "Costruttore" in UserData["Tipologia Acquisto"]:
            SpesaRegistro = 200
            SpesaIpotecaria = 200
            SpesaCatastale = 200
            if "Lusso" in UserData["Tipologia Acquisto"]:
                IVA = 22
                SpesaIVA = IVA*float(UserData["Prezzo Immobile"])*0.01
            else:
                IVA = 10
                SpesaIVA = IVA*float(UserData["Prezzo Immobile"])*0.01


    SpeseIniziali = {
        "PrezzoImmobile €" : float(UserData["Prezzo Immobile"]),
        "TotFinanziamento €" : Finanziamento,
        "CostoAgenzia" : float(UserData["Percentuale Agenzia"])*0.01*float(UserData["Prezzo Immobile"]),
        "CostoIstruttoria" : Istruttoria,
        "CostoSostitutiva" : SpesaSostitutiva,
        "CostoPerizia" : float(UserData["Spese di Perizia"]),
        "CostoAssicurazioni" : float(UserData["Assicurazioni"]),
        "CostoNotaio" : SpesaRegistro + SpesaIpotecaria + SpesaCatastale,
        "CostoIVA" : SpesaIVA
    }

    SpeseIniziali["TotCosti"] = SpeseIniziali["CostoAgenzia"] + SpeseIniziali["CostoNotaio"] + SpeseIniziali["CostoIstruttoria"] + SpeseIniziali["CostoSostitutiva"] + SpeseIniziali["CostoPerizia"] + SpeseIniziali["CostoAssicurazioni"] + SpeseIniziali["CostoIVA"]
    SpeseIniziali["AnticipoMutuo"] = float(UserData["Prezzo Immobile"])-Finanziamento
    SpeseIniziali["SpesaTotIniziale"] = SpeseIniziali["TotCosti"] + SpeseIniziali["AnticipoMutuo"]
    
    PrezzoImmobileList = ["Prezzo Immobile €" , round(SpeseIniziali["PrezzoImmobile €"],0)]
    TotFinanziamentoList = ["Tot. Finanziamento €" , round(SpeseIniziali["TotFinanziamento €"],0)]
    CostoAgenziaList = ["Parcella Agenzia €" , round(SpeseIniziali["CostoAgenzia"],0)]
    CostoIstruttoriaList = ["Spesa di Istruttoria €" , round(SpeseIniziali["CostoIstruttoria"],0)]
    CostoSostitutivaList = ["Imposta Sostitutiva €" , round(SpeseIniziali["CostoSostitutiva"],0)]
    CostoPeriziaList = ["Costo Perizia €" , round(SpeseIniziali["CostoPerizia"],0)]
    CostoAssicurazioniList = ["Costo Assicurazioni €" , round(SpeseIniziali["CostoAssicurazioni"],0)]
    CostoNotaioList = ["Costi Notarili €" , round(SpeseIniziali["CostoNotaio"],0)]
    CostoIVAList = ["IVA €" , round(SpeseIniziali["CostoIVA"],0)]

    TipologiaAcquistoList = ["Tip. Acquisto", UserData["Tipologia Acquisto"]]
    PercFinanziamentoList = ["Percentuale Mutuo %", float(UserData["Percentuale Mutuo"])]
    ImpostaRegistroList = ["Di cui Imposta di Registro", SpesaRegistro]
    ImpostaIpotecariaList = ["Di cui Imposta Ipotecaria", SpesaIpotecaria]
    ImpostaCatastaleList = ["Di cui Imposta Catastale", SpesaCatastale]




    OutputsSpeseInizialiDettaglio = pd.DataFrame(list(zip(PrezzoImmobileList, TipologiaAcquistoList, PercFinanziamentoList, TotFinanziamentoList, CostoAgenziaList, CostoIstruttoriaList, CostoSostitutivaList, CostoPeriziaList, CostoAssicurazioniList, CostoNotaioList, ImpostaRegistroList, ImpostaIpotecariaList, ImpostaCatastaleList, CostoIVAList )),
        columns =["Prezzo Immobile €", "Tip. Acquisto", "Percentuale Mutuo", "Tot. Finanziamento €", "Parcella Agenzia €", "Spesa di Istruttoria €", "Imposta Sostitutiva €", "Costo Perizia €", "Costo Assicurazioni €", "Costi Notarili €", "Di cui Imposta di Registro", "Di cui Imposta Ipotecaria", "Di cui Imposta Catastale", "IVA €"])

    OutputsSpeseInizialiDettaglio = OutputsSpeseInizialiDettaglio.T

    OutputsSpeseIniziali= pd.DataFrame(data=SpeseIniziali, index=[0])
    OutputsSpeseIniziali.round(0)

    return OutputsSpeseIniziali, OutputsSpeseInizialiDettaglio

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

def EurostatCall(UserData) :
    code = UserData["Grafico"]
    pars = eurostat.get_pars(code)

    if code == 'ilc_lvho02':
        title = "Distribution of population by tenure status, type of household and income group - EU-SILC survey"
        my_filter_pars = {"geo" : "IT", "hhtyp" : "TOTAL", "tenure" : ["OWN","OWN_L","RENT"], "incgrp" : "TOTAL", 'startPeriod': 2011}
    elif code == 'PRC_HPI_A':
        title = "House price index (2015 = 100) - annual data"
        my_filter_pars = {"geo" : "IT", "purchase" : "TOTAL", "unit": ["I10_A_AVG","I15_A_AVG","RCH_A_AVG"], 'startPeriod': 2011}
    elif code == 'ILC_MDES05':
        title = "Arrears (mortgage or rent, utility bills or hire purchase) from 2003 onwards - EU-SILC survey"
        my_filter_pars = {"geo" : "IT", "incgrp" : "TOTAL", "hhtyp": "TOTAL", 'startPeriod': 2011}
    elif code == 'ILC_MDED01':
        title = "Share of housing costs in disposable household income, by type of household and income group - EU-SILC survey"
        my_filter_pars = {"geo" : "IT", "hhtyp": "TOTAL", 'startPeriod': 2011}
    elif code == 'PRC_HICP_MANR':
        title = "HICP - monthly data (annual rate of change)"
        my_filter_pars = {"geo" : "IT", 'startPeriod': "2011-01"}


    data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
    data_filter = data.iloc[:,len(pars):data.size]

    return data