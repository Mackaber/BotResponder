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
        "X-API-Key": "lt-eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJsYW5ndGFpbC1hcGkiLCJzdWIiOiJjbG9sbmxvYzUwMDAzangwODMwcjN2MXMwIiwianRpIjoiY2x1bGRsdXFwMDAwOGpwMGY3dDdoZHB0byIsInJhdGVMaW1pdCI6bnVsbCwiaWF0IjoxNzEyMjQzNTYwfQ.eNzS0YuD0KmZ9CwgcYFelJl_hBGWkfzj6WaZxzYUqWE9zaqOe763e-Ut_7fIoMGDK61HwR1o2i7z9_CZ6f2wig",
        "content-type": "application/json"
    }
    
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    
    print(response.text)

    # parse json
    data = json.loads(response.text)
    return data['choices'][0]['message']['content']