import requests

from config import BACKEND_URL


def analyze_mood(message: str):

    response = requests.post(
        f"{BACKEND_URL}/analyze/mood",
        json={
            "message": message
        }
    )

    response.raise_for_status()

    return response.json()