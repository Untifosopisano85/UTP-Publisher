import cloudinary
import cloudinary.uploader

from connectors.meta.config import (
    CLOUDINARY_CLOUD_NAME,
    CLOUDINARY_API_KEY,
    CLOUDINARY_API_SECRET,
)


class StorageService:


    def __init__(self):

        cloudinary.config(
            cloud_name=CLOUDINARY_CLOUD_NAME,
            api_key=CLOUDINARY_API_KEY,
            api_secret=CLOUDINARY_API_SECRET,
        )


    def upload_video(
        self,
        file_path: str,
    ):

        result = cloudinary.uploader.upload(
            file_path,
            resource_type="video",
        )

        return {
            "url": result["secure_url"],
            "public_id": result["public_id"],
        }