import requests

# This is my main API call -> this gets called by all other sub_api functions
def call_api(api_key, url, params=None):
    
    headers = {
        "x-cg-demo-api-key": api_key,
    }
    print(f"Calling API: {url}")
    print(f"Params: {params}")
    try:
        response = requests.get(url, headers=headers, params=params)
        print(f"Response status: {response.status_code}")
        print(f"Response length: {len(response.text)} chars")
        
        response.raise_for_status()
        data = response.json()
        print(f"JSON parsed: {len(data) if isinstance(data, list) else 'dict'} items")
    except requests.exceptions.RequestException as e:
        print(f"API call failed: {e}")
        data = None

    return data


