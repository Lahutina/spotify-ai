import spotipy


class SpotifyAPI:
    def __init__(self, client: spotipy.Spotify):
        self.client = client

    def search_tracks(self, query: str) -> list[dict]:

        result = self.client.search(
            q=query,
            type="track",
            limit=10,
        )

        return result["tracks"]["items"]
