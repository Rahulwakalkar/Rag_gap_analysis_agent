from groq import Groq
from app.core.config import settings

class GroqLLM:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)

    def invoke(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=settings.GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        return response.choices[0].message.content