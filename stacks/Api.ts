import {
  StackContext,
  use,
  Api as ApiGateway,
  Function
} from "@serverless-stack/resources";
import { SubnetType, Vpc } from "aws-cdk-lib/aws-ec2";
import { Effect, PolicyStatement } from "aws-cdk-lib/aws-iam";

export function Api({ stack }: StackContext) {

  const getVpcPermissions = (): PolicyStatement => {
    return new PolicyStatement({
      effect: Effect.ALLOW,
      actions: ['execute-api:Invoke'],
      resources: ['arn:aws:execute-api:eu-west-1:*:*/*']
    });
  }

  const vpc = Vpc.fromLookup(this, 'vpc', {
    vpcId: 'vpc-0323fde994a2faeef'
  })

  const func = new Function(this, 'handler', {
    handler: 'functions/handler.handler',
    permissions: [getVpcPermissions()],
    vpc: vpc,
    vpcSubnets: {
      subnetType: SubnetType.PUBLIC,
    },
    allowPublicSubnet: true
  })

  const api = new ApiGateway(stack, "api", {
    routes: {
      "GET /test": {
        function: func
      }
    },
  });
  

  stack.addOutputs({
    API_URL: api.url,
  });

  return api;
}
