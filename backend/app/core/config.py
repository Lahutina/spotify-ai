import os
from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

OPENAI_MODEL = "gpt-4.1-mini"

SPOTIFY_CLIENT_ID = os.getenv(
    "SPOTIFY_CLIENT_ID"
)

SPOTIFY_CLIENT_SECRET = os.getenv(
    "SPOTIFY_CLIENT_SECRET"
)