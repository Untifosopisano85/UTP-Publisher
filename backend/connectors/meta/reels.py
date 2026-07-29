from pathlib import Path

import requests

from connectors.meta.config import (
    PAGE_ID,
    PAGE_ACCESS_TOKEN,
    GRAPH_API_VERSION,
)

from connectors.meta.exceptions import MetaAPIError


class MetaReels:
    """
    Gestione pubblicazione Facebook Reels.

    Workflow:

        1. start upload
        2. upload video
        3. finish upload / publish
    """

    BASE_URL = "https://graph.facebook.com"

    DEBUG = True

    def __init__(self):
        self.page_id = PAGE_ID
        self.token = PAGE_ACCESS_TOKEN
        self.version = GRAPH_API_VERSION

            # --------------------------------------------------
    # STATUS
    # --------------------------------------------------

    def get_status(
        self,
        video_id: str,
    ):

        response = requests.get(
            f"{self.BASE_URL}/{self.version}/{video_id}",
            params={
                "fields": "status",
                "access_token": self.token,
            },
            timeout=30,
        )

        self._debug(
            "STATUS",
            response,
        )

        self._check(response)

        return response.json()

    # --------------------------------------------------
    # PUBLIC API
    # --------------------------------------------------

    def publish(
        self,
        video_path: str,
        title: str = "",
        description: str = "",
    ):
        """
        Pubblica un Reel completo.
        """

        upload = self._start_upload()

        video_id = upload["video_id"]
        upload_url = upload["upload_url"]

        self._upload_video(
            upload_url,
            video_path,
        )

        result = self._finish_upload(
            video_id,
            title,
            description,
        )

        return {
            "video_id": video_id,
            "result": result,
        }

    # --------------------------------------------------
    # START
    # --------------------------------------------------

    def _start_upload(self):

        response = requests.post(
            f"{self.BASE_URL}/{self.version}/{self.page_id}/video_reels",
            data={
                "upload_phase": "start",
                "access_token": self.token,
            },
            timeout=60,
        )

        self._debug(
            "START",
            response,
        )

        self._check(response)

        return response.json()

    # --------------------------------------------------
    # UPLOAD FILE
    # --------------------------------------------------

    def _upload_video(
        self,
        upload_url: str,
        video_path: str,
    ):

        path = Path(video_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Video non trovato: {path}"
            )

        file_size = path.stat().st_size

        with path.open("rb") as video:

            response = requests.post(
                upload_url,
                headers={
                    "Authorization": f"OAuth {self.token}",
                    "offset": "0",
                    "file_size": str(file_size),
                    "Content-Type": "application/octet-stream",
                },
                data=video,
                timeout=300,
            )

        self._debug(
            "UPLOAD",
            response,
        )

        self._check(response)

        return response.json()

    # --------------------------------------------------
    # FINISH / PUBLISH
    # --------------------------------------------------

    def _finish_upload(
        self,
        video_id: str,
        title: str,
        description: str,
    ):

        response = requests.post(
            f"{self.BASE_URL}/{self.version}/{self.page_id}/video_reels",
            data={
                "access_token": self.token,
                "upload_phase": "finish",
                "video_id": video_id,
                "video_state": "PUBLISHED",
                "title": title,
                "description": description,
            },
            timeout=60,
        )

        self._debug(
            "FINISH",
            response,
        )

        self._check(response)

        return response.json()

    # --------------------------------------------------
    # HELPERS
    # --------------------------------------------------

    def _check(self, response):

        if not response.ok:
            raise MetaAPIError(
                response.text
            )

    def _debug(
        self,
        name,
        response,
    ):

        if not self.DEBUG:
            return

        print(
            f"\n===== {name} ====="
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