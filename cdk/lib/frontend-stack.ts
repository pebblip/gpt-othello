import { Stack, StackProps, CfnOutput } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as cloudfrontS3 from '@aws-solutions-constructs/aws-cloudfront-s3';
import { BucketDeployment, Source } from 'aws-cdk-lib/aws-s3-deployment';

export class FrontendStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const { s3Bucket, cloudFrontWebDistribution } = new cloudfrontS3.CloudFrontToS3(this, 'WebAppCloudFrontS3', {
      insertHttpSecurityHeaders: false,
    });

    new BucketDeployment(this, 'WebAppDeploy', {
      destinationBucket: s3Bucket!,
      distribution: cloudFrontWebDistribution,
      sources: [       
        Source.asset('../frontend/dist'),
      ],
    });

    new CfnOutput(this, 'DistributionDomainName', {
      value: cloudFrontWebDistribution!.distributionDomainName,
    });
  }
}
