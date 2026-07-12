from fastapi import FastAPI
from app.api.chat import router as chat_router


app = FastAPI(
    title="Spotify-AI",
    description="AI music assistant powered by Generative AI",
    version="0.1"
)

app.include_router(chat_router)