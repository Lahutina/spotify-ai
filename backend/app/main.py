from fastapi import FastAPI


app = FastAPI(
    title="Spotify-AI",
    description="AI music assistant powered by Generative AI",
    version="0.1"
)


@app.get("/")
def home():
    return {
        "message": "Spotify-AI backend is running"
    }