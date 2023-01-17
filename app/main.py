from flask import Flask, request, json
from werkzeug.exceptions import HTTPException
from flasgger import Swagger, swag_from
import requests

from validation import (
    url_validation,
    token_validation,
    alias_validation
)
from settings import (
    HOST,
    PORT
)

template = {
    "info":{
        "title": "ShortenREST API",
        "description": "ShortenREST adapter service to shorten URLs"
    }
}

BASE_URL = "https://api.shorten.rest/aliases"

app = Flask(__name__)
swagger = Swagger(app, template=template)


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        # "name": e.name,
        "data": {},
        "errors": [e.description],
    })
    response.content_type = "application/json"
    return response


@app.route("/create", methods=["POST"])
@swag_from("flasgger_docs/create_endpoint.yml")
def create_endpoint():
    # Get the url from the request body
    url = request.json.get("url")
    # Get the alias from the request body
    alias = request.json.get("alias", "")
    # Get the token from the request body
    token = request.json.get("token")

    errors = []
    # Validate the url
    try:
        url_validation(url)
    except ValueError as e:
        errors.append(str(e))
    # Validate the token
    try:
        token_validation(token)
    except ValueError as e:
        errors.append(str(e))
    # Validate the alias
    # try:
    #     alias_validation(alias)
    # except ValueError as e:
    #     errors.append(str(e))
    # Return the errors if any
    if errors:
        return {"data": {}, "errors": errors, "code": 422}, 422
    
    # Create the short url
    status_code, short_url, errors, code = create_short_url(url, alias, token)
    # Return the short url
    if status_code == 200:
        return {"data": {"short_url": short_url}, "errors": errors, "code": status_code}, status_code
    return {"data": {}, "errors": errors, "code": status_code}, status_code


@app.route("/delete", methods=["DELETE"])
@swag_from("flasgger_docs/delete_endpoint.yml")
def delete_endpoint():
    # Get the url from the request body
    alias = request.json.get("alias")
    # Get the token from the request body
    token = request.json.get("token")
    
    alias = alias.split("/")[-1]

    errors = []
    # Validate the token
    try:
        token_validation(token)
    except ValueError as e:
        errors.append(str(e))
    # Validate the alias
    try:
        alias_validation(alias)
    except ValueError as e:
        errors.append(str(e))
    # Return the errors if any
    if errors:
        return {"data": {}, "errors": errors, "code": 422}, 422

    # Delete the short url
    status_code, errors, code = delete_short_url(alias, token)
    # Return the response
    return {"data": {}, "errors": errors, "code": status_code}, status_code


def create_short_url(url, alias, token):
    # Set the header
    header = {
        'x-api-key': token
    }
    # Set the body
    body = {
        "destinations":
        [{
            "url": url
        }],
        "aliasName": alias
    }
    # Make the request
    response = requests.post(BASE_URL, json=body, headers=header)
    # Return the short url
    json = response.json()
    status_code = response.status_code
    if status_code == 200:
        return status_code, json["shortUrl"], json.get("errors", []), json.get("errorCode")
    return status_code, None, json.get("errorMessage", []), json.get("errorCode")


def delete_short_url(alias, token):
    # Set the header
    header = {
        'x-api-key': token
    }
    # Set the body
    body = {
        "aliasName": alias
    }
    # Make the request
    response = requests.delete(BASE_URL, json=body, headers=header)
    status_code = response.status_code
    if(status_code == 200):
        return status_code, [], 200
    # Return the response
    json = response.json()
    return status_code, json.get("errorMessage", []), json.get("errorCode")

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
