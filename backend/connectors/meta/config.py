from dotenv import load_dotenv
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

ENV_FILE = BASE_DIR / ".env"

load_dotenv(
    ENV_FILE
)

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")

PAGE_ID = os.getenv("PAGE_ID")
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")

INSTAGRAM_ACCOUNT_ID = os.getenv(
    "INSTAGRAM_ACCOUNT_ID"
)

GRAPH_API_VERSION = os.getenv(
    "GRAPH_API_VERSION",
    "v25.0"
)

CLOUDINARY_CLOUD_NAME = os.getenv(
    "CLOUDINARY_CLOUD_NAME"
)

CLOUDINARY_API_KEY = os.getenv(
    "CLOUDINARY_API_KEY"
)

CLOUDINARY_API_SECRET = os.getenv(
    "CLOUDINARY_API_SECRET"
)