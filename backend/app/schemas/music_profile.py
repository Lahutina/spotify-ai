from pydantic import BaseModel, Field


class MusicProfile(BaseModel):
    
    mood: str = Field(description="Dominant mood")

    genres: list[str]

    activities: list[str]

    instruments: list[str]

    vocals: str

    explanation: str