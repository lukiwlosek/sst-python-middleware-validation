let input = {
  "openapi": "3.0.1",
  "info": {
    "title": "GForces test validation middleware",
    "version": "1.0.0",
    "contact": {
      "name": "Shared Services",
      "email": "shared-services@gforces.auto",
      "url": "https://www.gforces.co.uk"
    },
    "description": "This API gives the ability to save, retrieve and delete vehicles against a users account."
  },
  "paths": {
    "/test": {
      "parameters": [
        {
          "$ref": "#/components/parameters/x-nd-meta-data"
        }
      ],
      "get": {
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string",
                  "example": "pong"
                }
              }
            }
          }
        }
      },
      "post": {
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "user": {
                    "type": "string",
                    "example": "lukasz"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "success"
                    }
                  }
                }
              }
            }
          }
        }
      }
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
          "pattern": "^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$"
        },
        "description": "A base 64 encoded JSON object following the defined structure. The group will be required and group software when on a V10 platform. The possible nodes are `group`, `franchise`, `location` and `groupSoftware`, the values need to be NetDirector hashes.",
        "required": true
      }
    }
  }
}

import * as toJsonSchema from "@openapi-contrib/openapi-schema-to-json-schema";

let postInput = toJsonSchema(input);
console.log(JSON.stringify(postInput, undefined, 2))