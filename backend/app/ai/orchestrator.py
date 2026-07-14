from app.ai.providers.openai_provider import OpenAIProvider
from app.schemas.music_profile import MusicProfile
from app.schemas.album_info import AlbumInfo
from app.schemas.album_explanation import AlbumExplanation
from app.core.prompt_loader import load_prompt
from app.musicbrainz.retriever import AlbumRetriever


class AIOrchestrator:
    def __init__(self):

        self.provider = OpenAIProvider()

        self.retriever = AlbumRetriever()

    def generate_music_profile(self, content) -> MusicProfile:

        prompt = load_prompt("music_profile.md")

        return self.provider.generate_music_profile(
            content=content,
            system_prompt=prompt,
        )

    def analyze_cover(self, image):

        album = self.identify_album(image)

        context = self.retriever.retrieve(
            album.artist,
            album.album,
        )

        return self.explain_album(context)

    def identify_album(self, image_content) -> AlbumInfo:

        prompt = load_prompt("identify_album.md")

        return self.provider.identify_album(
            image_content,
            prompt,
        )

    def explain_album(self, context: str) -> AlbumExplanation:

        prompt = load_prompt("explain_album.md")

        return self.provider.explain_album(
            context,
            prompt,
        )
