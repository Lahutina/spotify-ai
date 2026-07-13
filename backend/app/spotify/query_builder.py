import random

from app.ai.schemas.music_profile import MusicProfile


VALID_SPOTIFY_GENRES = {
    "pop",
    "rock",
    "indie-pop",
    "indie-rock",
    "folk",
    "acoustic",
    "ambient",
    "chill",
    "jazz",
    "blues",
    "soul",
    "classical",
    "electronic",
    "house",
    "dance",
    "edm",
    "metal",
    "punk",
    "hip-hop",
    "rap",
    "country",
    "reggae",
    "latin",
}


def music_profile_to_search_queries(profile: MusicProfile):

    queries = []

    genres = [
        genre.lower().strip()
        for genre in profile.genres
        if genre.lower().strip() in VALID_SPOTIFY_GENRES
    ]

    if not genres:
        genres = ["pop"]

    for genre in genres:

        queries.append(f"genre:{genre}")

        queries.append(
            f"genre:{genre} {profile.mood}"
        )

        queries.append(
            f"genre:{genre} {profile.vocals}"
        )

        for instrument in profile.instruments:

            queries.append(
                f"genre:{genre} {instrument}"
            )

    random.shuffle(queries)

    return queries[:8]