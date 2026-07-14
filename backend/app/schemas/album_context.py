from pydantic import BaseModel


class AlbumContext(BaseModel):
    
    artist: str

    album: str

    release_date: str | None = None

    country: str | None = None

    genres: list[str] = []

    labels: list[str] = []

    track_count: int | None = None

    context: str
