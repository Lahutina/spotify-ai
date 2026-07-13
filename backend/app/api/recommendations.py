from fastapi import APIRouter, Depends

from app.ai.schemas.music_profile import MusicProfile
from app.spotify.dependencies import get_spotify_service


router = APIRouter()


@router.post("/recommend")
def recommend(
    profile: MusicProfile,
    service = Depends(get_spotify_service)
):

    tracks = service.recommend(profile)

    return {
        "tracks": tracks
    }