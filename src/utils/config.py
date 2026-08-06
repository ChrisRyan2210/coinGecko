import yaml
from pathlib import Path

def load_config():
    # Get the current notebook's path using Spark SQL (works on all Databricks compute)
    username = spark.sql("SELECT current_user()").collect()[0][0]
    
    # Build path to config file using the workspace structure
    # This assumes your project is always at /Workspace/Users/{username}/coin_gecko/
    config_path = Path(f"/Workspace/Users/{username}/coin_gecko/src/config/config.yaml")
    
    print(f"Loading config from: {config_path}")
    
    # print(f"Loading config from: {config_path}")
    
    # Load the YAML file
    with open(config_path, 'r') as file:
        full_config = yaml.safe_load(file)
    
    # Read which environment to use from the file itself
    active_env = full_config['active_environment']
    
    # print(f"Active environment: {active_env}")
    
    # Return only the active environment's config
    config = full_config['environments'][active_env]
    config['environment'] = active_env  # Add the environment name to the config
    
    return config
