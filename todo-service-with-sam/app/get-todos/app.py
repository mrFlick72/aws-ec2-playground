import json
import boto3


def lambda_handler(event, context):
    response = []
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("Todo")

    scan_response = table.scan()['Items']

    for item in scan_response:
        response.append({"id": item["id"], "message": item["message"]})

    return {
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response),
        "statusCode": 200
    }
