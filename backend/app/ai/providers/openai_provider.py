from openai import OpenAI

from app.ai.providers.base import LLMProvider
from app.schemas.music_profile import MusicProfile
from app.schemas.album_info import AlbumInfo
from app.schemas.album_explanation import AlbumExplanation
from app.core.config import OPENAI_API_KEY, OPENAI_MODEL


class OpenAIProvider(LLMProvider):
    def __init__(self):

        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate_music_profile(self, content, system_prompt: str) -> MusicProfile:

        response = self.client.responses.parse(
            model=OPENAI_MODEL,
            input=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": content,
                },
            ],
            text_format=MusicProfile,
        )

        return response.output_parsed

    def identify_album(self, image_content, system_prompt) -> AlbumInfo:

        response = self.client.responses.parse(
            model=OPENAI_MODEL,
            input=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": image_content,
                },
            ],
            text_format=AlbumInfo,
        )

        return response.output_parsed

    def explain_album(self, context, system_prompt) -> AlbumExplanation:

        response = self.client.responses.parse(
            model=OPENAI_MODEL,
            input=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": context,
                },
            ],
            text_format=AlbumExplanation,
        )

        return response.output_parsed
