from llm.llm_client import LLMClient
from prompts.router_prompts import INTENT_ROUTER_PROMPT


llm_client = LLMClient()


VALID_INTENTS = {
    "policy_information",
    "claim_support",
    "policy_update",
    "restricted_operation",
    "general_query",
    "customer_policy_query",
    "unknown",
}


def detect_intent(user_input: str) -> str:
    """
    Detects user intent using LLM classification.
    """

    try:
        prompt = INTENT_ROUTER_PROMPT.format(
            user_query=user_input
        )

        response = llm_client.ask(prompt)

        intent = response.strip().lower()

        if intent in VALID_INTENTS:
            return intent

        return "unknown"

    except Exception:
        return "unknown"