from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class Reel:

    video: Path

    platforms: list[str] = field(
        default_factory=lambda: [
            "facebook",
            "instagram",
        ]
    )

    contents: dict = field(
        default_factory=dict
    )

    thumbnail: Path | None = None

    title: str = ""

    full_description: str = ""



    @classmethod
    def from_file(
        cls,
        filename: str,
        **kwargs
    ):

        return cls(
            video=Path(filename),
            **kwargs,
        )



    @property
    def exists(self):

        return self.video.exists()



    def get_content(
        self,
        platform: str
    ):

        return self.contents.get(
            platform,
            {}
        )