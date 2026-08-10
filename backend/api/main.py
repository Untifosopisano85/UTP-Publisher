from fastapi import FastAPI, UploadFile, File

from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path

import shutil

from api.schemas import PublishRequest

from models.publication import Publication

from services.publication_pipeline import PublicationPipeline

from services.publication_history import PublicationHistory


app = FastAPI(
    title="UTP Publisher",
    version="0.1"
)


app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "https://enthusiastic-wonder-production-610e.up.railway.app"
    ],

    allow_credentials=True,

    allow_methods=[
        "*"
    ],

    allow_headers=[
        "*"
    ],
)


UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(
    exist_ok=True
)


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.get("/")
def home():

    return {

        "app": "UTP Publisher",

        "status": "running"

    }


# --------------------------------------------------
# UPLOAD VIDEO
# --------------------------------------------------

@app.post("/upload")
async def upload_video(
    file: UploadFile = File(...)
):

    file_path = UPLOAD_DIR / file.filename


    with file_path.open("wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    return {

        "filename": file.filename,

        "path": str(file_path)

    }


# --------------------------------------------------
# PUBBLICAZIONE
# --------------------------------------------------

@app.post("/publish")
def publish(
    request: PublishRequest
):

    publication = Publication(

        video_path=request.video_path,

        platforms=request.platforms,

        youtube_title=request.youtube_title,

        youtube_description=request.youtube_description,

        facebook_message=request.facebook_message,

        instagram_caption=request.instagram_caption,

        tiktok_caption=request.tiktok_caption

    )


    pipeline = PublicationPipeline()

    result = pipeline.publish(publication)


    history = PublicationHistory()

    history.save(result)


    return result


# --------------------------------------------------
# PUBBLICAZIONI
# --------------------------------------------------

@app.get("/publications")
def publications():

    history = PublicationHistory()

    return history.all()


@app.get("/publications/{publication_id}")
def publication_detail(
    publication_id: str
):

    history = PublicationHistory()

    return history.get(publication_id)