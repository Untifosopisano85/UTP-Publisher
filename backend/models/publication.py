from dataclasses import dataclass, field
from datetime import datetime

from utils.publication_id import generate_publication_id


@dataclass
class Publication:


    # FILE

    video_path: str



    # IDENTIFICATIVO PUBBLICAZIONE

    publication_id: str = field(
        default_factory=generate_publication_id
    )


    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )



    # DATI GENERALI

    thumbnail_path: str | None = None


    platforms: list[str] = field(
        default_factory=list
    )



    # YOUTUBE

    youtube_title: str = ""

    youtube_description: str = ""

    youtube_tags: list[str] = field(
        default_factory=list
    )



    def validate(self):

        if len(self.youtube_title) > 100:

            raise ValueError(
                "Il titolo YouTube non può superare i 100 caratteri"
            )



    # FACEBOOK

    facebook_message: str = ""



    # INSTAGRAM

    instagram_caption: str = ""



    # TIKTOK

    tiktok_caption: str = ""