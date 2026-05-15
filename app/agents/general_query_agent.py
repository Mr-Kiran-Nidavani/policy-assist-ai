from llm.llm_client import LLMClient
from prompts.general_prompts import GENERAL_SUPPORT_PROMPT


llm_client = LLMClient()


def handle_general_query(user_input: str) -> str:
    """
    Handles general insurance support queries using
    LLM-generated responses.
    """

    try:
        # Build prompt
        prompt = GENERAL_SUPPORT_PROMPT.format(
            user_query=user_input
        )

        # Generate response
        response = llm_client.ask(prompt)

        return response

    except Exception:
        return (
            "I'm unable to process the request at the moment. "
            "Please try again later."
        )