import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("Todo")
    id = event["pathParameters"]["id"]

    table.delete_item(
        Key={
            'id': id
        }
    )

    return {
        "statusCode": 204
    }
