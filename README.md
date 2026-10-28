# AWS Serverless File Processing System

A serverless, event-driven file processing pipeline built using AWS services. When a file is uploaded to Amazon S3, an event is sent to Amazon SQS, processed by AWS Lambda, and the file metadata is stored in Amazon DynamoDB.

## Architecture

**Amazon S3 → Amazon SQS → AWS Lambda → Amazon DynamoDB**

Amazon SQS Dead-Letter Queue (DLQ) handles messages that repeatedly fail processing. Amazon CloudWatch provides logs for monitoring and troubleshooting.

## AWS Services Used

- **Amazon S3:** Stores uploaded files and publishes object-creation events.
- **Amazon SQS:** Buffers file-processing events for reliable asynchronous processing.
- **AWS Lambda:** Processes SQS messages and extracts file metadata.
- **Amazon DynamoDB:** Stores file metadata, including filename, bucket name, size, upload time, and processing status.
- **Amazon SQS DLQ:** Receives messages that fail repeatedly.
- **Amazon CloudWatch:** Stores Lambda execution logs.
- **AWS IAM:** Controls permissions between services.

## How It Works

1. A user uploads a file to the S3 bucket.
2. S3 sends an object-creation event to the main SQS queue.
3. Lambda receives messages from SQS through an event source mapping.
4. Lambda extracts the object metadata and saves it to DynamoDB.
5. CloudWatch records processing logs.
6. Messages that repeatedly fail processing can be moved to the DLQ according to the queue's redrive policy.

## Testing and Validation

The project was tested to verify:

- S3 upload events reached SQS.
- Lambda processed SQS messages.
- File metadata appeared in DynamoDB.
- CloudWatch recorded successful processing logs.
- Failed messages reached the dead-letter queue after repeated delivery attempts.

## Screenshots

Screenshots of the AWS configuration and test results are available in the [`screenshots/`](screenshots/) directory.

- [Lambda SQS trigger](screenshots/01-lambda-sqs-trigger.png)
- [S3 event notification](screenshots/02-s3-event-notification.png)
- [SQS redrive policy](screenshots/03-sqs-redrive-policy.png)
- [DLQ failed message](screenshots/04-dlq-failed-message.png)
- [DynamoDB processed file](screenshots/05-dynamodb-processed-file.png)
- [CloudWatch success logs](screenshots/06-cloudwatch-success-logs.png)

## Repository Structure

```text
aws-s3-file-processing-system/
├── README.md
├── architecture.md
├── src/
│   └── lambda_function.py
└── screenshots/
    ├── 01-lambda-sqs-trigger.png
    ├── 02-s3-event-notification.png
    ├── 03-sqs-redrive-policy.png
    ├── 04-dlq-failed-message.png
    ├── 05-dynamodb-processed-file.png
    └── 06-cloudwatch-success-logs.png
```

## Cost and Cleanup

The AWS resources used for this demonstration have been deleted after testing to avoid unnecessary ongoing resource costs. The code and screenshots remain available in this repository.

## Future Improvements

- Add automated deployment using AWS SAM or Terraform.
- Add automated tests for the Lambda function.
- Improve structured logging and error reporting.
- Add CI/CD using GitHub Actions.
- Add file validation and additional metadata fields.

## Author

Prince Kumar Yadav

Cloud Computing and DevOps Learner

