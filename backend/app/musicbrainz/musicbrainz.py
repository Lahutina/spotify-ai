import requests


BASE_URL = "https://musicbrainz.org/ws/2"


class MusicBrainzSource:
    def search_release(
        self,
        artist: str,
        album: str,
    ):

        query = f'release:"{album}" AND artist:"{artist}"'

        response = requests.get(
            f"{BASE_URL}/release/",
            params={
                "query": query,
                "fmt": "json",
            },
            headers={"User-Agent": "SpotifyAI/1.0"},
            timeout=15,
        )

        response.raise_for_status()

        releases = response.json()["releases"]

        if not releases:
            return None

        return releases[0]
