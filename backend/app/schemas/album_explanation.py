from pydantic import BaseModel


class AlbumExplanation(BaseModel):
    
    artist: str

    album: str

    summary: str

    interesting_facts: list[str]