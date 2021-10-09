import os
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).parent

#  Develop
DEBUG = os.getenv("DEBUG", "True").lower() == "true"


# Database
POSTGRES_USER = os.getenv("POSTGRES_USER", "MoreTech")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "MoreTech")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
POSTGRES_DATABASE_NAME = os.getenv("POSTGRES_DATABASE_NAME", "MoreTech")
DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE_NAME}"
