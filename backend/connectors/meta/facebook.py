from pathlib import Path

import requests

from connectors.meta.client import MetaClient
from connectors.meta.config import PAGE_ID
from connectors.meta.exceptions import MetaAPIError
from connectors.meta.reels import MetaReels


class FacebookConnector:

    def __init__(self):

        self.client = MetaClient()
        self.reels = MetaReels()


    # --------------------------------------------------
    # PAGINA
    # --------------------------------------------------

    def get_page_info(self):

        response = self.client.get(
            PAGE_ID,
            {
                "fields": "id,name",
            },
        )

        self._check(response)

        return response.json()


    # --------------------------------------------------
    # TESTO
    # --------------------------------------------------

    def publish_text(
        self,
        message: str,
    ):

        response = self.client.post(
            f"{PAGE_ID}/feed",
            {
                "message": message,
            },
        )

        self._check(response)

        return response.json()


    # --------------------------------------------------
    # IMMAGINE
    # --------------------------------------------------

    def publish_image(
        self,
        image_path: str,
        caption: str = "",
    ):

        path = Path(image_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Immagine non trovata: {path}"
            )

        with path.open("rb") as image:

            response = requests.post(
                f"{self.client.BASE_URL}/{PAGE_ID}/photos",
                data={
                    "caption": caption,
                    "access_token": self.client.access_token,
                },
                files={
                    "source": image,
                },
                timeout=60,
            )

        self._check(response)

        return response.json()


    # --------------------------------------------------
    # REEL
    # --------------------------------------------------

    def publish_reel(
        self,
        reel,
    ):

        return self.reels.publish(
            video_path=str(reel.video),
            title=reel.title,
            description=reel.full_description,
        )


    def get_reel_status(
        self,
        video_id: str,
    ):

        return self.reels.get_status(
            video_id
        )


    # --------------------------------------------------
    # ERROR HANDLING
    # --------------------------------------------------

    def _check(
        self,
        response,
    ):

        if not response.ok:

            raise MetaAPIError(
                response.text
            )