from fastapi import APIRouter, UploadFile, File, Form

from services.publisher import Publisher
from services.storage import StorageService
from models import Reel


router = APIRouter()

publisher = Publisher()
storage = StorageService()



@router.post("/publish/reel")
async def publish_reel(
    video: UploadFile = File(...),
    title: str = Form(""),
    description: str = Form(""),
):

    result = {
        "status": "completed",
        "cloudinary": None,
        "facebook": None,
        "instagram": None,
    }


    # -----------------------------
    # SALVATAGGIO FILE TEMPORANEO
    # -----------------------------

    file_path = f"/tmp/{video.filename}"

    with open(file_path, "wb") as f:
        f.write(
            await video.read()
        )


    # -----------------------------
    # CLOUDINARY
    # -----------------------------

    try:

        cloudinary_result = storage.upload_video(
            file_path
        )

        result["cloudinary"] = {
            "status": "uploaded",
            "url": cloudinary_result["url"],
            "public_id": cloudinary_result["public_id"],
        }


    except Exception as e:

        result["status"] = "failed"

        result["cloudinary"] = {
            "status": "error",
            "message": str(e),
        }

        return result



    # -----------------------------
    # REEL OBJECT
    # -----------------------------

    reel = Reel(
        video=file_path,
        title=title,
        description=description,
    )



    # -----------------------------
    # FACEBOOK
    # -----------------------------

    try:

        facebook_result = publisher.publish_facebook_reel(
            reel
        )

        result["facebook"] = {
            "status": "published",
            "data": facebook_result,
        }


    except Exception as e:

        result["status"] = "partial"

        result["facebook"] = {
            "status": "error",
            "message": str(e),
        }



    # -----------------------------
    # INSTAGRAM
    # -----------------------------

    try:

        instagram_result = publisher.publish_instagram_reel(
            video_url=result["cloudinary"]["url"],
            caption=description,
        )

        result["instagram"] = {
            "status": "published",
            "data": instagram_result,
        }


    except Exception as e:

        result["status"] = "partial"

        result["instagram"] = {
            "status": "error",
            "message": str(e),
        }



    return result