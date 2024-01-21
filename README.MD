## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed the latest version of [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

## Running the App with AWS SAM CLI

To run this application, follow these steps:

1. **Navigate to the project directory in your terminal.**

2. **Build the SAM application:**

	```
	sam build --use-container -t template.yaml
	```

3. **Deploy the SAM application:**

	```
	sam deploy --stack-name sam-app --capabilities CAPABILITY_IAM --image-repository <Your ECR repo>
	```

**Reference links**

1. [Deploying Docker Containers to Lambda using AWS SAM and CodePipeline (Part 1)](https://dev.to/aws-builders/deploying-docker-containers-to-lambda-using-aws-sam-and-codepipeline-part-1-4nm5)
2. [How to run Playwright with Python in AWS Lambda](https://www.cloudtechsimplified.com/playwright-aws-lambda-python/)