mkdir -p ../src/lambda
nano ../src/lambda/handler.pyimport json
import boto3
import string
import random
import os

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('TABLE_NAME', 'url-shortener-table')

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def lambda_handler(event, context):
    http_method = event.get('httpMethod', '')
    path = event.get('path', '')

    if http_method == 'POST' and path == '/shorten':
        return shorten_url(event)
    elif http_method == 'GET' and path.startswith('/'):
        short_code = path.lstrip('/')
        return redirect_url(short_code)
    else:
        return response(400, {'error': 'Invalid request'})

def shorten_url(event):
    try:
        body = json.loads(event.get('body', '{}'))
        long_url = body.get('url', '')

        if not long_url:
            return response(400, {'error': 'URL is required'})

        short_code = generate_short_code()
        table = dynamodb.Table(TABLE_NAME)

        table.put_item(Item={
            'short_code': short_code,
            'long_url': long_url
        })

        return response(200, {
            'short_code': short_code,
            'short_url': f'https://yourapi.execute-api.eu-west-1.amazonaws.com/{short_code}',
            'long_url': long_url
        })
    except Exception as e:
        return response(500, {'error': str(e)})

def redirect_url(short_code):
    try:
        table = dynamodb.Table(TABLE_NAME)
        result = table.get_item(Key={'short_code': short_code})
        item = result.get('Item')

        if not item:
            return response(404, {'error': 'Short URL not found'})

        return {
            'statusCode': 301,
            'headers': {'Location': item['long_url']},
            'body': ''
        }
    except Exception as e:
        return response(500, {'error': str(e)})

def response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body)
    }

