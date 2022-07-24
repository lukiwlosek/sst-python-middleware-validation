import {
  StackContext,
  use,
  Api as ApiGateway,
} from "@serverless-stack/resources";

export function Api({ stack }: StackContext) {

  const api = new ApiGateway(stack, "api", {
    routes: {
      "GET /test": 'functions/handler.handler',
      "POST /test": "functions/handler.handler"
    },
  });

  stack.addOutputs({
    API_URL: api.url,
  });

  return api;
}
