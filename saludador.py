import json


def handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hola desde lambda version 2!'
    }
