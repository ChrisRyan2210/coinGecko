from src.api.api_call import call_api

def get_market_data(api_key, base_url, max_pages = 100):
    """
    Fetch cryptocurrency market data from CoinGecko API.
    
    Args:
        api_key: CoinGecko API key
        base_url: Base URL for the API (e.g., "https://api.coingecko.com/api/v3/")
        max_pages: Maximum number of pages to fetch (default: 250)
    
    Returns:
        List of cryptocurrency market data dictionaries
    """
    url = f"{base_url}coins/markets"
    all_data = []

    for page in range(1, max_pages+1):
        params = {
            "vs_currency":"usd",
            "per_page":250,
            "page":page,
        }
        
        data = call_api(api_key, url, params)
        
        # Break if no data returned (reached end of available data)
        if not data:
            break
            
        all_data.extend(data)

    return all_data

