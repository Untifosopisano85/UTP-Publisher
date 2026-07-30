from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from dotenv import load_dotenv
import os


load_dotenv()


credentials = Credentials(

    token=None,

    refresh_token=os.getenv(
        "YOUTUBE_REFRESH_TOKEN"
    ),

    token_uri="https://oauth2.googleapis.com/token",

    client_id=os.getenv(
        "YOUTUBE_CLIENT_ID"
    ),

    client_secret=os.getenv(
        "YOUTUBE_CLIENT_SECRET"
    ),

)


youtube = build(
    "youtube",
    "v3",
    credentials=credentials,
)


response = youtube.channels().list(
    part="snippet",
    mine=True,
).execute()


print(response["items"][0]["snippet"]["title"])