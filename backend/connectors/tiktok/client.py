from config import (
    TIKTOK_CLIENT_KEY,
    TIKTOK_CLIENT_SECRET,
    TIKTOK_ACCESS_TOKEN,
)

import requests


class TikTokClient:

    BASE_URL = "https://open.tiktokapis.com"


    def __init__(self):

        self.client_key = TIKTOK_CLIENT_KEY
        self.client_secret = TIKTOK_CLIENT_SECRET
        self.access_token = TIKTOK_ACCESS_TOKEN


    def headers(self):

        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }


    def post(self, endpoint, payload=None):

        url = f"{self.BASE_URL}{endpoint}"

        response = requests.post(
            url,
            headers=self.headers(),
            json=payload
        )

        response.raise_for_status()

        return response.json()