import json
from datetime import datetime
from src.config.get_api_info import get_raw_storage_location

def save_raw_json(data, file_type):

    timestamp = datetime.now().strftime("%Y-%m-%d")
    file_path = f"{get_raw_storage_location()}/{file_type}_{timestamp}.json"
    
    with open(file_path, "w") as file:
        json.dump(data, file)