import base64

from pydantic import BaseModel
from fastapi import (
    APIRouter,
    UploadFile,
    File
)

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
async def analyze_text(
    request: ChatRequest,
):
    return orchestrator.generate_music_profile(request.message)



@router.post(
    "/analyze/image",
    response_model=MusicProfile,
)
async def analyze_image(
    file: UploadFile = File(...),
):

    content = encode_image(file)

    return orchestrator.generate_music_profile(content)


def encode_image(file: UploadFile) -> list[dict]:

    image_bytes = file.file.read()

    image_base64 = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    return [
        {
            "type": "input_text",
            "text": "Analyze this image and create a music profile."
        },
        {
            "type": "input_image",
            "image_url": (
                f"data:{file.content_type};base64,{image_base64}"
            )
        }
    ]
