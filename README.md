# AWS S3 File Processing System

## Project Overview
A serverless AWS project that processes file-upload events from Amazon S3, uses AWS Lambda to handle the events, and stores file metadata in Amazon DynamoDB.

## Architecture
Amazon S3 → AWS Lambda → Amazon DynamoDB

Amazon CloudWatch is used for logging and troubleshooting, while AWS IAM manages permissions.

## AWS Services Used
- **Amazon S3:** Stores uploaded files and generates object-created events.
- **AWS Lambda:** Processes S3 events using Python.
- **Amazon DynamoDB:** Stores file metadata.
- **AWS IAM:** Controls access between AWS services.
- **Amazon CloudWatch:** Records Lambda execution logs.

## Workflow
1. A file is uploaded to the S3 bucket.
2. S3 triggers the Lambda function.
3. Lambda extracts the relevant file information.
4. Metadata is stored in DynamoDB.
5. CloudWatch captures execution logs for troubleshooting.

## Key Learnings
- S3 event notifications
- Serverless event-driven architecture
- Python and AWS Lambda
- IAM permissions and troubleshooting
- DynamoDB integration
- CloudWatch logging

## Project Status
Completed as a hands-on AWS learning project. Cloud resources were cleaned up after testing.

## Security
No AWS credentials, access keys, passwords, or other secrets should be committed to this repository.
