from llm.llm_client import LLMClient
from prompts.claim_prompts import SAFETY_CLAIM_PROMPT


llm_client = LLMClient()


def handle_claim_support_query(user_input: str) -> str:
    """
    Handles claim-related support queries using
    LLM-generated responses with safety-focused prompts.
    """

    try:
        # Build prompt
        prompt = SAFETY_CLAIM_PROMPT.format(
            user_query=user_input
        )

        # Generate response
        response = llm_client.ask(prompt)

        return response

    except Exception:
        return (
            "I'm unable to process the claims support request at the moment. "
            "Please try again later or contact customer support."
        )