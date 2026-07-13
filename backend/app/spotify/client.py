import spotipy


class SpotifyClient:

    def __init__(
        self,
        client: spotipy.Spotify
    ):
        self.client = client


    def search_tracks(
        self,
        query: str
    ) -> list[dict]:

        result = self.client.search(
            q=query,
            type="track",
            limit=10
        )

        tracks = result["tracks"]["items"]

        return [
            {
                "name": track["name"],
                "artist": track["artists"][0]["name"],
                "album": track["album"]["name"],
                "image": track["album"]["images"][0]["url"]
                    if track["album"]["images"]
                    else None,
                "spotify_url": track["external_urls"]["spotify"]
            }
            for track in tracks
        ]