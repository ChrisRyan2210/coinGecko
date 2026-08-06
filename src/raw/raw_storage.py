import json
from datetime import datetime

def save_raw_json(data, path, file_type):

    timestamp = datetime.now().strftime("%Y-%m-%d")
    file_path = f"{path}/{file_type}_{timestamp}.json"
    
    with open(file_path, "w") as file:
        json.dump(data, file)