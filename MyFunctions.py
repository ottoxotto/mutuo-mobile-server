from operator import mod
import eurostat
import pandas as pd
import numpy as np

def LanguageDict(UserData) :

    if UserData["Language"] == "it":
        Dictionary = {
            "UserFinanziamento" : "Finanziamento",
            "UserAnniCalcMutuo" : "Anni per Calcolo Mutuo",
            "UserInTasso" : "Tasso di Interesse",
            "UserInAnniTotTasso" : "Anni Tasso Fisso",
            "UserInRata" : "Rata",
            "UserInMaxiRataAnnuale" : "Maxi-Rata Annuale",
            "UserInMeseMaxiRata" : "N° Mensilitá prima della Maxi-Rata",
            "UserInAmmortamento" : "Tasso di Ammortamento",
            "UserInPrezzo" : "Prezzo Immobile",
            "UserInPercMutuo" : "Percentuale Mutuo",
            "UserInPercAgenzia" : "Percentuale Agenzia",
            "UserInIstruttoria" : "Spese di Istruttoria",
            "UserInAssicurazione" : "Assicurazioni",
            "UserInPerizia" : "Spese di Perizia",
            "UserInGrunderwerbsteuer" : "Grunderwerbsteuer",
            "UserInGrundbuchkosten" : "Grundbuchkosten",
            "UserInNotarkosten" : "Notarkosten",
            "UserInMaklergebühren" : "Maklergebühren",
            "UserInTipAcquisto" : "Tipologia Acquisto",
            "UserInBundesland" : "Bundesland",
            "OutNRata" : "N° Rata",
            "OutAnno" : "Anno",
            "OutRata" : "Rata €",
            "OutCapitale" : "Capitale €",
            "OutInteresse" : "Interessi €",
            "OutTotCapResiduo" : "Capitale residuo €",
            "OutTotIntPagati" : "Interessi pagati €",
            "OutCapMedioAnnuo" : "Capitale Medio Annuo €",
            "OutIntMedioAnnuo" : "Interesse Medio Annuo €",
            "OutAnni" : "Anni",
            "OutCapMedio" : "Capitale Medio €",
            "OutIntMedio" : "Interesse Medio €",
            "OutFinanziamento" : "Finanziamento €",
            "OutAnniTassoFisso" : "Anni Tasso Fisso",
            "OutTasso" : "Tasso di Interesse %",
            "OutAmmortamento" : "Tasso diAmmortamento %",
            "OutMaxiRataAnnuale" : "Maxi-Rata Annuale €",
            "OutTotMaxiRata" : "Tot. Maxi-Rate Annuali €",
            "OutAnticipo" : "Anticipo Mutuo",
            "OutSpese" : "Spese Iniziali",
            "OutUsciteTot" : "Tot. Uscite Iniziali",
            "OutPrezzo" : "Prezzo Immobile €",
            "OutTipo" : "Tip. Acquisto",
            "OutAgenzia" : "Parcella Agenzia €",
            "OutIstruttoria" : "Spesa di Istruttoria €",
            "OutSostitutiva" : "Imposta Sostitutiva €",
            "OutPerizia" : "Costo Perizia €",
            "OutAssicurazioni" : "Costo Assicurazioni €",
            "OutNotaio" : "Costi Notarili €",
            "OutRegistro" : "Di cui Imposta di Registro",
            "OutIpotecaria" : "Di cui Imposta Ipotecaria",
            "OutCatastale" : "Di cui Imposta Catastale",
            "OutIVA" : "IVA €",
            "OutPercMutuo" : "Percentuale Mutuo %",
            "OutSpeseTot" : "Spese Totali €",
            "OutGrunderwerbsteuer" : "Di cui Grunderwerbsteuer €",
            "OutGrundbuchkosten" : "Di cui Grundbuchkosten €",
            "OutNotarkosten" : "Di cui Notarkosten €",
            "OutMaklergebühren" : "Di cui Maklergebühren €",

        }
    else:
        Dictionary = {
            "UserFinanziamento" : "Financing Amount",
            "UserAnniCalcMutuo" : "N° of Years for Calculation",
            "UserInTasso" : "Interest Rate",
            "UserInAnniTotTasso" : "Fixed-term Duration",
            "UserInRata" : "Installment",
            "UserInMaxiRataAnnuale" : "Yearly Lump Payment",
            "UserInMeseMaxiRata" : "N° of Months before the Lump Sum",
            "UserInAmmortamento" : "Amortization Rate",
            "UserInPrezzo" : "Buying Price",
            "UserInPercMutuo" : "Loan-to-Value Ratio",
            "UserInPercAgenzia" : "Real Estate Agent Fees",
            "UserInIstruttoria" : "Processing Fees",
            "UserInAssicurazione" : "Insurance Fees",
            "UserInPerizia" : "Valuation Fees",
            "UserInGrunderwerbsteuer" : "Grunderwerbsteuer",
            "UserInGrundbuchkosten" : "Grundbuchkosten",
            "UserInNotarkosten" : "Notarkosten",
            "UserInMaklergebühren" : "Maklergebühren",
            "UserInTipAcquisto" : "Purchase Type",
            "UserInBundesland" : "Bundesland",
            "OutNRata" : "N° Payment",
            "OutAnno" : "Year",
            "OutRata" : "Installment €",
            "OutCapitale" : "Principal €",
            "OutInteresse" : "Interests €",
            "OutTotCapResiduo" : "Residual Principal €",
            "OutTotIntPagati" : "Payed Interests €",
            "OutCapMedioAnnuo" : "Avg. Annual Principal €",
            "OutIntMedioAnnuo" : "Avg. Annual Interests €",
            "OutAnni" : "Years",
            "OutCapMedio" : "Avg. Principal €",
            "OutIntMedio" : "Avg. Interests €",
            "OutFinanziamento" : "Financing Amount €",
            "OutAnniTassoFisso" : "Fixed-term Duration",
            "OutTasso" : "Interest Rate %",
            "OutAmmortamento" : "Amortization Rate %",
            "OutMaxiRataAnnuale" : "Yearly Lump Payment €",
            "OutTotMaxiRata" : "Tot. Lump Sum Payments €",
            "OutAnticipo" : "Down Payment",
            "OutSpese" : "Purchasing fees",
            "OutUsciteTot" : "Initial Tot. Expenses",
            "OutPrezzo" : "Buying Price €",
            "OutTipo" : "Purchase Type",
            "OutAgenzia" : "Real Estate Agency Fees €",
            "OutIstruttoria" : "Processing Fees €",
            "OutSostitutiva" : "Replacement Tax €",
            "OutPerizia" : "Valuation Fees €",
            "OutAssicurazioni" : "Insurance Fees €",
            "OutNotaio" : "Notary Fees €",
            "OutRegistro" : "Of which Registration Tax",
            "OutIpotecaria" : "Of which Mortgage Tax",
            "OutCatastale" : "Of which Cadastral Tax",
            "OutIVA" : "IVA €",
            "OutPercMutuo" : "Loan-to-Value Ratio %",
            "OutSpeseTot" : "Total Fees €",
            "OutGrunderwerbsteuer" : "Of which Grunderwerbsteuer €",
            "OutGrundbuchkosten" : "Of which Grundbuchkosten €",
            "OutNotarkosten" : "Of which Notarkosten €",
            "OutMaklergebühren" : "Of which Maklergebühren €",
        }

    return Dictionary

def CalcolaMutuoAnniCalcAPI(UserData) :
    
    for key in UserData:
        UserData[key] = UserData[key].strip("€")
        UserData[key] = UserData[key].strip("%")
        UserData[key] = UserData[key].replace(",","")

    Dictionary = LanguageDict(UserData)

    TotFinanziamento = float(UserData[Dictionary["UserFinanziamento"]])
    In_AnniTotCalc = int(UserData[Dictionary["UserAnniCalcMutuo"]])
    RateTotali = int(In_AnniTotCalc*12)
    In_Tasso = float(UserData[Dictionary["UserInTasso"]])
    TassoTot = float(In_Tasso/100)
    In_AnniTotTasso = int(UserData[Dictionary["UserInAnniTotTasso"]])
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
            if In_AnniTotTasso>10:
                CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[11:In_AnniTotTasso]))
                InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[11:In_AnniTotTasso]))
                AnniMediaTot.append("11-" + UserData[Dictionary["UserInAnniTotTasso"]])

    Tilgung = float((Rata[1]-TassoTot*TotFinanziamento/12)*12/TotFinanziamento)
    MaxiRataFinale = float(TotCapRimanente[RataFinale])
    TotInteressiFinale = float(TotInteressi[RataFinale])

    NumRata = NumRata[0:In_AnniTotTasso*12+1]
    AnniRata = AnniRata[0:In_AnniTotTasso*12+1]
    Rata = Rata[0:In_AnniTotTasso*12+1]
    CapitalePerRata = CapitalePerRata[0:In_AnniTotTasso*12+1]
    InteressePerRata = InteressePerRata[0:In_AnniTotTasso*12+1]
    TotCapRimanente = TotCapRimanente[0:In_AnniTotTasso*12+1]
    TotInteressi = TotInteressi[0:In_AnniTotTasso*12+1]

    AnniRataAnnuo = AnniRataAnnuo[0:In_AnniTotTasso+1]
    CapitaleMedioAnnuo = CapitaleMedioAnnuo[0:In_AnniTotTasso+1]
    InteresseMedioAnnuo = InteresseMedioAnnuo[0:In_AnniTotTasso+1]
    TotCapRimanenteAnnuo = TotCapRimanenteAnnuo[0:In_AnniTotTasso+1]
    TotInteressiAnnuo = TotInteressiAnnuo[0:In_AnniTotTasso+1]


    OutputsMutuo = pd.DataFrame(list(zip(NumRata, AnniRata, Rata, CapitalePerRata, InteressePerRata, TotCapRimanente, TotInteressi)),
        columns =[Dictionary["OutNRata"], Dictionary["OutAnno"], Dictionary["OutRata"], Dictionary["OutCapitale"], Dictionary["OutInteresse"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"] ])
            
    OutputsMutuo = OutputsMutuo.round(1)

    OutputsAnnuoMutuo = pd.DataFrame(list(zip(AnniRataAnnuo, CapitaleMedioAnnuo, InteresseMedioAnnuo, TotCapRimanenteAnnuo, TotInteressiAnnuo)),
        columns =[Dictionary["OutAnno"], Dictionary["OutCapMedioAnnuo"], Dictionary["OutIntMedioAnnuo"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"]])

    OutputsAnnuoMutuo = OutputsAnnuoMutuo.round(1)

    OutputAvgMutuo = pd.DataFrame(list(zip(AnniMediaTot, CapitaleMedioAnniTot, InteresseMedioAnniTot)),
        columns =[Dictionary["OutAnni"], Dictionary["OutCapMedio"], Dictionary["OutIntMedio"]])
    
    OutputAvgMutuo = OutputAvgMutuo.round(1)

    OVdata = {
        Dictionary["OutFinanziamento"] : round(TotFinanziamento,0),
        Dictionary["OutAnniTassoFisso"] : In_AnniTotTasso,
        Dictionary["OutTasso"] : round(TassoTot*100,2),
        Dictionary["OutAmmortamento"] : round(Tilgung*100,2),
        Dictionary["OutRata"] : round(Rata[1],1),
        Dictionary["OutTotCapResiduo"] : round(MaxiRataFinale,0),
        Dictionary["OutTotIntPagati"] : round(TotInteressiFinale,0),

    }

    TotFinanziamentoList = [Dictionary["OutFinanziamento"] , round(TotFinanziamento,0)]
    In_AnniTotTassoList = [Dictionary["UserInAnniTotTasso"] , In_AnniTotTasso]
    TassoTotList = [Dictionary["OutTasso"] , round(TassoTot*100,2)]
    TilgungList = [Dictionary["OutAmmortamento"] , round(Tilgung*100,2)]
    RataList = [Dictionary["OutRata"], round(Rata[1],1)]
    MaxiRataFinaleList = [Dictionary["OutTotCapResiduo"] , round(MaxiRataFinale,0)]
    TotInteressiFinaleList = [Dictionary["OutTotIntPagati"] , round(TotInteressiFinale,0)]


    OutputOverviewMutuo = pd.DataFrame(list(zip(TotFinanziamentoList, In_AnniTotTassoList, TassoTotList, TilgungList, RataList, MaxiRataFinaleList, TotInteressiFinaleList )),
        columns =[Dictionary["OutFinanziamento"], Dictionary["UserInAnniTotTasso"], Dictionary["OutTasso"], Dictionary["OutAmmortamento"], Dictionary["OutCapitale"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"] ])

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

    Dictionary = LanguageDict(UserData)

    TotFinanziamento = float(UserData[Dictionary["UserFinanziamento"]])
    In_Rata = float(UserData[Dictionary["UserInRata"]])
    In_Tasso = float(UserData[Dictionary["UserInTasso"]])
    TassoTot = float(In_Tasso/100)
    In_AnniTotTasso = int(UserData[Dictionary["UserInAnniTotTasso"]])
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

    AnniTot = 0

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
            
            if CapitalePerRata[idx]<0:
                return -1

            AnniRata[idx] = int((idx-1)/12)+1
            
            if (AnniRata[idx]> AnniRata[idx-1] and AnniRata[idx-1]>0) or (idx == RateTotali) :
                RataMediaAnnua[AnniRata[idx-1]] = np.mean(Rata[idx-11:idx+1])
                CapitaleMedioAnnuo[AnniRata[idx-1]] = np.mean(CapitalePerRata[idx-11:idx+1]) 
                InteresseMedioAnnuo[AnniRata[idx-1]] = np.mean(InteressePerRata[idx-11:idx+1])
                TotCapRimanenteAnnuo[AnniRata[idx-1]] = TotCapRimanente[idx]
                TotInteressiAnnuo[AnniRata[idx-1]] = TotInteressi[idx]
                AnniRataAnnuo[AnniRata[idx-1]] = AnniRata[idx-1]

            if TotCapRimanente[idx]<=0:
                TotCapRimanente[idx] = 0
                RataFinale = idx
                RateTotali = idx
                AnniTot = int(idx/12)
                break

            if CapitalePerRata[idx]<=0:
                break

            if InteressePerRata[idx]>Rata[idx]:
                break

    if AnniTot != 0:
        AnniTotCalc = AnniTot   
    else: AnniTotCalc = In_AnniTotCalc 

    # if AnniTotCalc>=5:
    if AnniRata[idx-1] >=5:
        CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[1:5]))
        InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[1:5]))
        AnniMediaTot.append("1-5")
        # if AnniTotCalc>=10:
        if AnniRata[idx-1] >=10:
            CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[1:10]))
            InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[1:10]))
            AnniMediaTot.append("1-10")
            # if AnniTotCalc>10:
            if AnniRata[idx-1] >10:
                CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[11:AnniTotCalc]))
                InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[11:AnniTotCalc]))
                AnniMediaTot.append("11-" + UserData[Dictionary["UserInAnniTotTasso"]] )

    Tilgung = float((Rata[1]-TassoTot*TotFinanziamento/12)*12/TotFinanziamento)
    MaxiRataFinale = float(TotCapRimanente[RataFinale])
    TotInteressiFinale = float(TotInteressi[RataFinale])

    NumRata = NumRata[0:RataFinale+1]
    AnniRata = AnniRata[0:RataFinale+1]
    Rata = Rata[0:RataFinale+1]
    CapitalePerRata = CapitalePerRata[0:RataFinale+1]
    InteressePerRata = InteressePerRata[0:RataFinale+1]
    TotCapRimanente = TotCapRimanente[0:RataFinale+1]
    TotInteressi = TotInteressi[0:RataFinale+1]

    AnniRataAnnuo = AnniRataAnnuo[0:AnniTotCalc+1]
    CapitaleMedioAnnuo = CapitaleMedioAnnuo[0:AnniTotCalc+1]
    InteresseMedioAnnuo = InteresseMedioAnnuo[0:AnniTotCalc+1]
    TotCapRimanenteAnnuo = TotCapRimanenteAnnuo[0:AnniTotCalc+1]
    TotInteressiAnnuo = TotInteressiAnnuo[0:AnniTotCalc+1]

    OutputsMutuo = pd.DataFrame(list(zip(NumRata, AnniRata, Rata, CapitalePerRata, InteressePerRata, TotCapRimanente, TotInteressi)),
        columns =[Dictionary["OutNRata"], Dictionary["OutAnno"], Dictionary["OutRata"], Dictionary["OutCapitale"], Dictionary["OutInteresse"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"] ])
            
    OutputsMutuo = OutputsMutuo.round(1)

    OutputsAnnuoMutuo = pd.DataFrame(list(zip(AnniRataAnnuo, CapitaleMedioAnnuo, InteresseMedioAnnuo, TotCapRimanenteAnnuo, TotInteressiAnnuo)),
        columns =[Dictionary["OutAnno"], Dictionary["OutCapMedioAnnuo"], Dictionary["OutIntMedioAnnuo"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"]])

    OutputsAnnuoMutuo = OutputsAnnuoMutuo.round(1)

    OutputAvgMutuo = pd.DataFrame(list(zip(AnniMediaTot, CapitaleMedioAnniTot, InteresseMedioAnniTot)),
        columns =[Dictionary["OutAnni"], Dictionary["OutCapMedio"], Dictionary["OutIntMedio"]])

    OutputAvgMutuo = OutputAvgMutuo.round(1)

    OVdata = {
        Dictionary["OutFinanziamento"] : round(TotFinanziamento,0),
        Dictionary["UserInAnniTotTasso"] : AnniTotCalc,
        Dictionary["OutTasso"] : round(TassoTot*100,2),
        Dictionary["OutAmmortamento"] : round(Tilgung*100,2),
        Dictionary["OutRata"] : round(Rata[1],1),
        Dictionary["OutTotCapResiduo"] : round(MaxiRataFinale,0),
        Dictionary["OutTotIntPagati"] : round(TotInteressiFinale,0),

    }

    TotFinanziamentoList = [Dictionary["OutFinanziamento"] , round(TotFinanziamento,0)]
    In_AnniTotTassoList = [Dictionary["UserInAnniTotTasso"] , AnniTotCalc]
    TassoTotList = [Dictionary["OutTasso"] , round(TassoTot*100,2)]
    TilgungList = [Dictionary["OutAmmortamento"] , round(Tilgung*100,2)]
    RataList = [Dictionary["OutRata"], round(Rata[1],1)]
    MaxiRataFinaleList = [Dictionary["OutTotCapResiduo"] , round(MaxiRataFinale,0)]
    TotInteressiFinaleList = [Dictionary["OutTotIntPagati"] , round(TotInteressiFinale,0)]


    OutputOverviewMutuo = pd.DataFrame(list(zip(TotFinanziamentoList, In_AnniTotTassoList, TassoTotList, TilgungList, RataList, MaxiRataFinaleList, TotInteressiFinaleList )),
        columns =[Dictionary["OutFinanziamento"], Dictionary["UserInAnniTotTasso"], Dictionary["OutTasso"], Dictionary["OutAmmortamento"], Dictionary["OutCapitale"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"] ])

    OutputOverviewMutuo2 = pd.DataFrame(OVdata, index=["Val"])
    OutputOverviewMutuo = OutputOverviewMutuo.T
    # OutputOverviewMutuo = OutputOverviewMutuo.round(1)    
    dummy=1
    return OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo

def CalcolaMutuoRimborsoCapAPI(UserData) :

    for key in UserData:
        UserData[key] = UserData[key].strip("€")
        UserData[key] = UserData[key].strip("%")
        UserData[key] = UserData[key].replace(",","")

    Dictionary = LanguageDict(UserData)

    TotFinanziamento = float(UserData[Dictionary["UserFinanziamento"]])
    In_Tilgung = float(UserData[Dictionary["UserInAmmortamento"]])
    In_Tasso = float(UserData[Dictionary["UserInTasso"]])
    TassoTot = float(In_Tasso/100)
    In_AnniTotTasso = int(UserData[Dictionary["UserInAnniTotTasso"]])
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
                InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[11:In_AnniTotTasso]))
                AnniMediaTot.append("11-" + UserData[Dictionary["UserInAnniTotTasso"]] )


    MaxiRataFinale = float(TotCapRimanente[RataFinale])
    TotInteressiFinale = float(TotInteressi[RataFinale])


    OutputsMutuo = pd.DataFrame(list(zip(NumRata, AnniRata, Rata, CapitalePerRata, InteressePerRata, TotCapRimanente, TotInteressi)),
        columns =[Dictionary["OutNRata"], Dictionary["OutAnno"], Dictionary["OutRata"], Dictionary["OutCapitale"], Dictionary["OutInteresse"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"] ])
            
    OutputsMutuo = OutputsMutuo.round(1)

    OutputsAnnuoMutuo = pd.DataFrame(list(zip(AnniRataAnnuo, CapitaleMedioAnnuo, InteresseMedioAnnuo, TotCapRimanenteAnnuo, TotInteressiAnnuo)),
        columns =[Dictionary["OutAnno"], Dictionary["OutCapMedioAnnuo"], Dictionary["OutIntMedioAnnuo"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"]])

    OutputsAnnuoMutuo = OutputsAnnuoMutuo.round(1)

    OutputAvgMutuo = pd.DataFrame(list(zip(AnniMediaTot, CapitaleMedioAnniTot, InteresseMedioAnniTot)),
        columns =[Dictionary["OutAnni"], Dictionary["OutCapMedio"], Dictionary["OutIntMedio"]])

    OutputAvgMutuo = OutputAvgMutuo.round(1)

    OVdata = {
        Dictionary["OutFinanziamento"] : round(TotFinanziamento,0),
        Dictionary["UserInAnniTotTasso"] : In_AnniTotTasso,
        Dictionary["OutTasso"] : round(TassoTot*100,2),
        Dictionary["OutAmmortamento"] : round(In_Tilgung,2),
        Dictionary["OutRata"] : round(Rata[1],1),
        Dictionary["OutTotCapResiduo"] : round(MaxiRataFinale,0),
        Dictionary["OutTotIntPagati"] : round(TotInteressiFinale,0),
    }

    TotFinanziamentoList = [Dictionary["OutFinanziamento"] , round(TotFinanziamento,0)]
    In_AnniTotTassoList = [Dictionary["UserInAnniTotTasso"] , In_AnniTotTasso]
    TassoTotList = [Dictionary["OutTasso"] , round(TassoTot*100,2)]
    TilgungList = [Dictionary["OutAmmortamento"] , round(In_Tilgung,2)]
    RataList = [Dictionary["OutRata"], round(Rata[1],1)]
    MaxiRataFinaleList = [Dictionary["OutTotCapResiduo"] , round(MaxiRataFinale,0)]
    TotInteressiFinaleList = [Dictionary["OutTotIntPagati"] , round(TotInteressiFinale,0)]


    OutputOverviewMutuo = pd.DataFrame(list(zip(TotFinanziamentoList, In_AnniTotTassoList, TassoTotList, TilgungList, RataList, MaxiRataFinaleList, TotInteressiFinaleList )),
        columns =[Dictionary["OutFinanziamento"], Dictionary["UserInAnniTotTasso"], Dictionary["OutTasso"], Dictionary["OutAmmortamento"], Dictionary["OutCapitale"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"] ])

    OutputOverviewMutuo2 = pd.DataFrame(OVdata, index=["Val"])
    OutputOverviewMutuo = OutputOverviewMutuo.T
    # OutputOverviewMutuo = OutputOverviewMutuo.round(1)    
    dummy=1
    return OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo

def CalcolaMutuoAnniCalcAPIDE(UserData) :
    
    for key in UserData:
        UserData[key] = UserData[key].strip("€")
        UserData[key] = UserData[key].strip("%")
        UserData[key] = UserData[key].replace(",","")

    Dictionary = LanguageDict(UserData)

    TotFinanziamento = float(UserData[Dictionary["UserFinanziamento"]])
    In_AnniTotCalc = int(UserData[Dictionary["UserAnniCalcMutuo"]])
    RateTotali = int(In_AnniTotCalc*12)
    In_Tasso = float(UserData[Dictionary["UserInTasso"]])
    TassoTot = float(In_Tasso/100)
    In_AnniTotTasso = int(UserData[Dictionary["UserInAnniTotTasso"]])
    RataFinale = int(In_AnniTotTasso*12)
    In_MaxiRata = float(UserData[Dictionary["UserInMaxiRataAnnuale"]])
    In_MesiPreMaxiRata = int(UserData[Dictionary["UserInMeseMaxiRata"]])
    
    # Inizializza liste
    NumRata = [i for i in range(0,RateTotali+1)]
    AnniRata = ["" for i in range(0,RateTotali+1)]
    Rata = ["" for i in range(0,RateTotali+1)]
    InteressePerRata = ["" for i in range(0,RateTotali+1)]
    CapitalePerRata = ["" for i in range(0,RateTotali+1)]
    MaxiRataAnnuale = ["" for i in range(0,RateTotali+1)]
    TotCapRimanente = ["" for i in range(0,RateTotali+1)]
    TotInteressi = ["" for i in range(0,RateTotali+1)]
    TotMaxiRataAnnuale = ["" for i in range(0,RateTotali+1)]
    #  In_AnniTotTasso vs In_AnniTotCalc
    RataMediaAnnua = ["" for i in range(0,In_AnniTotCalc+1)]
    CapitaleMedioAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    InteresseMedioAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    TotCapRimanenteAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    TotInteressiAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    AnniRataAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    MaxiRataAnnualeAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]

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
            MaxiRataAnnuale[idx] = 0
            TotCapRimanente[idx] = TotFinanziamento
            TotInteressi[idx] = 0
            TotMaxiRataAnnuale[idx] = 0
            RataMediaAnnua[idx] = 0

            RataMediaAnnua[idx] = Rata[idx]
            CapitaleMedioAnnuo[idx] = CapitalePerRata[idx]
            InteresseMedioAnnuo[idx] = InteressePerRata[idx]
            TotCapRimanenteAnnuo[idx] = TotCapRimanente[idx]
            TotInteressiAnnuo[idx] = TotInteressi[idx]
            AnniRataAnnuo[idx] = AnniRata[idx]
            MaxiRataAnnualeAnnuo[idx] = MaxiRataAnnuale[idx]
        else:

            AnniRata[idx] = int((idx-1)/12)+1

            if (idx == In_MesiPreMaxiRata) or (idx == (AnniRata[idx]-1)*12 + In_MesiPreMaxiRata):
                # TotCapRimanente[idx] = float(TotCapRimanente[idx-1])-In_MaxiRata
                MaxiRataAnnuale[idx] = In_MaxiRata
                TotMaxiRataAnnuale[idx] = In_MaxiRata
                # print("here MaxiRata is =!0 ---------------------------------------------")
                if idx>12:
                    TotMaxiRataAnnuale[idx] = TotMaxiRataAnnuale[idx-12] + In_MaxiRata                    
            else:
                MaxiRataAnnuale[idx] = 0
                TotMaxiRataAnnuale[idx] =  TotMaxiRataAnnuale[idx-1]

            Rata[idx] = (TotFinanziamento*TassoTot/12)/(1-(1/(1+TassoTot/12)**(RateTotali)))
            InteressePerRata[idx] = (TotCapRimanente[idx-1]-MaxiRataAnnuale[idx])*TassoTot/12
            CapitalePerRata[idx] = Rata[idx]-InteressePerRata[idx]
            TotCapRimanente[idx] = TotCapRimanente[idx-1]-MaxiRataAnnuale[idx]-CapitalePerRata[idx]
            TotInteressi[idx] = TotInteressi[idx-1]+InteressePerRata[idx]
            
            if (AnniRata[idx]> AnniRata[idx-1] and AnniRata[idx-1]>0) or (idx == RateTotali) :
                RataMediaAnnua[AnniRata[idx-1]] = np.mean(Rata[idx-11:idx+1])
                CapitaleMedioAnnuo[AnniRata[idx-1]] = np.mean(CapitalePerRata[idx-11:idx+1]) 
                InteresseMedioAnnuo[AnniRata[idx-1]] = np.mean(InteressePerRata[idx-11:idx+1])
                TotCapRimanenteAnnuo[AnniRata[idx-1]] = TotCapRimanente[idx]
                TotInteressiAnnuo[AnniRata[idx-1]] = TotInteressi[idx]
                AnniRataAnnuo[AnniRata[idx-1]] = AnniRata[idx-1]
                MaxiRataAnnualeAnnuo[AnniRata[idx-1]] = In_MaxiRata

    
    if In_AnniTotCalc>=5:
        CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[1:5]))
        InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[1:5]))
        AnniMediaTot.append("1-5")
        if In_AnniTotCalc>=10:
            CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[1:10]))
            InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[1:10]))
            AnniMediaTot.append("1-10")
            if In_AnniTotTasso>10:
                CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[11:In_AnniTotTasso]))
                InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[11:In_AnniTotTasso]))
                AnniMediaTot.append("11-" + UserData[Dictionary["UserInAnniTotTasso"]] )

    Tilgung = float((Rata[1]-TassoTot*TotFinanziamento/12)*12/TotFinanziamento)
    MaxiRataFinale = float(TotCapRimanente[RataFinale])
    TotMaxiRataAnnualeFinale = float(TotMaxiRataAnnuale[RataFinale])
    TotInteressiFinale = float(TotInteressi[RataFinale])

    NumRata = NumRata[0:In_AnniTotTasso*12+1]
    AnniRata = AnniRata[0:In_AnniTotTasso*12+1]
    Rata = Rata[0:In_AnniTotTasso*12+1]
    CapitalePerRata = CapitalePerRata[0:In_AnniTotTasso*12+1]
    InteressePerRata = InteressePerRata[0:In_AnniTotTasso*12+1]
    TotCapRimanente = TotCapRimanente[0:In_AnniTotTasso*12+1]
    TotInteressi = TotInteressi[0:In_AnniTotTasso*12+1]
    MaxiRataAnnuale = MaxiRataAnnuale[0:In_AnniTotTasso*12+1]

    AnniRataAnnuo = AnniRataAnnuo[0:In_AnniTotTasso+1]
    CapitaleMedioAnnuo = CapitaleMedioAnnuo[0:In_AnniTotTasso+1]
    InteresseMedioAnnuo = InteresseMedioAnnuo[0:In_AnniTotTasso+1]
    TotCapRimanenteAnnuo = TotCapRimanenteAnnuo[0:In_AnniTotTasso+1]
    TotInteressiAnnuo = TotInteressiAnnuo[0:In_AnniTotTasso+1]
    MaxiRataAnnualeAnnuo = MaxiRataAnnualeAnnuo[0:In_AnniTotTasso+1]


    OutputsMutuo = pd.DataFrame(list(zip(NumRata, AnniRata, Rata, CapitalePerRata, InteressePerRata, TotCapRimanente, TotInteressi, MaxiRataAnnuale)),
        columns =[Dictionary["OutNRata"], Dictionary["OutAnno"], Dictionary["OutRata"], Dictionary["OutCapitale"], Dictionary["OutInteresse"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"], Dictionary["OutMaxiRataAnnuale"] ])
            
    OutputsMutuo = OutputsMutuo.round(1)

    OutputsAnnuoMutuo = pd.DataFrame(list(zip(AnniRataAnnuo, CapitaleMedioAnnuo, InteresseMedioAnnuo, TotCapRimanenteAnnuo, TotInteressiAnnuo, MaxiRataAnnualeAnnuo)),
        columns =[Dictionary["OutAnno"], Dictionary["OutCapMedioAnnuo"], Dictionary["OutIntMedioAnnuo"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"], Dictionary["OutMaxiRataAnnuale"]])

    OutputsAnnuoMutuo = OutputsAnnuoMutuo.round(1)

    OutputAvgMutuo = pd.DataFrame(list(zip(AnniMediaTot, CapitaleMedioAnniTot, InteresseMedioAnniTot)),
        columns =[Dictionary["OutAnni"], Dictionary["OutCapMedio"], Dictionary["OutIntMedio"]])

    OutputAvgMutuo = OutputAvgMutuo.round(1)

    OVdata = {
        Dictionary["OutFinanziamento"] : round(TotFinanziamento,0),
        Dictionary["UserInAnniTotTasso"] : In_AnniTotTasso,
        Dictionary["OutTasso"] : round(TassoTot*100,2),
        Dictionary["OutAmmortamento"] : round(Tilgung*100,2),
        Dictionary["OutRata"] : round(Rata[1],1),
        Dictionary["OutMaxiRataAnnuale"] : round(In_MaxiRata,0),
        Dictionary["OutTotMaxiRata"] : round(TotMaxiRataAnnualeFinale,0),
        Dictionary["OutTotCapResiduo"] : round(MaxiRataFinale,0),
        Dictionary["OutTotIntPagati"] : round(TotInteressiFinale,0),
        
    }

    TotFinanziamentoList = [Dictionary["OutFinanziamento"] , round(TotFinanziamento,0)]
    In_AnniTotTassoList = [Dictionary["UserInAnniTotTasso"] , In_AnniTotTasso]
    TassoTotList = [Dictionary["OutTasso"] , round(TassoTot*100,2)]
    TilgungList = [Dictionary["OutAmmortamento"] , round(Tilgung*100,2)]
    RataList = [Dictionary["OutRata"], round(Rata[1],1)]
    In_MaxiRataList = [Dictionary["OutMaxiRataAnnuale"] , round(In_MaxiRata,0)]
    TotMaxiRataAnnualeFinaleList = [Dictionary["OutTotMaxiRata"] , round(TotMaxiRataAnnualeFinale,0)]
    MaxiRataFinaleList = [Dictionary["OutTotCapResiduo"] , round(MaxiRataFinale,0)]
    TotInteressiFinaleList = [Dictionary["OutTotIntPagati"] , round(TotInteressiFinale,0)]


    OutputOverviewMutuo = pd.DataFrame(list(zip(TotFinanziamentoList, In_AnniTotTassoList, TassoTotList, TilgungList, RataList, In_MaxiRataList, TotMaxiRataAnnualeFinaleList, MaxiRataFinaleList, TotInteressiFinaleList )),
        columns =[Dictionary["OutFinanziamento"], Dictionary["UserInAnniTotTasso"], Dictionary["OutTasso"], Dictionary["OutAmmortamento"], Dictionary["OutCapitale"], Dictionary["OutMaxiRataAnnuale"], Dictionary["OutTotMaxiRata"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"] ])

    OutputOverviewMutuo2 = pd.DataFrame(OVdata, index=["Val"])
    OutputOverviewMutuo = OutputOverviewMutuo.T
    # OutputOverviewMutuo = OutputOverviewMutuo.round(1)    
    dummy=1
    return OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo

def CalcolaMutuoRataFissaAPIDE(UserData) :
    
    for key in UserData:
        UserData[key] = UserData[key].strip("€")
        UserData[key] = UserData[key].strip("%")
        UserData[key] = UserData[key].replace(",","")

    Dictionary = LanguageDict(UserData)

    TotFinanziamento = float(UserData[Dictionary["UserFinanziamento"]])
    In_Rata = float(UserData[Dictionary["UserInRata"]])
    In_Tasso = float(UserData[Dictionary["UserInTasso"]])
    TassoTot = float(In_Tasso/100)
    In_AnniTotTasso = int(UserData[Dictionary["UserInAnniTotTasso"]])
    In_AnniTotCalc = In_AnniTotTasso
    RateTotali = int(In_AnniTotCalc*12)
    RataFinale = int(In_AnniTotTasso*12)
    In_MaxiRata = float(UserData[Dictionary["UserInMaxiRataAnnuale"]])
    In_MesiPreMaxiRata = int(UserData[Dictionary["UserInMeseMaxiRata"]])

    # Inizializza liste
    NumRata = [i for i in range(0,RateTotali+1)]
    AnniRata = ["" for i in range(0,RateTotali+1)]
    Rata = ["" for i in range(0,RateTotali+1)]
    InteressePerRata = ["" for i in range(0,RateTotali+1)]
    CapitalePerRata = ["" for i in range(0,RateTotali+1)]
    MaxiRataAnnuale = ["" for i in range(0,RateTotali+1)]
    TotCapRimanente = ["" for i in range(0,RateTotali+1)]
    TotInteressi = ["" for i in range(0,RateTotali+1)]
    TotMaxiRataAnnuale = ["" for i in range(0,RateTotali+1)]

    RataMediaAnnua = ["" for i in range(0,In_AnniTotCalc+1)]
    CapitaleMedioAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    InteresseMedioAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    TotCapRimanenteAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    TotInteressiAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    AnniRataAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    MaxiRataAnnualeAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]

    AnniMediaTot = []
    CapitaleMedioAnniTot  = []
    InteresseMedioAnniTot  = []

    TotFinanziamentoList = []
    In_AnniTotTassoList = []

    AnniTot = 0

    for idx in range(0, RateTotali+1):
        if idx == 0 :
            Rata[idx] = 0
            AnniRata[idx] = 0
            InteressePerRata[idx] = 0
            CapitalePerRata[idx] = 0
            MaxiRataAnnuale[idx] = 0
            TotCapRimanente[idx] = TotFinanziamento
            TotInteressi[idx] = 0
            TotMaxiRataAnnuale[idx] = 0
            RataMediaAnnua[idx] = 0

            if CapitalePerRata[idx]<0:
                return -1
            
            RataMediaAnnua[idx] = Rata[idx]
            CapitaleMedioAnnuo[idx] = CapitalePerRata[idx]
            InteresseMedioAnnuo[idx] = InteressePerRata[idx]
            TotCapRimanenteAnnuo[idx] = TotCapRimanente[idx]
            TotInteressiAnnuo[idx] = TotInteressi[idx]
            AnniRataAnnuo[idx] = AnniRata[idx]
            MaxiRataAnnualeAnnuo[idx] = MaxiRataAnnuale[idx]
        else:
            AnniRata[idx] = int((idx-1)/12)+1

            if (idx == In_MesiPreMaxiRata) or (idx == (AnniRata[idx]-1)*12 + In_MesiPreMaxiRata):
                # TotCapRimanente[idx] = float(TotCapRimanente[idx-1])-In_MaxiRata
                MaxiRataAnnuale[idx] = In_MaxiRata
                TotMaxiRataAnnuale[idx] = In_MaxiRata
                # print("here MaxiRata is =!0 ---------------------------------------------")
                if idx>12:
                    TotMaxiRataAnnuale[idx] = TotMaxiRataAnnuale[idx-12] + In_MaxiRata                    
            else:
                MaxiRataAnnuale[idx] = 0
                TotMaxiRataAnnuale[idx] =  TotMaxiRataAnnuale[idx-1]


            Rata[idx] = In_Rata
            InteressePerRata[idx] = (TotCapRimanente[idx-1]-MaxiRataAnnuale[idx])*TassoTot/12
            CapitalePerRata[idx] = Rata[idx]-InteressePerRata[idx]
            TotCapRimanente[idx] = TotCapRimanente[idx-1]-MaxiRataAnnuale[idx]-CapitalePerRata[idx]
            TotInteressi[idx] = TotInteressi[idx-1]+InteressePerRata[idx]
            
            if (AnniRata[idx]> AnniRata[idx-1] and AnniRata[idx-1]>0) or (idx == RateTotali) :
                RataMediaAnnua[AnniRata[idx-1]] = np.mean(Rata[idx-11:idx+1])
                CapitaleMedioAnnuo[AnniRata[idx-1]] = np.mean(CapitalePerRata[idx-11:idx+1]) 
                InteresseMedioAnnuo[AnniRata[idx-1]] = np.mean(InteressePerRata[idx-11:idx+1])
                TotCapRimanenteAnnuo[AnniRata[idx-1]] = TotCapRimanente[idx]
                TotInteressiAnnuo[AnniRata[idx-1]] = TotInteressi[idx]
                AnniRataAnnuo[AnniRata[idx-1]] = AnniRata[idx-1]
                MaxiRataAnnualeAnnuo[AnniRata[idx-1]] = In_MaxiRata

            if TotCapRimanente[idx]<=0:
                TotCapRimanente[idx] = 0
                RataFinale = idx
                RateTotali = idx
                AnniTot = int(idx/12)
                break

            if CapitalePerRata[idx]<=0:
                break

            if InteressePerRata[idx]>Rata[idx]:
                break

    if AnniTot != 0:
        AnniTotCalc = AnniTot   
    else: AnniTotCalc = In_AnniTotCalc 

    # if AnniTotCalc>=5:
    if AnniRata[idx-1] >=5:
        CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[1:5]))
        InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[1:5]))
        AnniMediaTot.append("1-5")
        # if AnniTotCalc>=10:
        if AnniRata[idx-1] >=10:
            CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[1:10]))
            InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[1:10]))
            AnniMediaTot.append("1-10")
            # if AnniTotCalc>10:
            if AnniRata[idx-1] >10:
                CapitaleMedioAnniTot.append(np.mean(CapitaleMedioAnnuo[11:AnniTotCalc]))
                InteresseMedioAnniTot.append(np.mean(InteresseMedioAnnuo[11:AnniTotCalc]))
                AnniMediaTot.append("11-" + UserData[Dictionary["UserInAnniTotTasso"]] )
                
    Tilgung = float((Rata[1]-TassoTot*TotFinanziamento/12)*12/TotFinanziamento)
    MaxiRataFinale = float(TotCapRimanente[RataFinale])
    TotMaxiRataAnnualeFinale = float(TotMaxiRataAnnuale[RataFinale])
    TotInteressiFinale = float(TotInteressi[RataFinale])

    NumRata = NumRata[0:RataFinale+1]
    AnniRata = AnniRata[0:RataFinale+1]
    Rata = Rata[0:RataFinale+1]
    CapitalePerRata = CapitalePerRata[0:RataFinale+1]
    InteressePerRata = InteressePerRata[0:RataFinale+1]
    TotCapRimanente = TotCapRimanente[0:RataFinale+1]
    TotInteressi = TotInteressi[0:RataFinale+1]
    MaxiRataAnnuale = MaxiRataAnnuale[0:RataFinale+1]


    AnniRataAnnuo = AnniRataAnnuo[0:AnniTotCalc+1]
    CapitaleMedioAnnuo = CapitaleMedioAnnuo[0:AnniTotCalc+1]
    InteresseMedioAnnuo = InteresseMedioAnnuo[0:AnniTotCalc+1]
    TotCapRimanenteAnnuo = TotCapRimanenteAnnuo[0:AnniTotCalc+1]
    TotInteressiAnnuo = TotInteressiAnnuo[0:AnniTotCalc+1]
    MaxiRataAnnualeAnnuo = MaxiRataAnnualeAnnuo[0:AnniTotCalc+1]

    OutputsMutuo = pd.DataFrame(list(zip(NumRata, AnniRata, Rata, CapitalePerRata, InteressePerRata, TotCapRimanente, TotInteressi, MaxiRataAnnuale)),
        columns =[Dictionary["OutNRata"], Dictionary["OutAnno"], Dictionary["OutRata"], Dictionary["OutCapitale"], Dictionary["OutInteresse"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"], Dictionary["OutMaxiRataAnnuale"] ])
            
    OutputsMutuo = OutputsMutuo.round(1)

    OutputsAnnuoMutuo = pd.DataFrame(list(zip(AnniRataAnnuo, CapitaleMedioAnnuo, InteresseMedioAnnuo, TotCapRimanenteAnnuo, TotInteressiAnnuo, MaxiRataAnnualeAnnuo)),
        columns =[Dictionary["OutAnno"], Dictionary["OutCapMedioAnnuo"], Dictionary["OutIntMedioAnnuo"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"], Dictionary["OutMaxiRataAnnuale"]])

    OutputsAnnuoMutuo = OutputsAnnuoMutuo.round(1)

    OutputAvgMutuo = pd.DataFrame(list(zip(AnniMediaTot, CapitaleMedioAnniTot, InteresseMedioAnniTot)),
        columns =[Dictionary["OutAnni"], Dictionary["OutCapMedio"], Dictionary["OutIntMedio"]])

    OutputAvgMutuo = OutputAvgMutuo.round(1)

    OVdata = {
        Dictionary["OutFinanziamento"] : round(TotFinanziamento,0),
        Dictionary["UserInAnniTotTasso"] : In_AnniTotTasso,
        Dictionary["OutTasso"] : round(TassoTot*100,2),
        Dictionary["OutAmmortamento"] : round(Tilgung*100,2),
        Dictionary["OutRata"] : round(Rata[1],1),
        Dictionary["OutMaxiRataAnnuale"] : round(In_MaxiRata,0),
        Dictionary["OutTotMaxiRata"] : round(TotMaxiRataAnnualeFinale,0),
        Dictionary["OutTotCapResiduo"] : round(MaxiRataFinale,0),
        Dictionary["OutTotIntPagati"] : round(TotInteressiFinale,0),
        
    }

    TotFinanziamentoList = [Dictionary["OutFinanziamento"] , round(TotFinanziamento,0)]
    In_AnniTotTassoList = [Dictionary["UserInAnniTotTasso"] , In_AnniTotTasso]
    TassoTotList = [Dictionary["OutTasso"] , round(TassoTot*100,2)]
    TilgungList = [Dictionary["OutAmmortamento"] , round(Tilgung*100,2)]
    RataList = [Dictionary["OutRata"], round(Rata[1],1)]
    In_MaxiRataList = [Dictionary["OutMaxiRataAnnuale"] , round(In_MaxiRata,0)]
    TotMaxiRataAnnualeFinaleList = [Dictionary["OutTotMaxiRata"] , round(TotMaxiRataAnnualeFinale,0)]
    MaxiRataFinaleList = [Dictionary["OutTotCapResiduo"] , round(MaxiRataFinale,0)]
    TotInteressiFinaleList = [Dictionary["OutTotIntPagati"] , round(TotInteressiFinale,0)]


    OutputOverviewMutuo = pd.DataFrame(list(zip(TotFinanziamentoList, In_AnniTotTassoList, TassoTotList, TilgungList, RataList, In_MaxiRataList, TotMaxiRataAnnualeFinaleList, MaxiRataFinaleList, TotInteressiFinaleList )),
        columns =[Dictionary["OutFinanziamento"], Dictionary["UserInAnniTotTasso"], Dictionary["OutTasso"], Dictionary["OutAmmortamento"], Dictionary["OutCapitale"], Dictionary["OutMaxiRataAnnuale"], Dictionary["OutTotMaxiRata"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"] ])

    OutputOverviewMutuo2 = pd.DataFrame(OVdata, index=["Val"])
    OutputOverviewMutuo = OutputOverviewMutuo.T
    # OutputOverviewMutuo = OutputOverviewMutuo.round(1)    
    dummy=1
    return OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo

def CalcolaMutuoRimborsoCapAPIDE(UserData) :

    for key in UserData:
        UserData[key] = UserData[key].strip("€")
        UserData[key] = UserData[key].strip("%")
        UserData[key] = UserData[key].replace(",","")

    Dictionary = LanguageDict(UserData)

    TotFinanziamento = float(UserData[Dictionary["UserFinanziamento"]])
    In_Tilgung = float(UserData[Dictionary["UserInAmmortamento"]])
    In_Tasso = float(UserData[Dictionary["UserInTasso"]])
    TassoTot = float(In_Tasso/100)
    In_AnniTotTasso = int(UserData[Dictionary["UserInAnniTotTasso"]])
    In_AnniTotCalc = In_AnniTotTasso
    RateTotali = int(In_AnniTotCalc*12)
    RataFinale = int(In_AnniTotTasso*12)
    In_MaxiRata = float(UserData[Dictionary["UserInMaxiRataAnnuale"]])
    In_MesiPreMaxiRata = int(UserData[Dictionary["UserInMeseMaxiRata"]])
    # print("In_MaxiRata: ", In_MaxiRata)
    # print("In_MesiPreMaxiRata: ", In_MesiPreMaxiRata)

    # Inizializza liste
    NumRata = [i for i in range(0,RateTotali+1)]
    AnniRata = ["" for i in range(0,RateTotali+1)]
    Rata = ["" for i in range(0,RateTotali+1)]
    InteressePerRata = ["" for i in range(0,RateTotali+1)]
    CapitalePerRata = ["" for i in range(0,RateTotali+1)]
    MaxiRataAnnuale = ["" for i in range(0,RateTotali+1)]
    TotCapRimanente = ["" for i in range(0,RateTotali+1)]
    TotInteressi = ["" for i in range(0,RateTotali+1)]
    TotMaxiRataAnnuale = ["" for i in range(0,RateTotali+1)]

    RataMediaAnnua = ["" for i in range(0,In_AnniTotCalc+1)]
    CapitaleMedioAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    InteresseMedioAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    TotCapRimanenteAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    TotInteressiAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    AnniRataAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]
    MaxiRataAnnualeAnnuo = ["" for i in range(0,In_AnniTotCalc+1)]

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
            MaxiRataAnnuale[idx] = 0
            TotCapRimanente[idx] = TotFinanziamento
            TotInteressi[idx] = 0
            TotMaxiRataAnnuale[idx] = 0
            RataMediaAnnua[idx] = 0

            RataMediaAnnua[idx] = Rata[idx]
            CapitaleMedioAnnuo[idx] = CapitalePerRata[idx]
            InteresseMedioAnnuo[idx] = InteressePerRata[idx]
            TotCapRimanenteAnnuo[idx] = TotCapRimanente[idx]
            TotInteressiAnnuo[idx] = TotInteressi[idx]
            AnniRataAnnuo[idx] = AnniRata[idx]
            MaxiRataAnnualeAnnuo[idx] = MaxiRataAnnuale[idx]

        else:
            
            AnniRata[idx] = int((idx-1)/12)+1

            if (idx == In_MesiPreMaxiRata) or (idx == (AnniRata[idx]-1)*12 + In_MesiPreMaxiRata):
                # TotCapRimanente[idx] = float(TotCapRimanente[idx-1])-In_MaxiRata
                MaxiRataAnnuale[idx] = In_MaxiRata
                TotMaxiRataAnnuale[idx] = In_MaxiRata
                # print("here MaxiRata is =!0 ---------------------------------------------")
                if idx>12:
                    TotMaxiRataAnnuale[idx] = TotMaxiRataAnnuale[idx-12] + In_MaxiRata                    
            else:
                MaxiRataAnnuale[idx] = 0
                TotMaxiRataAnnuale[idx] =  TotMaxiRataAnnuale[idx-1]

            Rata[idx] = float((TotFinanziamento/12)*(In_Tilgung+In_Tasso)/100)
            InteressePerRata[idx] = (TotCapRimanente[idx-1]-MaxiRataAnnuale[idx])*TassoTot/12
            CapitalePerRata[idx] = Rata[idx]-InteressePerRata[idx]
            TotCapRimanente[idx] = TotCapRimanente[idx-1]-MaxiRataAnnuale[idx]-CapitalePerRata[idx]
            TotInteressi[idx] = TotInteressi[idx-1]+InteressePerRata[idx]

            # print("idx: ", idx)
            # print("In_MesiPreMaxiRata: ", In_MesiPreMaxiRata)
            # print("AnniRata[idx]: ", AnniRata[idx])
            # print("MaxiRataAnnuale: ", MaxiRataAnnuale)
            # print("MaxiRataAnnuale[idx]: ", MaxiRataAnnuale[idx])
            # print("TotCapRimanente[idx-1]: ", TotCapRimanente[idx-1])
            # print("InteressePerRata[idx]: ", InteressePerRata[idx])
            # print("TotCapRimanente[idx]: ", TotCapRimanente[idx])
            # print("TotMaxiRataAnnuale[idx]: ", TotMaxiRataAnnuale[idx])
            # print("TotInteressi[idx]: ", TotInteressi[idx])
            
            if (AnniRata[idx]> AnniRata[idx-1] and AnniRata[idx-1]>0) or (idx == RateTotali) :
                RataMediaAnnua[AnniRata[idx-1]] = np.mean(Rata[idx-11:idx+1])
                CapitaleMedioAnnuo[AnniRata[idx-1]] = np.mean(CapitalePerRata[idx-11:idx+1]) 
                InteresseMedioAnnuo[AnniRata[idx-1]] = np.mean(InteressePerRata[idx-11:idx+1])
                TotCapRimanenteAnnuo[AnniRata[idx-1]] = TotCapRimanente[idx]
                TotInteressiAnnuo[AnniRata[idx-1]] = TotInteressi[idx]
                AnniRataAnnuo[AnniRata[idx-1]] = AnniRata[idx-1]
                MaxiRataAnnualeAnnuo[AnniRata[idx-1]] = In_MaxiRata



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
                AnniMediaTot.append("11-" + UserData[Dictionary["UserInAnniTotTasso"]] )


    MaxiRataFinale = float(TotCapRimanente[RataFinale])
    TotMaxiRataAnnualeFinale = float(TotMaxiRataAnnuale[RataFinale])
    TotInteressiFinale = float(TotInteressi[RataFinale])

    OutputsMutuo = pd.DataFrame(list(zip(NumRata, AnniRata, Rata, CapitalePerRata, InteressePerRata, TotCapRimanente, TotInteressi, MaxiRataAnnuale)),
        columns =[Dictionary["OutNRata"], Dictionary["OutAnno"], Dictionary["OutRata"], Dictionary["OutCapitale"], Dictionary["OutInteresse"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"], Dictionary["OutMaxiRataAnnuale"] ])
            
    OutputsMutuo = OutputsMutuo.round(1)

    OutputsAnnuoMutuo = pd.DataFrame(list(zip(AnniRataAnnuo, CapitaleMedioAnnuo, InteresseMedioAnnuo, TotCapRimanenteAnnuo, TotInteressiAnnuo, MaxiRataAnnualeAnnuo)),
        columns =[Dictionary["OutAnno"], Dictionary["OutCapMedioAnnuo"], Dictionary["OutIntMedioAnnuo"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"], Dictionary["OutMaxiRataAnnuale"]])

    OutputsAnnuoMutuo = OutputsAnnuoMutuo.round(1)

    OutputAvgMutuo = pd.DataFrame(list(zip(AnniMediaTot, CapitaleMedioAnniTot, InteresseMedioAnniTot)),
        columns =[Dictionary["OutAnni"], Dictionary["OutCapMedio"], Dictionary["OutIntMedio"]])

    OutputAvgMutuo = OutputAvgMutuo.round(1)

    OVdata = {
        Dictionary["OutFinanziamento"] : round(TotFinanziamento,0),
        Dictionary["UserInAnniTotTasso"] : In_AnniTotTasso,
        Dictionary["OutTasso"] : round(TassoTot*100,2),
        Dictionary["OutAmmortamento"] : round(In_Tilgung,2),
        Dictionary["OutRata"] : round(Rata[1],1),
        Dictionary["OutMaxiRataAnnuale"] : round(In_MaxiRata,0),
        Dictionary["OutTotMaxiRata"] : round(TotMaxiRataAnnualeFinale,0),
        Dictionary["OutTotCapResiduo"] : round(MaxiRataFinale,0),
        Dictionary["OutTotIntPagati"] : round(TotInteressiFinale,0),
        
    }

    TotFinanziamentoList = [Dictionary["OutFinanziamento"] , round(TotFinanziamento,0)]
    In_AnniTotTassoList = [Dictionary["UserInAnniTotTasso"] , In_AnniTotTasso]
    TassoTotList = [Dictionary["OutTasso"] , round(TassoTot*100,2)]
    TilgungList = [Dictionary["OutAmmortamento"] , round(In_Tilgung,2)]
    RataList = [Dictionary["OutRata"], round(Rata[1],1)]
    In_MaxiRataList = [Dictionary["OutMaxiRataAnnuale"] , round(In_MaxiRata,0)]
    TotMaxiRataAnnualeFinaleList = [Dictionary["OutTotMaxiRata"] , round(TotMaxiRataAnnualeFinale,0)]
    MaxiRataFinaleList = [Dictionary["OutTotCapResiduo"] , round(MaxiRataFinale,0)]
    TotInteressiFinaleList = [Dictionary["OutTotIntPagati"] , round(TotInteressiFinale,0)]


    OutputOverviewMutuo = pd.DataFrame(list(zip(TotFinanziamentoList, In_AnniTotTassoList, TassoTotList, TilgungList, RataList, In_MaxiRataList, TotMaxiRataAnnualeFinaleList, MaxiRataFinaleList, TotInteressiFinaleList )),
        columns =[Dictionary["OutFinanziamento"], Dictionary["UserInAnniTotTasso"], Dictionary["OutTasso"], Dictionary["OutAmmortamento"], Dictionary["OutRata"], Dictionary["OutMaxiRataAnnuale"], Dictionary["OutTotMaxiRata"], Dictionary["OutTotCapResiduo"], Dictionary["OutTotIntPagati"] ])

    OutputOverviewMutuo2 = pd.DataFrame(OVdata, index=["Val"])
    OutputOverviewMutuo = OutputOverviewMutuo.T
    # OutputOverviewMutuo = OutputOverviewMutuo.round(1)    
    dummy=1
    return OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo


def CalcolaCashIniziale(UserData) :

    for key in UserData:
        UserData[key] = UserData[key].strip("€")
        UserData[key] = UserData[key].strip("%")
        UserData[key] = UserData[key].replace(",","")
    
    Dictionary = LanguageDict(UserData)
    if UserData["Language"] == "it":
        PrimaPrivateLbl = "Prima"
        SecondaPrivateLbl = "Seconda"
        PrivateLbl = "Privato"
        CostruttoreLbl = "Costruttore"
        LussoLbl = "Lusso"
    elif UserData["Language"] == "en":
        PrimaPrivateLbl = "1st"
        SecondaPrivateLbl = "2nd"
        PrivateLbl = "Private"
        CostruttoreLbl = "Developer"
        LussoLbl = "Luxury"

    Finanziamento = float(UserData[Dictionary["UserInPrezzo"]])*float(UserData[Dictionary["UserInPercMutuo"]])*0.01

    if float(UserData[Dictionary["UserInIstruttoria"]])>=0 and float(UserData[Dictionary["UserInIstruttoria"]])<=2:
        IstruttoriaType = "percentuale"
        Istruttoria = float(UserData[Dictionary["UserInIstruttoria"]])*0.01*(Finanziamento)
    elif float(UserData[Dictionary["UserInIstruttoria"]])>=50:
        IstruttoriaType = "fissa"
        Istruttoria = float(UserData[Dictionary["UserInIstruttoria"]])
    else:
        IstruttoriaType = "fissa"
        Istruttoria = 0.0

    
    if PrimaPrivateLbl in UserData[Dictionary["UserInTipAcquisto"]]:
        Sostitutiva = 0.25
        SpesaSostitutiva = Sostitutiva*Finanziamento*0.01
        if PrivateLbl in UserData[Dictionary["UserInTipAcquisto"]]:
            Registro = 2
            SpesaRegistro = Registro*0.01*float(UserData[Dictionary["UserInPrezzo"]])
            if SpesaRegistro <1000:
                SpesaRegistro = 1000
            SpesaIpotecaria = 50
            SpesaCatastale = 50
            IVA = 0
            SpesaIVA = IVA*float(UserData[Dictionary["UserInPrezzo"]])*0.01
        elif CostruttoreLbl in UserData[Dictionary["UserInTipAcquisto"]]:
            SpesaRegistro = 200
            SpesaIpotecaria = 200
            SpesaCatastale = 200
            IVA = 4
            SpesaIVA = IVA*float(UserData[Dictionary["UserInPrezzo"]])*0.01
    elif SecondaPrivateLbl in UserData[Dictionary["UserInTipAcquisto"]]:
        Sostitutiva = 2
        SpesaSostitutiva = Sostitutiva*Finanziamento*0.01
        if PrivateLbl in UserData[Dictionary["UserInTipAcquisto"]]:
            Registro = 9
            SpesaRegistro = Registro*0.01*float(UserData[Dictionary["UserInPrezzo"]])
            if SpesaRegistro <1000:
                SpesaRegistro = 1000
            SpesaIpotecaria = 50
            SpesaCatastale = 50
            IVA = 0
            SpesaIVA = IVA*float(UserData[Dictionary["UserInPrezzo"]])*0.01
        elif CostruttoreLbl in UserData[Dictionary["UserInTipAcquisto"]]:
            SpesaRegistro = 200
            SpesaIpotecaria = 200
            SpesaCatastale = 200
            if LussoLbl in UserData[Dictionary["UserInTipAcquisto"]]:
                IVA = 22
                SpesaIVA = IVA*float(UserData[Dictionary["UserInPrezzo"]])*0.01
            else:
                IVA = 10
                SpesaIVA = IVA*float(UserData[Dictionary["UserInPrezzo"]])*0.01


    SpeseIniziali = {
        "PrezzoImmobile €" : float(UserData[Dictionary["UserInPrezzo"]]),
        "TotFinanziamento €" : Finanziamento,
        "CostoAgenzia" : float(UserData[Dictionary["UserInPercAgenzia"]])*0.01*float(UserData[Dictionary["UserInPrezzo"]]),
        "CostoIstruttoria" : Istruttoria,
        "CostoSostitutiva" : SpesaSostitutiva,
        "CostoPerizia" : float(UserData[Dictionary["UserInPerizia"]]),
        "CostoAssicurazioni" : float(UserData[Dictionary["UserInAssicurazione"]]),
        "CostoNotaio" : SpesaRegistro + SpesaIpotecaria + SpesaCatastale,
        "CostoIVA" : SpesaIVA
    }

    SpeseIniziali["TotCosti"] = SpeseIniziali["CostoAgenzia"] + SpeseIniziali["CostoNotaio"] + SpeseIniziali["CostoIstruttoria"] + SpeseIniziali["CostoSostitutiva"] + SpeseIniziali["CostoPerizia"] + SpeseIniziali["CostoAssicurazioni"] + SpeseIniziali["CostoIVA"]
    SpeseIniziali["AnticipoMutuo"] = float(UserData[Dictionary["UserInPrezzo"]])-Finanziamento
    SpeseIniziali["SpesaTotIniziale"] = SpeseIniziali["TotCosti"] + SpeseIniziali["AnticipoMutuo"]
    
    PrezzoImmobileList = [Dictionary["OutPrezzo"] , round(SpeseIniziali["PrezzoImmobile €"],0)]
    TotFinanziamentoList = [Dictionary["OutFinanziamento"] , round(SpeseIniziali["TotFinanziamento €"],0)]
    CostoAgenziaList = [Dictionary["OutAgenzia"] , round(SpeseIniziali["CostoAgenzia"],0)]
    CostoIstruttoriaList = [Dictionary["OutIstruttoria"] , round(SpeseIniziali["CostoIstruttoria"],0)]
    CostoSostitutivaList = [Dictionary["OutSostitutiva"] , round(SpeseIniziali["CostoSostitutiva"],0)]
    CostoPeriziaList = [Dictionary["OutPerizia"] , round(SpeseIniziali["CostoPerizia"],0)]
    CostoAssicurazioniList = [Dictionary["OutAssicurazioni"] , round(SpeseIniziali["CostoAssicurazioni"],0)]
    CostoNotaioList = [Dictionary["OutNotaio"] , round(SpeseIniziali["CostoNotaio"],0)]
    CostoIVAList = [Dictionary["OutIVA"] , round(SpeseIniziali["CostoIVA"],0)]

    TipologiaAcquistoList = [Dictionary["OutTipo"], UserData[Dictionary["UserInTipAcquisto"]]]
    PercFinanziamentoList = [Dictionary["OutPercMutuo"], float(UserData[Dictionary["UserInPercMutuo"]])]
    ImpostaRegistroList = [Dictionary["OutRegistro"], SpesaRegistro]
    ImpostaIpotecariaList = [Dictionary["OutIpotecaria"], SpesaIpotecaria]
    ImpostaCatastaleList = [Dictionary["OutCatastale"], SpesaCatastale]




    OutputsSpeseInizialiDettaglio = pd.DataFrame(list(zip(PrezzoImmobileList, TipologiaAcquistoList, PercFinanziamentoList, TotFinanziamentoList, CostoAgenziaList, CostoIstruttoriaList, CostoSostitutivaList, CostoPeriziaList, CostoAssicurazioniList, CostoNotaioList, ImpostaRegistroList, ImpostaIpotecariaList, ImpostaCatastaleList, CostoIVAList )),
        columns =[Dictionary["OutPrezzo"], Dictionary["OutTipo"], Dictionary["UserInPercMutuo"], Dictionary["OutFinanziamento"], Dictionary["OutAgenzia"], Dictionary["OutIstruttoria"], Dictionary["OutSostitutiva"], Dictionary["OutPerizia"], Dictionary["OutAssicurazioni"], Dictionary["OutNotaio"], Dictionary["OutRegistro"], Dictionary["OutIpotecaria"], Dictionary["OutCatastale"], Dictionary["OutIVA"]])

    OutputsSpeseInizialiDettaglio = OutputsSpeseInizialiDettaglio.T

    OutputsSpeseIniziali= pd.DataFrame(data=SpeseIniziali, index=[0])
    OutputsSpeseIniziali.round(0)

    return OutputsSpeseIniziali, OutputsSpeseInizialiDettaglio

def CalcolaCashInizialeDE(UserData) :

    for key in UserData:
        UserData[key] = UserData[key].strip("€")
        UserData[key] = UserData[key].strip("%")
        UserData[key] = UserData[key].replace(",","")

    Dictionary = LanguageDict(UserData)

    Grunderwerbsteuer = float(UserData[Dictionary["UserInGrunderwerbsteuer"]])*0.01*float(UserData[Dictionary["UserInPrezzo"]])
    Grundbuchkosten = float(UserData[Dictionary["UserInGrundbuchkosten"]])*0.01*float(UserData[Dictionary["UserInPrezzo"]])
    Notarkosten = float(UserData[Dictionary["UserInNotarkosten"]])*0.01*float(UserData[Dictionary["UserInPrezzo"]])
    Maklergebueren = float(UserData[Dictionary["UserInMaklergebühren"]])*0.01*float(UserData[Dictionary["UserInPrezzo"]])

    SpeseIniziali = {
        "Bundesland" : UserData[Dictionary["UserInBundesland"]],
        "PrezzoImmobile" : float(UserData[Dictionary["UserInPrezzo"]]),
        "Grunderwerbsteuer" : Grunderwerbsteuer,
        "Grundbuchkosten" : Grundbuchkosten,
        "Notarkosten" : Notarkosten,
        "Maklergebueren" : Maklergebueren,
    }

    SpeseIniziali["TotCosti"] = SpeseIniziali["Grunderwerbsteuer"] + SpeseIniziali["Grundbuchkosten"] + SpeseIniziali["Notarkosten"] + SpeseIniziali["Maklergebueren"]
    
    RegioneList = [Dictionary["UserInBundesland"] , SpeseIniziali["Bundesland"]]
    PrezzoImmobileList = [Dictionary["OutPrezzo"] , round(SpeseIniziali["PrezzoImmobile"],0)]
    SpeseTotList = [Dictionary["OutSpeseTot"] , round(SpeseIniziali["TotCosti"],0)]
    GrunderwerbsteurList = [Dictionary["OutGrunderwerbsteuer"] , round(SpeseIniziali["Grunderwerbsteuer"],0)]
    GrundbuchkostenList = [Dictionary["OutGrundbuchkosten"] , round(SpeseIniziali["Grundbuchkosten"],0)]
    NotarkostenList = [Dictionary["OutNotarkosten"] , round(SpeseIniziali["Notarkosten"],0)]
    MaklergebuerenList = [Dictionary["OutMaklergebühren"] , round(SpeseIniziali["Maklergebueren"],0)]


    OutputsSpeseInizialiDettaglioDE = pd.DataFrame(list(zip(RegioneList, PrezzoImmobileList, SpeseTotList, GrunderwerbsteurList, GrundbuchkostenList, NotarkostenList, MaklergebuerenList)),
        columns =[Dictionary["UserInBundesland"], Dictionary["OutPrezzo"], Dictionary["OutSpeseTot"],Dictionary["OutGrunderwerbsteuer"], Dictionary["OutGrundbuchkosten"], Dictionary["OutNotarkosten"], Dictionary["OutMaklergebühren"]])

    OutputsSpeseInizialiDettaglioDE = OutputsSpeseInizialiDettaglioDE.T

    OutputsSpeseInizialiDE= pd.DataFrame(data=SpeseIniziali, index=[0])
    OutputsSpeseInizialiDE.round(0)

    return OutputsSpeseInizialiDE, OutputsSpeseInizialiDettaglioDE

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

    Dictionary = LanguageDict(UserData)

    code = UserData["Grafico"]
    pars = eurostat.get_pars(code)

    if code == "ilc_lvho02":
        title = "Distribution of population by tenure status, type of household and income group - EU-SILC survey"
        my_filter_pars = {"geo" : "IT", "hhtyp" : "TOTAL", "tenure" : "OWN", "incgrp" : "TOTAL", "startPeriod": 2011}
    elif code == "PRC_HPI_A":
        title = "House price index (2015 = 100) - annual data"
        my_filter_pars = {"geo" : "IT", "purchase" : "TOTAL", "unit": "RCH_A_AVG", "startPeriod": 2011}
    elif code == "ILC_MDES05":
        title = "Arrears (mortgage or rent, utility bills or hire purchase) from 2003 onwards - EU-SILC survey"
        my_filter_pars = {"geo" : "IT", "incgrp" : "TOTAL", "hhtyp": "TOTAL", "startPeriod": 2011}
    elif code == "ILC_MDED01":
        title = "Share of housing costs in disposable household income, by type of household and income group - EU-SILC survey"
        my_filter_pars = {"geo" : "IT", "hhtyp": "TOTAL", "incgrp": "TOTAL", "startPeriod": 2011}
    elif code == "PRC_HICP_MANR":
        title = "HICP - monthly data (annual rate of change)"
        my_filter_pars = {"geo" : "IT", "coicop": "CP00",  "startPeriod": "2011-01"}


    data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
    data_filter = data.iloc[:,len(pars):data.size]

    return data