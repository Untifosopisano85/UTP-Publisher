from pydantic import BaseModel


class PublishRequest(BaseModel):

    video_path: str

    platforms: list[str]

    password: str

    youtube_title: str = ""

    youtube_description: str = ""

    facebook_message: str = ""

    instagram_caption: str = ""

    tiktok_caption: str = ""
