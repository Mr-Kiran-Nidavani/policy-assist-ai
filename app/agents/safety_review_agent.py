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
        logger.info("[SAFETY] Status: RESTRICTED - Operation blocked")
        return RESTRICTED_RESPONSE
    
    # Approved low-risk operational workflows
    if intent == "policy_update":
        logger.info("[SAFETY] Status: APPROVED - Low-risk policy update")
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
            logger.info("[SAFETY] Status: RESTRICTED - Response blocked")
            return RESTRICTED_RESPONSE

        elif safety_result == "ESCALATE":
            logger.info("[SAFETY] Status: ESCALATE - Human review required")
            return ESCALATION_RESPONSE

        logger.info("[SAFETY] Status: SAFE - Response approved")
        return response

    except Exception as error:
        # Fail-safe fallback
        logger.error(f"[SAFETY] Safety review failed: {str(error)}")
        return ESCALATION_RESPONSE