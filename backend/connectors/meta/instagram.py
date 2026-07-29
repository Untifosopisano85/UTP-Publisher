import time
import requests

from connectors.meta.config import (
    INSTAGRAM_ACCOUNT_ID,
    PAGE_ACCESS_TOKEN,
    GRAPH_API_VERSION,
)

from connectors.meta.exceptions import MetaAPIError


class InstagramConnector:

    BASE_URL = "https://graph.facebook.com"


    def __init__(self):

        self.account_id = INSTAGRAM_ACCOUNT_ID
        self.token = PAGE_ACCESS_TOKEN
        self.version = GRAPH_API_VERSION



    # --------------------------------------------------
    # PUBBLICAZIONE REEL COMPLETA
    # --------------------------------------------------

    def publish_reel(
        self,
        video_url: str,
        caption: str = "",
    ):

        container = self._create_container(
            video_url,
            caption,
        )


        self._wait_until_ready(
            container["id"]
        )


        return self._publish_container(
            container["id"]
        )



    # --------------------------------------------------
    # CREAZIONE CONTAINER
    # --------------------------------------------------

    def _create_container(
        self,
        video_url: str,
        caption: str,
    ):

        response = requests.post(
            f"{self.BASE_URL}/{self.version}/{self.account_id}/media",
            data={
                "media_type": "REELS",
                "video_url": video_url,
                "caption": caption,
                "access_token": self.token,
            },
            timeout=60,
        )


        self._debug(
            "INSTAGRAM CREATE",
            response,
        )


        self._check(response)

        return response.json()



    # --------------------------------------------------
    # ATTESA ELABORAZIONE INSTAGRAM
    # --------------------------------------------------

    def _wait_until_ready(
        self,
        container_id: str,
    ):

        while True:

            response = requests.get(
                f"{self.BASE_URL}/{self.version}/{container_id}",
                params={
                    "fields": "status_code",
                    "access_token": self.token,
                },
                timeout=30,
            )


            self._debug(
                "INSTAGRAM STATUS",
                response,
            )


            self._check(response)


            status = response.json().get(
                "status_code"
            )


            print(
                "INSTAGRAM STATUS:",
                status,
            )


            if status == "FINISHED":
                return


            if status == "ERROR":

                raise MetaAPIError(
                    "Errore elaborazione Instagram Reel"
                )


            time.sleep(5)



    # --------------------------------------------------
    # PUBBLICAZIONE CONTAINER
    # --------------------------------------------------

    def _publish_container(
        self,
        container_id: str,
    ):

        response = requests.post(
            f"{self.BASE_URL}/{self.version}/{self.account_id}/media_publish",
            data={
                "creation_id": container_id,
                "access_token": self.token,
            },
            timeout=60,
        )


        self._debug(
            "INSTAGRAM PUBLISH",
            response,
        )


        self._check(response)

        return response.json()



    # --------------------------------------------------
    # CONTROLLO ERRORI
    # --------------------------------------------------

    def _check(
        self,
        response,
    ):

        if not response.ok:

            raise MetaAPIError(
                response.text
            )



    # --------------------------------------------------
    # DEBUG
    # --------------------------------------------------

    def _debug(
        self,
        title,
        response,
    ):

        print(
            f"\n===== {title} ====="
        )

        print(
            "STATUS:",
            response.status_code,
        )

        print(
            response.text
        )

        print(
            "====================\n"
        )