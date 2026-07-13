from fastapi import FastAPI
from app.api.analysis import router as chat_router
from app.api.recommendations import router as spotify_router

app = FastAPI(
    title="Spotify-AI",
    description="AI music assistant powered by Generative AI",
    version="0.1"
)

app.include_router(chat_router)
app.include_router(spotify_router)