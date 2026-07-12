from pydantic import BaseModel, Field


class MusicProfile(BaseModel):
    mood: str = Field(description="Dominant mood")
    energy: float = Field(ge=0, le=1)
    valence: float = Field(ge=0, le=1)

    genres: list[str]

    activities: list[str]

    explanation: str