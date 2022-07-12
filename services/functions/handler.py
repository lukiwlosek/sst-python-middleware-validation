from cmath import e
# logger
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

# convert to json, and validate
from openapi_spec_validator import validate_spec, validate_spec_url
from openapi_spec_validator.readers import read_from_filename

# validation
from aws_lambda_powertools.utilities.validation import validator, envelopes

# json to json schema
from openapi2jsonschema import command

logger = Logger()

spec_dict, spec_url = read_from_filename('./services/assets/api-spec.yaml')

import services.functions.schemas as schemas

def handler(event, context: LambdaContext) -> str:
    print(event)
    print(spec_dict)

    # You can log entire objects too
    return "hello world"