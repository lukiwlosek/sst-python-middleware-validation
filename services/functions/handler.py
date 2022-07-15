from cmath import e
import json
from lib2to3.pytree import Base

# logger
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

# convert to json, and validate
from openapi_spec_validator import validate_spec, validate_spec_url
from openapi_spec_validator.readers import read_from_filename

# validation
from aws_lambda_powertools.utilities.validation import validator, envelopes, validate

# json to json schema
from openapi2jsonschema import command

logger = Logger()

spec_dict, spec_url = read_from_filename("./services/assets/api-spec.yaml")

import services.functions.schemas as schemas

# use JMESPATH aka envelope to extract JSON object from data input

from aws_lambda_powertools.utilities.data_classes import (
    event_source,
    APIGatewayProxyEvent,
)


@event_source(data_class=APIGatewayProxyEvent)
def handler(event: APIGatewayProxyEvent, context: LambdaContext) -> str:
    print(event.__dict__)
    validate(event=event, schema=schemas.INPUT_2)

    # You can log entire objects too
    return "hello world"
