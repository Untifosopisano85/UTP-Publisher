from dataclasses import dataclass
from datetime import datetime


@dataclass
class PublicationResult:

    publication_id: str

    platform: str

    status: str

    external_id: str | None = None

    url: str | None = None

    error: str | None = None

    created_at: str = None



    def __post_init__(self):

        if self.created_at is None:

            self.created_at = datetime.now().isoformat()



    def to_dict(self):

        return {

            "publication_id": self.publication_id,

            "platform": self.platform,

            "status": self.status,

            "external_id": self.external_id,

            "url": self.url,

            "error": self.error,

            "created_at": self.created_at,

        }