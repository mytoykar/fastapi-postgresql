import os

from dotenv import load_dotenv

load_dotenv(".env")

SQLALCHEMY_DB_URL = os.getenv("SQLALCHEMY_DB_URL", "")
