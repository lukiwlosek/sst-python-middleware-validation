import json
from services.functions.handler import handler
import unittest


class TestSum(unittest.TestCase):
    def test_handler_get(self):
        event = {
            "_data": {
                "version": "2.0",
                "routeKey": "GET /test",
                "rawPath": "/test",
                "rawQueryString": "",
                "headers": {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "content-length": "0",
                    "host": "7s3as6rcqa.execute-api.eu-west-1.amazonaws.com",
                    "user-agent": "Thunder Client (https://www.thunderclient.com)",
                    "x-amzn-trace-id": "Root=1-62d6e09c-04e4521b6afbe9606391dade",
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
                        "method": "GET",
                        "path": "/test",
                        "protocol": "HTTP/1.1",
                        "sourceIp": "86.18.202.122",
                        "userAgent": "Thunder Client (https://www.thunderclient.com)",
                    },
                    "requestId": "VhgIfgLPjoEEJEQ=",
                    "routeKey": "GET /test",
                    "stage": "$default",
                    "time": "19/Jul/2022:16:49:32 +0000",
                    "timeEpoch": 1658249372582,
                },
                "isBase64Encoded": False,
            },
            "_json_data": None,
        }
        context = {}
        print(json.dumps(handler(event, context)))
        self.assertEqual(handler(event, context)["statusCode"], 200)

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
