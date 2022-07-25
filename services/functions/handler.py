# from cmath import e
# import json
# from lib2to3.pytree import Base

# # logger
# from aws_lambda_powertools import Logger
# from aws_lambda_powertools.utilities.typing import LambdaContext

# # convert to json, and validate
# from openapi_spec_validator import validate_spec, validate_spec_url
# from openapi_spec_validator.readers import read_from_filename

# # validation
# from aws_lambda_powertools.utilities.validation import validator, envelopes, validate

# json to json schema
# from openapi2jsonschema import command

from module.service import make_external_request

# spec_dict, spec_url = read_from_filename("./services/assets/api-spec.yaml")


# use JMESPATH aka envelope to extract JSON object from data input

from aws_lambda_powertools.utilities.data_classes import (
    event_source,
    APIGatewayProxyEvent,
)


@event_source(data_class=APIGatewayProxyEvent)
def handler(event: APIGatewayProxyEvent, context) -> str:
    make_external_request()
    # You can log entire objects too
    return "hello world"
