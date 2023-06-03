import {
  aws_lambda as lambda,
  aws_ssm as ssm,
  Duration,
  Stack,
  StackProps,
} from "aws-cdk-lib";
import { Architecture } from "aws-cdk-lib/aws-lambda";

import { Construct } from "constructs";

export class BackendStack extends Stack {
  public readonly fn: lambda.DockerImageFunction;

  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const openApiKey = ssm.StringParameter.fromStringParameterName(
      this,
      "openapi-key",
      "/gpt-othello/openapi-key"
    );

    const fn = new lambda.DockerImageFunction(this, "GptOthello", {
      code: lambda.DockerImageCode.fromImageAsset("../backend", {
        target: "prod",
        exclude: ["tests"],
      }),
      architecture: Architecture.ARM_64,
      timeout: Duration.minutes(3),
      memorySize: 4096,
      environment: {
        STAGE: "prod",
        OPENAI_API_KEY: openApiKey.stringValue,
      },
    });

    this.fn = fn;
  }
}
