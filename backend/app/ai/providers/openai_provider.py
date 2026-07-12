from openai import OpenAI

from app.ai.providers.base import LLMProvider
from app.ai.schemas.music_profile import MusicProfile
from app.core.config import OPENAI_API_KEY, OPENAI_MODEL


class OpenAIProvider(LLMProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    def generate_music_profile(
        self,
        user_message: str,
        system_prompt: str
    ) -> MusicProfile:

        response = self.client.responses.parse(
            model=OPENAI_MODEL,
            input=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
            text_format=MusicProfile,
        )

        return response.output_parsed