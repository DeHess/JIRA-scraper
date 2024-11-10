import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

# Insert Domain, in this case io-link-manager
url = "https://io-link-manager.atlassian.net/rest/api/3/search"

#Insert your e-mail and a generated API Token
auth = HTTPBasicAuth("nathhess@gmail.com", api_key)

headers = {
  "Accept": "application/json"
}

#Insert Project Key
query = {
  'jql': 'project = HELLO'
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