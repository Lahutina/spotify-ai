from fastapi import APIRouter, Depends

from app.schemas.music_profile import MusicProfile
from app.spotify.dependencies import get_spotify
from app.spotify.recommender import SpotifyRecommender


router = APIRouter()


@router.post("/recommend")
def recommend(
    profile: MusicProfile,
    spotify: SpotifyRecommender = Depends(get_spotify),
):

    tracks = spotify.recommend(profile)

    return {"tracks": tracks}
