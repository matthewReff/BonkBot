import json
from requests import Response
from http import HTTPStatus

class Error():
    status: HTTPStatus
    message: str

    def __init__(self, status, message):
        self.status = status
        self.message = message

class ResultOrError():
    error: Error = None
    result: any = None

    def __init__(self, response: Response):
        if response == None:
            raise ValueError("Response cannot be None")
        
        statusCode = response.status_code
        if statusCode >= 200 and statusCode < 300:
            return self.createWithResult(response.json())
        else:
            return self.createWithError(Error(statusCode, response.text))
        
    def createWithResult(self, result):
        self.result = result

    def createWithError(self, error):
        self.error = error

    def isSuccess(self):
        return self.error == None
    
    def isFailure(self):
        return not self.isSuccess()