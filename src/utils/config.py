import yaml
from pathlib import Path

def load_config():
    # Get current working directory (works for any user)
    project_root = Path(__file__).resolve().parent.parent
    
    # Single config file path
    config_path = project_root / "config" / "config.yaml"
    
    print(f"Loading config from: {config_path}")
    
    # Load the YAML file
    with open(config_path, 'r') as file:
        full_config = yaml.safe_load(file)
    
    # Read which environment to use from the file itself
    active_env = full_config['active_environment']
    
    # Return only the active environment's config
    config = full_config['environments'][active_env]
    config['environment'] = active_env  # Add the environment name to the config
    
    return config