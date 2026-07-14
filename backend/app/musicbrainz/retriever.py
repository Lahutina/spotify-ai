from app.musicbrainz.musicbrainz import MusicBrainzSource


class AlbumRetriever:
    def __init__(self):

        self.musicbrainz = MusicBrainzSource()

    def retrieve(self, artist: str, album: str) -> str:

        data = self.musicbrainz.search_release(
            artist,
            album,
        )

        if not data:
            return "No information found."

        return f"""
                Artist:
                {artist}

                Album:
                {album}

                Release date:
                {data.get("date")}

                Country:
                {data.get("country")}

                Label:
                {data.get("label-info")}

                Genres:
                {data.get("tags")}
                """
