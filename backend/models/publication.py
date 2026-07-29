from pydantic import BaseModel


class Platforms(BaseModel):

    facebook: bool = True
    instagram: bool = True
    youtube: bool = False
    tiktok: bool = False