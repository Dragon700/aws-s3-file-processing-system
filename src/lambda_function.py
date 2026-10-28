
import json
import boto3
import urllib.parse
import logging
from datetime import datetime, timezone

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("FileMetadata")


def lambda_handler(event, context):
    logger.info("Received SQS event")

    for sqs_record in event.get("Records", []):
        try:
            # SQS message body contains the original S3 event
            body = json.loads(sqs_record["body"])

            # Process each S3 record in the message
            for record in body.get("Records", []):
                bucket_name = record["s3"]["bucket"]["name"]

                object_key = urllib.parse.unquote_plus(
                    record["s3"]["object"]["key"]
                )

                file_size = record["s3"]["object"].get("size", 0)

                upload_time = record.get(
                    "eventTime",
                    datetime.now(timezone.utc).isoformat()
                )

                table.put_item(
                    Item={
                        "fileName": object_key,
                        "bucketName": bucket_name,
                        "fileSize": file_size,
                        "uploadTime": upload_time,
                        "status": "PROCESSED"
                    }
                )

                logger.info(
                    "Successfully saved metadata for %s",
                    object_key
                )

        except Exception:
            logger.exception("Failed to process SQS message")
            raise

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "SQS messages processed successfully"
        })
    }

