import json
import requests
from http import HTTPStatus

from api.resultOrError import ResultOrError, Error

API_BASE_URL = "https://testapi.tendec.dev/"
JAIL_ENDPOINT = API_BASE_URL + "v1/jail"
ADD_OFFENSE_ENDPOINT = API_BASE_URL + "v1/addoffense"
GET_OFFENSES_ENDPOINT = API_BASE_URL + "v1/getoffenses"
RAP_SHEET_ENDPOINT = API_BASE_URL + "v1/rapsheet"

def wrapper(function) -> ResultOrError:
    try:
        pass
        result = function
        return ResultOrError(result)
    except Exception as e:
        error = Error(HTTPStatus.BAD_REQUEST, "Unhandled exception while making api call: " + str(e))
        return ResultOrError.createWithError(error)
        
    
def jailCall(serverId, userId, offenseName) -> ResultOrError:
    try:
        requestJson = json.dumps(
            {
                "serverId": str(serverId),
                "userId": str(userId),
                "offenseName": offenseName,
            }
        )
        apiResponse = requests.post(JAIL_ENDPOINT, data=requestJson, timeout=3)
        return ResultOrError(apiResponse)
    except Exception as e:
        error = Error(HTTPStatus.BAD_REQUEST, "Unhandled exception while making api call: " + str(e))
        return ResultOrError.createWithError(error)

def addOffenseCall(serverId, offenseName) -> ResultOrError:
    try:
        requestJson = json.dumps(
            {
                "serverId": str(serverId),
                "offenseName": offenseName,
            }
        )
        apiResponse = requests.put(ADD_OFFENSE_ENDPOINT, data=requestJson, timeout=3)
        return ResultOrError(apiResponse)
    except Exception as e:
        error = Error(HTTPStatus.BAD_REQUEST, "Unhandled exception while making api call: " + str(e))
        return ResultOrError.createWithError(error)

def rapsheetCall(serverId, userId) -> ResultOrError:
    try:
        requestJson = json.dumps(
            {
                "serverId": str(serverId),
                "userId": str(userId),
            }
        )
        apiResponse = requests.post(RAP_SHEET_ENDPOINT, data=requestJson, timeout=3)
        return ResultOrError(apiResponse)
    except Exception as e:
        error = Error(HTTPStatus.BAD_REQUEST, "Unhandled exception while making api call: " + str(e))
        return ResultOrError.createWithError(error)

def getOffensesCall(serverId) -> ResultOrError:
    try:
        requestJson = json.dumps(
            {
                "serverId": str(serverId)
            }
        )
        apiResponse = requests.post(GET_OFFENSES_ENDPOINT, data=requestJson, timeout=3)
        return ResultOrError(apiResponse)
    except Exception as e:
        error = Error(HTTPStatus.BAD_REQUEST, "Unhandled exception while making api call: " + str(e))
        return ResultOrError.createWithError(error)