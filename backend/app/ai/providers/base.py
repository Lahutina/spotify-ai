from abc import ABC, abstractmethod

from app.schemas.music_profile import MusicProfile


class LLMProvider(ABC):

    @abstractmethod
    def generate_music_profile(
        self,
        user_message: str,
        system_prompt: str
    ) -> MusicProfile:
        pass