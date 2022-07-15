INPUT = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "openapi": {"type": "string"},
        "info": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "version": {"type": "string"},
                "contact": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "email": {"type": "string"},
                        "url": {"type": "string"},
                    },
                    "required": ["name", "email", "url"],
                },
                "description": {"type": "string"},
            },
            "required": ["title", "version", "contact", "description"],
        },
        "paths": {
            "type": "object",
            "properties": {
                "/test": {
                    "type": "object",
                    "properties": {
                        "parameters": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {"$ref": {"type": "string"}},
                                    "required": ["$ref"],
                                }
                            ],
                        },
                        "get": {
                            "type": "object",
                            "properties": {
                                "responses": {
                                    "type": "object",
                                    "properties": {
                                        "200": {
                                            "type": "object",
                                            "properties": {
                                                "description": {"type": "string"},
                                                "content": {
                                                    "type": "object",
                                                    "properties": {
                                                        "text/plain": {
                                                            "type": "object",
                                                            "properties": {
                                                                "schema": {
                                                                    "type": "object",
                                                                    "properties": {
                                                                        "type": {
                                                                            "type": "string"
                                                                        },
                                                                        "example": {
                                                                            "type": "string"
                                                                        },
                                                                    },
                                                                    "required": [
                                                                        "type",
                                                                        "example",
                                                                    ],
                                                                }
                                                            },
                                                            "required": ["schema"],
                                                        }
                                                    },
                                                    "required": ["text/plain"],
                                                },
                                            },
                                            "required": ["description", "content"],
                                        }
                                    },
                                    "required": ["200"],
                                }
                            },
                            "required": ["responses"],
                        },
                    },
                    "required": ["parameters", "get"],
                }
            },
            "required": ["/test"],
        },
        "components": {
            "type": "object",
            "properties": {
                "parameters": {
                    "type": "object",
                    "properties": {
                        "x-nd-meta-data": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "in": {"type": "string"},
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "type": {"type": "string"},
                                        "example": {"type": "string"},
                                        "minLength": {"type": "integer"},
                                        "pattern": {"type": "string"},
                                    },
                                    "required": [
                                        "type",
                                        "example",
                                        "minLength",
                                        "pattern",
                                    ],
                                },
                                "description": {"type": "string"},
                                "required": {"type": "boolean"},
                            },
                            "required": [
                                "name",
                                "in",
                                "schema",
                                "description",
                                "required",
                            ],
                        }
                    },
                    "required": ["x-nd-meta-data"],
                }
            },
            "required": ["parameters"],
        },
    },
    "required": ["openapi", "info", "paths", "components"],
}

OUTPUT = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "Sample outgoing schema",
    "description": "The root schema comprises the entire JSON document.",
    "examples": [{"statusCode": 200, "body": "response"}],
    "required": ["statusCode", "body"],
    "properties": {
        "statusCode": {
            "$id": "#/properties/statusCode",
            "type": "integer",
            "title": "The statusCode",
        },
        "body": {"$id": "#/properties/body", "type": "string", "title": "The response"},
    },
}

INPUT_2 = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "openapi": "2.0.1",
    "info": {
        "title": "GForces test validation middleware",
        "version": "1.0.0",
        "contact": {
            "name": "Shared Services",
            "email": "shared-services@gforces.auto",
            "url": "https://www.gforces.co.uk",
        },
        "description": "This API gives the ability to save, retrieve and delete vehicles against a users account.",
    },
    "paths": {
        "/test": {
            "parameters": [
                {
                    "x-nd-meta-data": {
                        "name": "x-nd-meta-data",
                        "in": "header",
                        "schema": {
                            "type": "string",
                            "example": "ewogICJncm91cCI6ICI4ZTc3M2RiMjk3Mjk4ODVkMzMwOWMyMGMzNWY0N2JjYTgxZDdjYjA3IiwKICAiZnJhbmNoaXNlIjogIjczMWM0Yjk0OTY3OTczNjM0NjhiMmZlNTJhYTVlMmIxNTZjNGVkN2UiLAogICJsb2NhdGlvbiI6ICJiMzdiNDA1YjgwYTFjZjMxMzJjY2ZjMjZjMDdmZmRkYmYzNjk2NDI1IiwKICAibG9jYWxlIjogImVuLUdCIgp9",
                            "minLength": 1,
                            "pattern": "^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$",
                        },
                        "description": "A base 64 encoded JSON object following the defined structure. The group will be required and group software when on a V10 platform. The possible nodes are `group`, `franchise`, `location` and `groupSoftware`, the values need to be NetDirector hashes.",
                        "required": True,
                    }
                }
            ],
            "get": {
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "text/plain": {
                                "schema": {"type": "string", "example": "pong"}
                            }
                        },
                    }
                }
            },
        }
    },
    "components": {
        "parameters": {
            "x-nd-meta-data": {
                "name": "x-nd-meta-data",
                "in": "header",
                "schema": {
                    "type": "string",
                    "example": "ewogICJncm91cCI6ICI4ZTc3M2RiMjk3Mjk4ODVkMzMwOWMyMGMzNWY0N2JjYTgxZDdjYjA3IiwKICAiZnJhbmNoaXNlIjogIjczMWM0Yjk0OTY3OTczNjM0NjhiMmZlNTJhYTVlMmIxNTZjNGVkN2UiLAogICJsb2NhdGlvbiI6ICJiMzdiNDA1YjgwYTFjZjMxMzJjY2ZjMjZjMDdmZmRkYmYzNjk2NDI1IiwKICAibG9jYWxlIjogImVuLUdCIgp9",
                    "minLength": 1,
                    "pattern": "^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$",
                },
                "description": "A base 64 encoded JSON object following the defined structure. The group will be required and group software when on a V10 platform. The possible nodes are `group`, `franchise`, `location` and `groupSoftware`, the values need to be NetDirector hashes.",
                "required": True,
            }
        }
    },
}
