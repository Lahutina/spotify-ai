import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
from app.spotify.spotify_api import SpotifyAPI
from app.spotify.recommender import SpotifyRecommender

from app.core.config import (
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET,
)


def get_spotify():

    client = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
        )
    )

    api = SpotifyAPI(client)

    return SpotifyRecommender(api)