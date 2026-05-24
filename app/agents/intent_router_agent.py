import re

from llm.llm_client import LLMClient
from prompts.router_prompts import INTENT_ROUTER_PROMPT
from logs.logger import get_logger
import json


logger = get_logger()
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


def detect_intent(user_input: str, conversation_history: str) -> str:
    """
    Detects user intent using LLM classification.
    """

    try:
        prompt = INTENT_ROUTER_PROMPT.format(
            user_query=user_input,
            conversation_history=conversation_history
        )

        response = llm_client.ask(prompt)
        response = re.sub(r"```json|```", "", response).strip()
        result = json.loads(response)
        intent = result.get("intent", "unknown").lower().strip()

        if intent not in VALID_INTENTS:
            intent = "unknown"

        result["intent"] = intent
        logger.info(f"[ROUTER] Intent detected: {intent}")
        return result

    except Exception as error:
        logger.error(f"[ROUTER] Failed to detect intent: {str(error)}")
        return {
            "intent": "unknown",
            "customer_id": None,
            "requires_customer_id": False
        }