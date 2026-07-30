from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from connectors.meta.config import (
    YOUTUBE_CLIENT_ID,
    YOUTUBE_CLIENT_SECRET,
    YOUTUBE_REFRESH_TOKEN,
)



class YouTubeClient:


    def __init__(self):

        self.credentials = Credentials(

            token=None,

            refresh_token=YOUTUBE_REFRESH_TOKEN,

            token_uri="https://oauth2.googleapis.com/token",

            client_id=YOUTUBE_CLIENT_ID,

            client_secret=YOUTUBE_CLIENT_SECRET,

        )


        self.youtube = build(

            "youtube",

            "v3",

            credentials=self.credentials,

        )