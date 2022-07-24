import json

from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.validation import validator, envelopes, validate

import services.functions.schemas as schemas

logger = Logger(service="APP")

app = APIGatewayRestResolver()


@app.post("/test")
def hello_name():
    return {"message": f"hello !"}


@app.get("/test")
def hello():
    logger.info(f"Request from GET received")
    return {"message": "hello unknown!"}


@logger.inject_lambda_context(
    correlation_id_path=correlation_paths.API_GATEWAY_HTTP, log_event=True
)
def handler(event: dict, context: LambdaContext):
    event["path"] = event["requestContext"]["http"]["path"]
    event["httpMethod"] = event["requestContext"]["http"]["method"]

    # validate body schemas
    validate(
        event=event,
        schema=schemas.INPUT["paths"]["/test"]["post"]["requestBody"]["content"][
            "application/json"
        ]["schema"],
        envelope=envelopes.API_GATEWAY_HTTP,
    )

    # validate headers
    validate(
        event=event,
        schema=schemas.INPUT["paths"]["/test"]["parameters"],
        envelope="headers",
    )

    return app.resolve(event, context)
