import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python 38 syntax test.')


    if (name := req.params.get('name')) is not None:
        return func.HttpResponse(f"Python 38 Hello {name}!")
    else:
        return func.HttpResponse(
             "Python 38 test OK",
             status_code=400
        )
