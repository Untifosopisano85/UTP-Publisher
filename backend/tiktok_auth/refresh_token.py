import requests

from config import (
    TIKTOK_CLIENT_KEY,
    TIKTOK_CLIENT_SECRET,
)


TOKEN_URL = "https://open.tiktokapis.com/v2/oauth/token/"


def refresh_access_token(refresh_token):

    payload = {

        "client_key": TIKTOK_CLIENT_KEY,

        "client_secret": TIKTOK_CLIENT_SECRET,

        "grant_type": "refresh_token",

        "refresh_token": refresh_token,

    }


    response = requests.post(
        TOKEN_URL,
        data=payload
    )


    response.raise_for_status()


    return response.json()



if __name__ == "__main__":

    print(
        "Refresh token TikTok pronto"
    )