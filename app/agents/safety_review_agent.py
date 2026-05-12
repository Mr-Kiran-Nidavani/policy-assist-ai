from llm.llm_client import LLMClient
from prompts.safety_prompts import SAFETY_REVIEW_PROMPT
from logs.logger import get_logger

logger = get_logger()
llm_client = LLMClient()


RESTRICTED_RESPONSE = (
    "I'm unable to assist with this request because it involves restricted "
    "or unauthorized operations. Please contact an authorized insurance "
    "representative or support specialist for further assistance."
)


ESCALATION_RESPONSE = (
    "This request may require review by a licensed insurance representative "
    "or claims specialist for accurate assistance."
)


def review_response(
    user_input: str,
    intent: str,
    response: str
) -> str:
    """
    Performs LLM-based safety validation
    before returning responses to users.
    """

    # Restricted operations blocked immediately
    if intent == "restricted_operation":
        logger.warning("Restricted operation blocked")
        return RESTRICTED_RESPONSE
    
    # Approved low-risk operational workflows
    if intent == "policy_update":
        logger.info("Policy update request completed successfully")
        return response

    try:
        # Build safety review prompt
        prompt = SAFETY_REVIEW_PROMPT.format(
            user_query=user_input,
            intent=intent,
            response=response
        )

        # Run safety classification
        safety_result = llm_client.ask(prompt)

        safety_result = safety_result.strip().upper()

        # Enforce final decision
        if safety_result == "RESTRICTED":
            logger.warning("Restricted operation blocked")
            return RESTRICTED_RESPONSE

        elif safety_result == "ESCALATE":
            logger.warning("Response escalated for human review")
            return ESCALATION_RESPONSE

        logger.info("Safe response approved")
        return response

    except Exception:
        # Fail-safe fallback
        logger.error("Safety review agent failed")
        return ESCALATION_RESPONSE