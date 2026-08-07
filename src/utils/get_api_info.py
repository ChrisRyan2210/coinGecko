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

def get_raw_storage_location():

    raw_storage_path = config['storage']['raw']
    # print(raw_storage_path)
    
    return raw_storage_path

def get_bronze_schema_path():

    bronze_schema_path = config['storage']['bronze_schema_path']
    # print(raw_storage_path)
    
    return bronze_schema_path
