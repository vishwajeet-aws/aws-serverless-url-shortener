import json
import sys
sys.path.insert(0, '.')

from handler import lambda_handler

def test_shorten():
    event = {
        'httpMethod': 'POST',
        'path': '/shorten',
        'body': json.dumps({'url': 'https://www.google.com/very/long/url/here'})
    }
    result = lambda_handler(event, {})
    print("SHORTEN TEST:")
    print(f"  Status: {result['statusCode']}")
    print(f"  Body: {result['body']}")
    return json.loads(result['body'])

def test_redirect(short_code):
    event = {
        'httpMethod': 'GET',
        'path': f'/{short_code}'
    }
    result = lambda_handler(event, {})
    print("\nREDIRECT TEST:")
    print(f"  Status: {result['statusCode']}")

if __name__ == '__main__':
    result = test_shorten()
    if 'short_code' in result:
        test_redirect(result['short_code'])
