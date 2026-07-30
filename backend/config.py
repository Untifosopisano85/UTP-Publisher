from dotenv import load_dotenv
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

ENV_FILE = BASE_DIR / ".env"

load_dotenv(
    ENV_FILE
)


# META

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")

PAGE_ID = os.getenv("PAGE_ID")
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")


GRAPH_API_VERSION = os.getenv(
    "GRAPH_API_VERSION",
    "v25.0"
)


# CLOUDINARY

CLOUDINARY_CLOUD_NAME = os.getenv(
    "CLOUDINARY_CLOUD_NAME"
)

CLOUDINARY_API_KEY = os.getenv(
    "CLOUDINARY_API_KEY"
)

CLOUDINARY_API_SECRET = os.getenv(
    "CLOUDINARY_API_SECRET"
)


# YOUTUBE

YOUTUBE_CLIENT_ID = os.getenv(
    "YOUTUBE_CLIENT_ID"
)

YOUTUBE_CLIENT_SECRET = os.getenv(
    "YOUTUBE_CLIENT_SECRET"
)

YOUTUBE_REFRESH_TOKEN = os.getenv(
    "YOUTUBE_REFRESH_TOKEN"
)
# TIKTOK

TIKTOK_CLIENT_KEY = os.getenv(
    "TIKTOK_CLIENT_KEY"
)

TIKTOK_CLIENT_SECRET = os.getenv(
    "TIKTOK_CLIENT_SECRET"
)

TIKTOK_ACCESS_TOKEN = os.getenv(
    "TIKTOK_ACCESS_TOKEN"
)