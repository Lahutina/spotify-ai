from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.orchestrator import AIOrchestrator
from app.ai.schemas.music_profile import MusicProfile


router = APIRouter()


class ChatRequest(BaseModel):
    message: str


orchestrator = AIOrchestrator()


@router.post(
    "/analyze/mood",
    response_model=MusicProfile,
)
def chat(
    request: ChatRequest,
):

    return orchestrator.generate_music_profile(request.message)
