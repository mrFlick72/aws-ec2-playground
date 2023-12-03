import os
import requests
from jwcrypto import jws, jwk
import json

default_token_verification_outcome = {
    "principalId": "*",
    "effect": "Deny"
}


def generate_policy(principalId, effect):
    return {
        "context": {},
        "principalId": principalId,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": "*"
                }
            ]
        }
    }


def token_verifier(jwstoken, keys):
    principalId = "*"
    effect = "Allow"

    try:
        jwstoken.verify(keys[0])
        principalId = json.loads(jwstoken.payload.decode("utf-8"))["sub"]
    except:
        try:
            jwstoken.verify(keys[1])
            principalId = json.loads(jwstoken.payload.decode("utf-8"))["sub"]
        except:
            effect = "Deny"

    return {
        "principalId": principalId,
        "effect": effect
    }


def token_validator(token):
    try:
        jwks = f"https://cognito-idp.{os.environ['REGION']}.amazonaws.com/{os.environ['USER_POOL_ID']}/.well-known/jwks.json"
        jwks_content = requests.get(jwks).json()
        keys = [
            jwk.JWK(**jwks_content["keys"][0]),
            jwk.JWK(**jwks_content["keys"][1]),
        ]

        jwstoken = jws.JWS()
        jwstoken.deserialize(token)

        return token_verifier(jwstoken, keys)
    except:
        return default_token_verification_outcome


def lambda_handler(event, context):
    token = event["authorizationToken"]
    validated_token_info = token_validator(token[7:])
    return generate_policy(validated_token_info["principalId"], validated_token_info["effect"])
