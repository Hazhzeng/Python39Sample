import logging

import azure.functions as func
from dataclasses import dataclass

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python 37 syntax test.')

    @dataclass
    class message():
        content = '123'

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Python 37 Hello {name}!")
    else:
        return func.HttpResponse(
             "Python 37 test OK",
             status_code=400
        )
