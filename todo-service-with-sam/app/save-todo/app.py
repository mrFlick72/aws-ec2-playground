import json
import boto3
import uuid


def lambda_handler(event, context):
    data = json.loads(event["body"])

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("Todo")
    table.put_item(Item={
        "id": str(uuid.uuid4()),
        "message": data["message"]
    })

    return {
        "statusCode": 204
    }
