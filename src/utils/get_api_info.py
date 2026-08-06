import sys
from pathlib import Path
from src.utils.config import load_config

config = load_config()

def get_api_info():

    api_key_secret = config['data_source']['coin_gecko_api']['api_key_secret_key']
    api_scope_secret = config['data_source']['coin_gecko_api']['api_key_secret_scope']
    base_url = config['data_source']['coin_gecko_api']['base_url']
    # print(api_key_secret)
    return api_key_secret, api_scope_secret, base_url