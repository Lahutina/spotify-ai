import random

from app.spotify.query_builder import music_profile_to_search_queries


class SpotifyRecommender:
    def __init__(self, api):
        self.api = api

    def recommend(self, profile):

        queries = music_profile_to_search_queries(profile)

        tracks = []

        for query in queries:
            tracks.extend(self.api.search_tracks(query))

        unique = {}

        for track in tracks:
            unique[track["id"]] = track

        recommendations = list(unique.values())

        random.shuffle(recommendations)

        return [
            {
                "name": track["name"],
                "artist": track["artists"][0]["name"],
                "album": track["album"]["name"],
                "image": track["album"]["images"][0]["url"]
                if track["album"]["images"]
                else None,
                "spotify_url": track["external_urls"]["spotify"],
            }
            for track in recommendations[:20]
        ]
