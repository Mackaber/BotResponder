import requests
import json

def langtail_request(msg):
    url = "https://api.langtail.com/workshop--xSR38/langtail-playground/potatoe/preview"
    
    querystring = {"v":"eaqerw93"}
    
    payload = {
        "stream": False,
        "user": "user_123",
        "seed": 123,
        "doNotRecord": False,
        "messages": [
            {
                "role": "user",
                "content": msg
            }
        ],
        "metadata": {"my_identifier": "my-custom-ID"}
    }
    headers = {
        "X-API-Key": os.getenv('LANG_TAIL_API_KEY'),
        "content-type": "application/json"
    }
    
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    
    print(response.text)

    # parse json
    data = json.loads(response.text)
    return data['choices'][0]['message']['content']
