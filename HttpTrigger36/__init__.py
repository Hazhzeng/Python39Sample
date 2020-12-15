import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python 36 syntax test.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Python 36 Hello {name}!")
    else:
        return func.HttpResponse(
             "Python 36 test OK",
             status_code=400
        )
