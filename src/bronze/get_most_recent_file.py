from src.utils.get_api_info import get_raw_storage_location
import os
from datetime import datetime
from pyspark.sql import SparkSession

def get_recent_file(file_prefix):

    spark = SparkSession.builder.getOrCreate()
    raw_file_path = get_raw_storage_location()
    target_file_path = None
    
    for file in os.listdir(raw_file_path):
        if file.split("_")[0] == file_prefix and file.split("_")[1][0:10] == datetime.now().strftime("%Y-%m-%d"):
            target_file_path = f"{raw_file_path}/{file}"
            
    if target_file_path:
        data = spark.read.json(target_file_path)
        return data
    return None
            