import sys
from pathlib import Path

# Getting the directory of src folder so I can import config.py
project_root = Path.cwd().parent.parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))  # ← Add this line!

from utils.config import load_config

config = load_config()

def get_api_info():

    api_key_secret = config['data_source']['coin_gecko_api']['api_key_secret_key']
    api_scope_secret = config['data_source']['coin_gecko_api']['api_key_secret_scope']
    base_url = config['data_source']['coin_gecko_api']['base_url']

    return api_key_secret, api_scope_secret, base_url