from flask import Flask, request
from flask_restful import Api
import json

from MyFunctions import CalcolaCashIniziale, CalcolaCashInizialeDE, CalcolaMutuoAnniCalcAPI, CalcolaMutuoAnniCalcAPIDE, CalcolaMutuoRataFissaAPI, CalcolaMutuoRataFissaAPIDE, CalcolaMutuoRimborsoCapAPI, CalcolaMutuoRimborsoCapAPIDE, EurostatCall, LanguageDict

app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    return "Homepage"



@app.route("/outMutuo", methods = ["POST"])
def returnDataDetails():

    print("/outMutuo")
    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8")) 
    print(request_data)
    Dictionary = LanguageDict(request_data)
    if Dictionary["UserAnniCalcMutuo"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAnniCalcAPI(request_data)
    elif Dictionary["UserInRata"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRataFissaAPI(request_data)
    elif Dictionary["UserInAmmortamento"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRimborsoCapAPI(request_data)

    dummy=1
    ReturnData = OutputsMutuo.to_json()

    return ReturnData

@app.route("/outMutuoDE", methods = ["POST"])
def returnDataDetailsDE():

    print("/outMutuoDE")
    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8")) 
    print(request_data)
    Dictionary = LanguageDict(request_data)
    if Dictionary["UserAnniCalcMutuo"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAnniCalcAPIDE(request_data)
    elif Dictionary["UserInRata"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRataFissaAPIDE(request_data)
    elif Dictionary["UserInAmmortamento"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRimborsoCapAPIDE(request_data)

    dummy=1
    ReturnData = OutputsMutuo.to_json()

    return ReturnData

@app.route("/outMutuoAvg", methods = ["POST"])
def returnDataAnno():

    print("/outMutuoAvg")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    Dictionary = LanguageDict(request_data)
    if Dictionary["UserAnniCalcMutuo"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAnniCalcAPI(request_data)
    elif Dictionary["UserInRata"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRataFissaAPI(request_data)
    elif Dictionary["UserInAmmortamento"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRimborsoCapAPI(request_data)
    dummy=1
    ReturnData = OutputsAnnuoMutuo.to_json()

    return ReturnData

@app.route("/outMutuoAvgTot", methods = ["POST"])
def returnDataAvg():

    print("/outMutuoAvgTot")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    Dictionary = LanguageDict(request_data)
    if Dictionary["UserAnniCalcMutuo"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAnniCalcAPI(request_data)
    elif Dictionary["UserInRata"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRataFissaAPI(request_data)
    elif Dictionary["UserInAmmortamento"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRimborsoCapAPI(request_data)
    dummy=1
    ReturnData = OutputAvgMutuo.to_json()

    return ReturnData

@app.route("/outMutuoOverview", methods = ["POST"])
def returnDataOv():

    print("/outMutuoOverview")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    Dictionary = LanguageDict(request_data)
    if Dictionary["UserAnniCalcMutuo"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAnniCalcAPI(request_data)
    elif Dictionary["UserInRata"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRataFissaAPI(request_data)
    elif Dictionary["UserInAmmortamento"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRimborsoCapAPI(request_data)
    dummy=1
    ReturnData = OutputOverviewMutuo.to_json()

    return ReturnData

@app.route("/outMutuoAvgDE", methods = ["POST"])
def returnDataAnnoDE():

    print("/outMutuoAvgDE")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    Dictionary = LanguageDict(request_data)
    if Dictionary["UserAnniCalcMutuo"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAnniCalcAPIDE(request_data)
    elif Dictionary["UserInRata"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRataFissaAPIDE(request_data)
    elif Dictionary["UserInAmmortamento"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRimborsoCapAPIDE(request_data)
    dummy=1
    ReturnData = OutputsAnnuoMutuo.to_json()

    return ReturnData

@app.route("/outMutuoAvgTotDE", methods = ["POST"])
def returnDataAvgDE():

    print("/outMutuoAvgTotDE")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    Dictionary = LanguageDict(request_data)
    if Dictionary["UserAnniCalcMutuo"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAnniCalcAPIDE(request_data)
    elif Dictionary["UserInRata"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRataFissaAPIDE(request_data)
    elif Dictionary["UserInAmmortamento"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRimborsoCapAPIDE(request_data)
    dummy=1
    ReturnData = OutputAvgMutuo.to_json()

    return ReturnData

@app.route("/outMutuoOverviewDE", methods = ["POST"])
def returnDataOvDE():

    print("/outMutuoOverviewDE")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    Dictionary = LanguageDict(request_data)
    if Dictionary["UserAnniCalcMutuo"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAnniCalcAPIDE(request_data)
    elif Dictionary["UserInRata"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRataFissaAPIDE(request_data)
    elif Dictionary["UserInAmmortamento"] in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRimborsoCapAPIDE(request_data)
    dummy=1
    ReturnData = OutputOverviewMutuo.to_json()

    return ReturnData

@app.route("/outSpese", methods = ["POST"])
def returnDataSpesa():

    print("/outSpese")
    print("HERE")
    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    OutputsSpeseIniziali, OutputsSpeseInizialiDettaglio = CalcolaCashIniziale(request_data)
    ReturnData = OutputsSpeseIniziali.to_json()

    return ReturnData

@app.route("/outSpeseDE", methods = ["POST"])
def returnDataSpesaDE():

    print("/outSpeseDE")
    print("HERE")
    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    OutputsSpeseInizialiDE, OutputsSpeseInizialiDettaglioDE = CalcolaCashInizialeDE(request_data)
    ReturnData = OutputsSpeseInizialiDE.to_json()

    return ReturnData

@app.route("/outSpeseOverview", methods = ["POST"])
def returnDataSpesaDetails():

    print("/outSpeseOverview")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    OutputsSpeseIniziali, OutputsSpeseInizialiDettaglio = CalcolaCashIniziale(request_data)
    dummy=1
    ReturnData = OutputsSpeseInizialiDettaglio.to_json()

    return ReturnData

@app.route("/outSpeseOverviewDE", methods = ["POST"])
def returnDataSpesaDetailsDE():

    print("/outSpeseOverviewDE")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    OutputsSpeseInizialiDE, OutputsSpeseInizialiDettaglioDE = CalcolaCashInizialeDE(request_data)
    dummy=1
    ReturnData = OutputsSpeseInizialiDettaglioDE.to_json()

    return ReturnData

@app.route("/outGrafici", methods = ["POST"])
def returnDataGraphs():

    print("/outGrafici")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    OutputsGrafico = EurostatCall(request_data)
    dummy=1
    ReturnData = OutputsGrafico.to_json()

    return ReturnData

# Uncomment the lines below and start the debugger to run in localhost and debug it
# if __name__ == "__main__":
    # app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)
    # app.run(host="192.168.0.88")
