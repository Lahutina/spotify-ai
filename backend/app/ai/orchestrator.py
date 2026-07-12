from app.ai.providers.openai_provider import OpenAIProvider

from app.ai.schemas.music_profile import MusicProfile

from app.core.prompt_loader import load_prompt


class AIOrchestrator:

    def __init__(self):

        self.provider = OpenAIProvider()

    def generate_music_profile(
        self,
        user_message: str
    ) -> MusicProfile:

        prompt = load_prompt(
            "music_profile.md"
        )

        return self.provider.generate_music_profile(
            user_message=user_message,
            system_prompt=prompt,
        )