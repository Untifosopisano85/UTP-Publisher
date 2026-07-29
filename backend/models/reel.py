from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class Reel:
    video: Path
    title: str = ""
    description: str = ""
    hashtags: list[str] = field(default_factory=list)
    thumbnail: Path | None = None

    @classmethod
    def from_file(cls, filename: str, **kwargs):
        return cls(
            video=Path(filename),
            **kwargs,
        )

    @property
    def exists(self):
        return self.video.exists()

    @property
    def full_description(self):
        if not self.hashtags:
            return self.description

        tags = " ".join(
            f"#{tag.lstrip('#')}"
            for tag in self.hashtags
        )

        if self.description:
            return f"{self.description}\n\n{tags}"

        return tags