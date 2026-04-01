import json
import random
import string

# Temporary storage (later we will use DynamoDB)
url_store = {}

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    
    long_url = body.get("url")
    
    if not long_url:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "URL is required"})
        }

    short_code = generate_short_code()
    url_store[short_code] = long_url

    short_url = f"https://short.ly/{short_code}"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "short_url": short_url
        })
    }
