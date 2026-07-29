from dotenv import load_dotenv
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

ENV_FILE = BASE_DIR / ".env"


load_dotenv(
    ENV_FILE
)


UTP_API_KEY = os.getenv(
    "UTP_API_KEY"
)