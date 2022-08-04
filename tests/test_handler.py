import json
from services.functions.handler import handler
import unittest


class TestSum(unittest.TestCase):
    def test_handler_get(self):
        event = {
            "version": "2.0",
            "routeKey": "GET /test",
            "rawPath": "/test",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "content-length": "0",
                "host": "1gksbcp2qc.execute-api.eu-west-1.amazonaws.com",
                "user-agent": "Thunder Client (https://www.thunderclient.com)",
                "x-amzn-trace-id": "Root=1-62e3bde5-5cdb7c2b004e3a5a2ffa21a4",
                "x-forwarded-for": "86.18.202.122",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "858167599744",
                "apiId": "1gksbcp2qc",
                "domainName": "1gksbcp2qc.execute-api.eu-west-1.amazonaws.com",
                "domainPrefix": "1gksbcp2qc",
                "http": {
                    "method": "GET",
                    "path": "/test",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "86.18.202.122",
                    "userAgent": "Thunder Client (https://www.thunderclient.com)",
                },
                "requestId": "WBqb2i4ujoEEJdA=",
                "routeKey": "GET /test",
                "stage": "$default",
                "time": "29/Jul/2022:11:00:53 +0000",
                "timeEpoch": 1659092453271,
            },
            "isBase64Encoded": False,
        }
        context = {
            "function_name": "Development-middleware-te-apiLambdaGETtest2CF2602D-a0e3XQV7MZri",
            "invoked_function_arn": "arn:aws:lambda:eu-west-1:858167599744:function:Development-middleware-te-apiLambdaGETtest2CF2602D-a0e3XQV7MZri",
            "aws_request_id": "61fd569a-7bd9-4dc9-8673-8c50f186b584",
            "memory_limit_in_mb": "1024",
            "deadline_ms": "1659088677382",
        }
        self.assertEqual(handler(event, context)["statusCode"], 200)
        self.assertEqual(True, True)

    def test_handler_post(self):
        event = {
            "version": "2.0",
            "routeKey": "POST /test",
            "rawPath": "/test",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "content-length": "22",
                "content-type": "application/json",
                "host": "7s3as6rcqa.execute-api.eu-west-1.amazonaws.com",
                "user-agent": "Thunder Client (https://www.thunderclient.com)",
                "x-amzn-trace-id": "Root=1-62dbd116-5cba8ae64cbe70ec3fee15b8",
                "x-forwarded-for": "86.18.202.122",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
            },
            "requestContext": {
                "accountId": "858167599744",
                "apiId": "7s3as6rcqa",
                "domainName": "7s3as6rcqa.execute-api.eu-west-1.amazonaws.com",
                "domainPrefix": "7s3as6rcqa",
                "http": {
                    "method": "POST",
                    "path": "/test",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "86.18.202.122",
                    "userAgent": "Thunder Client (https://www.thunderclient.com)",
                },
                "requestId": "Vt2bmhBcjoEEPkw=",
                "routeKey": "POST /test",
                "stage": "$default",
                "time": "23/Jul/2022:10:44:38 +0000",
                "timeEpoch": 1658573078846,
            },
            "body": '{\n    "diff": "diff"\n}',
            "isBase64Encoded": False,
        }
        context = {}
        print(json.dumps(handler(event, context)))
        self.assertEqual(handler(event, context)["statusCode"], 200)
