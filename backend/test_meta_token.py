import requests

from connectors.meta.config import (
    PAGE_ACCESS_TOKEN,
    PAGE_ID,
)


url = "https://graph.facebook.com/v25.0/debug_token"

params = {
    "input_token": PAGE_ACCESS_TOKEN,
    "access_token": PAGE_ACCESS_TOKEN,
}


response = requests.get(
    url,
    params=params
)


print(response.status_code)
print(response.json())