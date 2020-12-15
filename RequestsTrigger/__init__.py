import json
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    response = requests.get('https://microsoft.com')
    return func.HttpResponse(body=response.text, mimetype="text/html")
