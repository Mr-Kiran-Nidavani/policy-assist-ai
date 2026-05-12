from llm.llm_client import LLMClient
from prompts.policy_prompts import SAFETY_POLICY_PROMPT


llm_client = LLMClient()


def handle_policy_information_query(user_input: str) -> str:
    """
    Handles policy-related support queries using
    LLM-generated responses with safety-focused prompts.
    """

    try:
        # Build prompt
        prompt = SAFETY_POLICY_PROMPT.format(
            user_query=user_input
        )

        # Generate response
        response = llm_client.ask(prompt)

        return response

    except Exception as error:
        return (
            "I'm unable to process the policy information request at the moment. "
            "Please try again later or contact customer support."
        )