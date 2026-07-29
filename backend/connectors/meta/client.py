import requests

from connectors.meta.config import (
    GRAPH_API_VERSION,
    PAGE_ACCESS_TOKEN,
)


class MetaClient:

    BASE_URL = f"https://graph.facebook.com/{GRAPH_API_VERSION}"


    def __init__(self):

        self.access_token = PAGE_ACCESS_TOKEN
        self.graph_version = GRAPH_API_VERSION

        print(
            "TOKEN CARICATO:",
            self.access_token[:25],
            "...",
            self.access_token[-10:]
        )


    def get(
        self,
        endpoint: str,
        params: dict | None = None,
    ):

        return self._request(
            method="GET",
            endpoint=endpoint,
            params=params,
        )


    def post(
        self,
        endpoint: str,
        data: dict | None = None,
    ):

        return self._request(
            method="POST",
            endpoint=endpoint,
            data=data,
        )


    def _request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        data: dict | None = None,
    ):

        params = params or {}
        data = data or {}

        if method == "GET":
            params.setdefault(
                "access_token",
                self.access_token
            )

        else:
            data.setdefault(
                "access_token",
                self.access_token
            )


        return requests.request(
            method=method,
            url=f"{self.BASE_URL}/{endpoint.lstrip('/')}",
            params=params if method == "GET" else None,
            data=data if method == "POST" else None,
            timeout=30,
        )