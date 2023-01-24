from flask import Flask, request
from flask_restful import Api
import json

from MyFunctions import CalcolaCashIniziale, CalcolaMutuoAnniCalcAPI, CalcolaMutuoRataFissaAPI, CalcolaMutuoTilgungAPI, EurostatCall

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
    if "Anni per Calcolo Mutuo" in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAnniCalcAPI(request_data)
    elif "Rata" in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRataFissaAPI(request_data)
    elif "Rimborso Capitale" in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoTilgungAPI(request_data)

    dummy=1
    ReturnData = OutputsMutuo.to_json()

    return ReturnData

@app.route("/outMutuoAvg", methods = ["POST"])
def returnDataAnno():

    print("/outMutuoAvg")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    if "Anni per Calcolo Mutuo" in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAnniCalcAPI(request_data)
    elif "Rata" in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRataFissaAPI(request_data)
    elif "Rimborso Capitale" in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoTilgungAPI(request_data)
    dummy=1
    ReturnData = OutputsAnnuoMutuo.to_json()

    return ReturnData

@app.route("/outMutuoAvgTot", methods = ["POST"])
def returnDataAvg():

    print("/outMutuoAvgTot")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    if "Anni per Calcolo Mutuo" in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAnniCalcAPI(request_data)
    elif "Rata" in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRataFissaAPI(request_data)
    elif "Rimborso Capitale" in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoTilgungAPI(request_data)
    dummy=1
    ReturnData = OutputAvgMutuo.to_json()

    return ReturnData

@app.route("/outMutuoOverview", methods = ["POST"])
def returnDataOv():

    print("/outMutuoOverview")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    if "Anni per Calcolo Mutuo" in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAnniCalcAPI(request_data)
    elif "Rata" in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoRataFissaAPI(request_data)
    elif "Rimborso Capitale" in request_data:
        OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoTilgungAPI(request_data)
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

@app.route("/outSpeseOverview", methods = ["POST"])
def returnDataSpesaDetails():

    print("/outSpeseOverview")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    OutputsSpeseIniziali, OutputsSpeseInizialiDettaglio = CalcolaCashIniziale(request_data)
    dummy=1
    ReturnData = OutputsSpeseInizialiDettaglio.to_json()

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
# if __name__ == "__main__":
#     app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)
