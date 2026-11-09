import json, boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Properties')

def to_json(obj):
    '''
    Converts a DynamoDB item to JSON serializable format
    '''
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError(f"Not serializable: {type(obj)}")

def lambda_handler(event, context):
    listing_id = event['pathParameters']['id']
    resp = table.get_item(Key={'L_ListingID': listing_id})
    return {
        'statusCode': 200,
        'body': json.dumps(resp.get('Item', {}), default=to_json)
    }

'''
to_json function:

boto3 returns every DynamoDB number as Python’s Decimal type 
(to avoid float precision loss), and Python’s json.dumps doesn’t 
know how to serialize Decimal. Your item has at least one numeric 
attribute, probably something like a price, bedrooms, or square 
footage, so json.dumps fails on it.
'''