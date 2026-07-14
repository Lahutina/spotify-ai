from pydantic import BaseModel

class AlbumInfo(BaseModel):
    
    artist: str

    album: str