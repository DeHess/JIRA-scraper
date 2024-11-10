import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
email = os.getenv("EMAIL")
domain = os.getenv("JIRA_DOMAIN")
project_key = os.getenv("PROJECT_KEY")

url = f"https://{domain}.atlassian.net/rest/api/3/search"

auth = HTTPBasicAuth(email, api_key)

headers = {
  "Accept": "application/json"
}

query = {
  'jql': f'project = {project_key}'
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)


print("===============================================")
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))