import os
import requests
import yaml

# Retrieve environment variables
github_token = os.getenv("GITHUB_TOKEN")
repo_full_name = os.getenv("GITHUB_REPOSITORY")  # e.g., "owner/repo-name"
repo_owner, repo_name = repo_full_name.split("/")
github_actor = os.getenv("GITHUB_ACTOR")

# Fetch repository details from the GitHub API
api_url = f"https://api.github.com/repos/{repo_full_name}"
headers = {"Authorization": f"Bearer {github_token}"}
response = requests.get(api_url, headers=headers)

if response.status_code != 200:
    raise Exception(f"Failed to fetch repository details: {response.json()}")

repo_data = response.json()

# Define the configuration
config = {
    "version": "1.0",
    "repository": {
        "name": repo_data["name"],
        "owner": repo_data["owner"]["login"],
        "description": repo_data.get("description", "No description provided"),
        "created_at": repo_data["created_at"],
        "updated_at": repo_data["updated_at"]
    },
    "node_properties": [
        {
            "name": "exampleNode",
            "type": "container",
            "image": f"docker.io/{repo_owner}/{repo_name}:latest",
            "ports": [8080],
            "env": [
                {"name": "ENV_VAR", "value": "example_value"}
            ],
            "command": ["example_command", "arg1", "arg2"],
            "volumes": ["/data:/app/data"]
        }
    ],
    "settings": {
        "logging": "verbose",
        "monitoring": True,
        "auto_scale": False
    }
}

# Generate the YAML file
file_path = "nodeprop.config.yaml"
with open(file_path, "w") as file:
    yaml.dump(config, file, default_flow_style=False)

print(f"Configuration file '{file_path}' generated successfully.")