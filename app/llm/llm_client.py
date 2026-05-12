# app/llm/llm_client.py

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()


class LLMClient:
    """
    Centralized LangChain OpenAI client
    for PolicyAssist AI.
    """

    def __init__(self):
        self.llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE"),  # Optional
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            temperature=float(os.getenv("TEMPERATURE", 0.3)),
            max_tokens=int(os.getenv("MAX_TOKENS", 512)),
            timeout=30,
            max_retries=2,
        )

    def ask(self, prompt: str) -> str:
        """
        Executes LLM request using prompt string.
        """

        response = self.llm.invoke(prompt)

        return response.content

    def get_model(self):
        """
        Returns underlying LangChain model.
        """

        return self.llm