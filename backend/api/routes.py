from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    Depends,
)

from services.publisher import Publisher
from services.storage import StorageService
from models import Reel

from security import verify_api_key


router = APIRouter()

publisher = Publisher()
storage = StorageService()



@router.get("/health")
async def health():

    return {
        "status": "online"
    }



@router.post(
    "/publish/reel",
    dependencies=[
        Depends(verify_api_key)
    ]
)
async def publish_reel(
    video: UploadFile = File(...),
    title: str = Form(""),
    description: str = Form(""),

    facebook: bool = Form(True),
    instagram: bool = Form(True),
):


    result = {

        "status": "completed",

        "cloudinary": None,

        "facebook": None,

        "instagram": None,
    }



    selected_platforms = []


    if facebook:

        selected_platforms.append(
            "facebook"
        )


    if instagram:

        selected_platforms.append(
            "instagram"
        )



    # -----------------------------
    # SALVATAGGIO VIDEO TEMPORANEO
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

        return {

            "success": False,

            "message": "Errore caricamento video",

            "platforms": {},

            "error": str(e),
        }



    # -----------------------------
    # CREAZIONE REEL
    # -----------------------------

    reel = Reel(

        video=file_path,

        title=title,

        description=description,

        platforms=selected_platforms,
    )



    # -----------------------------
    # FACEBOOK
    # -----------------------------

    if facebook:

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


    else:

        result["facebook"] = {

            "status": "not_selected"
        }




    # -----------------------------
    # INSTAGRAM
    # -----------------------------

    if instagram:

        try:

            instagram_result = publisher.publish_instagram_reel(
                video_url=result["cloudinary"]["url"],
                caption=reel.full_description,
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


    else:

        result["instagram"] = {

            "status": "not_selected"
        }




    # -----------------------------
    # RISPOSTA PER CLIENT MOBILE
    # -----------------------------

    return {

        "success": result["status"] != "failed",

        "message": (

            "Reel pubblicato correttamente"

            if result["status"] == "completed"

            else "Pubblicazione completata con errori"
        ),


        "platforms": {

            "facebook": result["facebook"]["status"],

            "instagram": result["instagram"]["status"],
        },

    }