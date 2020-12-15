import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python 39 syntax test.')

    # Merge Dict
    pycon = {2016: "Portland", 2018: "Cleveland"}
    europython = {2017: "Rimini", 2018: "Edinburgh", 2019: "Basel"}
    merged = {**pycon, **europython}

    if (name := req.params.get('name')) is not None:
        return func.HttpResponse(f"Python 38 Hello {name}!")
    else:
        return func.HttpResponse(
             "Python 39 test OK",
             status_code=400
        )
