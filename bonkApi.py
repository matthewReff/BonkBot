import json
import requests

API_BASE_URL = "https://testapi.tendec.dev/"
JAIL_ENDPOINT = API_BASE_URL + "v1/jail"
ADD_OFFENSE_ENDPOINT = API_BASE_URL + "v1/addoffense"
GET_OFFENSES_ENDPOINT = API_BASE_URL + "v1/getoffenses"
RAP_SHEET_ENDPOINT = API_BASE_URL + "v1/rapsheet"

def jailCall(serverId, userId, offenseName):
    requestJson = json.dumps(
        {
            "serverId": str(serverId),
            "userId": str(userId),
            "offenseName": offenseName,
        }
    )
    return requests.post(JAIL_ENDPOINT, data=requestJson)

def addOffenseCall(serverId, offenseName):
    requestJson = json.dumps(
        {
            "serverId": str(serverId),
            "offenseName": offenseName,
        }
    )
    return requests.put(ADD_OFFENSE_ENDPOINT, data=requestJson)

def rapsheetCall(serverId, userId):
    requestJson = json.dumps(
        {
            "serverId": str(serverId),
            "userId": str(userId),
        }
    )
    return requests.post(RAP_SHEET_ENDPOINT, data=requestJson)

def getOffensesCall(serverId):
    requestJson = json.dumps(
        {
            "serverId": str(serverId)
        }
    )
    return requests.post(GET_OFFENSES_ENDPOINT, data=requestJson)