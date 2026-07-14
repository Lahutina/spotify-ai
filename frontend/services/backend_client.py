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


def analyze_image(image):

    response = requests.post(
        f"{BACKEND_URL}/analyze/image",
        files={
            "file": (
                image.name,
                image.getvalue(),
                image.type
            )
        }
    )

    response.raise_for_status()

    return response.json()


def get_recommendations(profile):

    response = requests.post(
        f"{BACKEND_URL}/recommend",
        json=profile
    )

    response.raise_for_status()

    return response.json()


def analyze_album_cover(image):

    response = requests.post(
        f"{BACKEND_URL}/analyze/album",
        files={
            "file": (
                image.name,
                image,
                image.type
            )
        }
    )

    response.raise_for_status()

    return response.json()