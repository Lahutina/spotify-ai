import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

from app.spotify.client import SpotifyClient
from app.spotify.service import SpotifyService
from app.core.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


def get_spotify_service():

    spotify = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET
        )
    )

    client = SpotifyClient(spotify)

    return SpotifyService(client)