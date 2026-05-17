from llm.llm_client import LLMClient
from prompts.general_prompts import GENERAL_SUPPORT_PROMPT
from logs.logger import get_logger

logger = get_logger()
llm_client = LLMClient()


def handle_general_query(user_input: str) -> str:
    """
    Handles general insurance support queries using
    LLM-generated responses.
    """

    try:
        logger.info("[AGENT] General Query Agent: Starting execution")
        
        # Build prompt
        prompt = GENERAL_SUPPORT_PROMPT.format(
            user_query=user_input
        )

        # Generate response
        response = llm_client.ask(prompt)
        logger.info("[AGENT] General Query Agent: Response received")

        return response

    except Exception as error:
        logger.error(f"[AGENT] General Query Agent: Error - {str(error)}")
        return (
            "I'm unable to process the request at the moment. "
            "Please try again later."
        )