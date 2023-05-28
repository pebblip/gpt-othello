import {
  aws_apigateway,
  aws_logs,
  RemovalPolicy,
  Stack,
  StackProps,
} from "aws-cdk-lib";
import { Cors, LambdaIntegration, RestApi } from "aws-cdk-lib/aws-apigateway";

import { Construct } from "constructs";

import { BackendStack } from "./backend-stack";

export class ApiGatewayStack extends Stack {
  constructor(
    scope: Construct,
    id: string,
    backend: BackendStack,
    props?: StackProps
  ) {
    super(scope, id, props);

    const api = new RestApi(this, "GptOthello", {
      deployOptions: {
        tracingEnabled: true,
        accessLogDestination: new aws_apigateway.LogGroupLogDestination(
          new aws_logs.LogGroup(this, "GptOthelloLogGroup", {
            logGroupName: "/aws/apigateway/gpt-othello",
            removalPolicy: RemovalPolicy.DESTROY,
          })
        ),
        accessLogFormat:
          aws_apigateway.AccessLogFormat.jsonWithStandardFields(),
        loggingLevel: aws_apigateway.MethodLoggingLevel.INFO,
      },
      defaultCorsPreflightOptions: {
        allowOrigins: Cors.ALL_ORIGINS,
        allowMethods: Cors.ALL_METHODS,
      },
    });

    api.root
      .addResource("{proxy+}")
      .addMethod("ANY", new LambdaIntegration(backend.fn));
  }
}
