import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#  Develop
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
