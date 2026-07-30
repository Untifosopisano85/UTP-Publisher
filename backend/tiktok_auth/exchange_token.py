import requests

from config import (
    TIKTOK_CLIENT_KEY,
    TIKTOK_CLIENT_SECRET,
)


TOKEN_URL = "https://open.tiktokapis.com/v2/oauth/token/"



def exchange_code(
    code,
    code_verifier
):

    payload = {

        "client_key": TIKTOK_CLIENT_KEY,

        "client_secret": TIKTOK_CLIENT_SECRET,

        "code": code,

        "grant_type": "authorization_code",

        "redirect_uri": "http://localhost:8000/tiktok/callback",

        "code_verifier": code_verifier,

    }


    response = requests.post(
        TOKEN_URL,
        data=payload
    )


    response.raise_for_status()


    return response.json()



if __name__ == "__main__":

    print(
        "Inserire authorization code e code verifier"
    )