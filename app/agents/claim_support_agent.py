from llm.llm_client import LLMClient
from prompts.claim_prompts import BASE_CLAIM_PROMPT
from logs.logger import get_logger

logger = get_logger()
llm_client = LLMClient()


def handle_claim_support_query(user_input: str) -> str:
    """
    Handles claim-related support queries using
    LLM-generated responses with safety-focused prompts.
    """

    try:
        logger.info("[AGENT] Claim Support Agent: Starting execution")
        
        # Build prompt
        prompt = BASE_CLAIM_PROMPT.format(
            user_query=user_input
        )

        # Generate response
        response = llm_client.ask(prompt)
        logger.info("[AGENT] Claim Support Agent: Response received")

        return response

    except Exception as error:
        logger.error(f"[AGENT] Claim Support Agent: Error - {str(error)}")
        return (
            "I'm unable to process the claims support request at the moment. "
            "Please try again later or contact customer support."
        )