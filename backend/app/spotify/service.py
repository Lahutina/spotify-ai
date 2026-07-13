import random

from app.spotify.query_builder import (
    music_profile_to_search_queries
)



class SpotifyService:

    def __init__(
        self,
        client
    ):
        self.client = client


    def recommend(
        self,
        profile
    ):

        queries = music_profile_to_search_queries(
            profile
        )

        tracks = []

        for query in queries:

            results = self.client.search_tracks(
                query
            )

            tracks.extend(results)


        # remove duplicates
        unique_tracks = []

        seen = set()

        for track in tracks:

            key = track["spotify_url"]

            if key not in seen:
                seen.add(key)
                unique_tracks.append(track)


        random.shuffle(unique_tracks)

        return unique_tracks[:20]

