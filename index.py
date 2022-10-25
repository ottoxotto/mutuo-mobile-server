from flask import Flask, request
from flask_restful import Api
import json

from MyFunctions import CalcolaCashIniziale, CalcolaMutuoAPI

app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    return 'Home Page Route'

@app.route("/outMutuo", methods = ["POST"])
def returnDataDetails():

    print("/outMutuo")
    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAPI(request_data)
    dummy=1
    ReturnData = OutputsMutuo.to_json()

    return ReturnData

@app.route("/outMutuoAvg", methods = ["POST"])
def returnDataAnno():

    print("/outMutuoAvg")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAPI(request_data)
    dummy=1
    ReturnData = OutputsAnnuoMutuo.to_json()

    return ReturnData

@app.route("/outMutuoAvgTot", methods = ["POST"])
def returnDataAvg():

    print("/outMutuoAvgTot")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAPI(request_data)
    dummy=1
    ReturnData = OutputAvgMutuo.to_json()

    return ReturnData

@app.route("/outMutuoOverview", methods = ["POST"])
def returnDataOv():

    print("/outMutuoOverview")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    OutputsMutuo, OutputsAnnuoMutuo, OutputAvgMutuo, OutputOverviewMutuo = CalcolaMutuoAPI(request_data)
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
    dummy=1
    ReturnData = OutputsSpeseIniziali.to_json()

    return "ReturnData"

@app.route("/outSpeseOverview", methods = ["POST"])
def returnDataSpesaDetails():

    print("/outSpeseOverview")

    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    OutputsSpeseIniziali, OutputsSpeseInizialiDettaglio = CalcolaCashIniziale(request_data)
    dummy=1
    ReturnData = OutputsSpeseInizialiDettaglio.to_json()

    return ReturnData

# if __name__ == "__main__":
#     app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)
