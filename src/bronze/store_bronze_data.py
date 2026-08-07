# from pyspark.sql import SparkSession
from src.utils.get_api_info import get_bronze_schema_path
from pyspark.sql.functions import lit
from datetime import datetime

# coin_gecko_dev.bronze
def save_data(raw_df, data_type):
    
    base_schema_path = f"{get_bronze_schema_path()}.{data_type}" 
    # spark = SparkSession.builder.getOrCreate()
    raw_df_with_meta_data = raw_df.withColumn("ingestion_time", lit(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    
    raw_df_with_meta_data.write.mode("append").format("delta").saveAsTable(base_schema_path)