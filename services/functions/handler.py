from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

from openapi_spec_validator import validate_spec
from openapi_spec_validator.readers import read_from_filename

spec_dict, spec_url = read_from_filename('assets/api-spec.yaml')

# If no exception is raised by validate_spec(), the spec is valid.
validate_spec(spec_dict)

validate_spec({})

logger = Logger()


@logger.inject_lambda_context
def handler(event: dict, context: LambdaContext) -> str:
    logger.info("Collecting payment")
    print(event)



    # You can log entire objects too
    return "hello world"