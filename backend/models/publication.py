from dataclasses import dataclass, field


@dataclass
class Publication:


    # FILE

    video_path: str



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