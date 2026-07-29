from pydantic import BaseModel


class PublishResponse(BaseModel):

    success: bool

    message: str

    platforms: dict
    