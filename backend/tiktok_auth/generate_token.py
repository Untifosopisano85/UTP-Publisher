import urllib.parse
import webbrowser
import secrets
import hashlib
import base64

from config import TIKTOK_CLIENT_KEY


REDIRECT_URI = "http://localhost:8000/tiktok/callback"


SCOPES = [
    "user.info.basic",
    "video.upload",
]


def generate_code_verifier():

    return secrets.token_urlsafe(64)



def generate_code_challenge(verifier):

    digest = hashlib.sha256(
        verifier.encode("utf-8")
    ).digest()

    return base64.urlsafe_b64encode(
        digest
    ).decode("utf-8").replace("=", "")



def generate_url():

    verifier = generate_code_verifier()

    challenge = generate_code_challenge(
        verifier
    )


    params = {

        "client_key": TIKTOK_CLIENT_KEY,

        "scope": ",".join(SCOPES),

        "response_type": "code",

        "redirect_uri": REDIRECT_URI,

        "code_challenge": challenge,

        "code_challenge_method": "S256",

    }


    url = (
        "https://www.tiktok.com/v2/auth/authorize/?"
        + urllib.parse.urlencode(params)
    )


    print("\n===== CODE VERIFIER =====\n")
    print(verifier)

    print("\n===== URL GENERATO =====\n")
    print(url)

    return url



if __name__ == "__main__":

    url = generate_url()

    webbrowser.open(url)