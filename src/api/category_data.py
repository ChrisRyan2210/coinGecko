from src.api.api_call import call_api

def get_category_data(api_key, base_url):

    url = f"{base_url}coins/categories"
    params = {
        "order":"market_cap_desc"
    }
    
    data = call_api(api_key, url, params)
    
    return data
