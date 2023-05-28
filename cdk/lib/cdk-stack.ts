import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';

import { BackendStack } from './backend-stack';
import { ApiGatewayStack } from './api-gateway-stack';
import { FrontendStack } from './frontend-stack';

export class CdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

      const backend = new BackendStack(this, 'Backend');
      const apiGateway = new ApiGatewayStack(this, 'ApiGateway', backend);
      const frontend = new FrontendStack(this, 'Frontend');
  }
}
