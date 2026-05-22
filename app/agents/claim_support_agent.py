from llm.llm_client import LLMClient
from prompts.claim_prompts import RAG_CLAIM_PROMPT
from logs.logger import get_logger
from retriever.retriever import get_retriever

logger = get_logger()
llm_client = LLMClient()
retriever = get_retriever()

def handle_claim_support_query(user_input: str) -> str:
    """
    Handles claim-related support queries using
    LLM-generated responses with safety-focused prompts.
    """

    try:
        logger.info("[AGENT] Claim Support Agent: Starting execution")
        
        # Retrieve relevant policy chunks (robust single-line fallback)
        retrieved_docs = (retriever.get_relevant_documents(user_input)
                          if hasattr(retriever, "get_relevant_documents")
                          else (retriever.retrieve(user_input)
                                if hasattr(retriever, "retrieve")
                                else (retriever(user_input) if callable(retriever) else [])))

        # Build retrieval context
        context = "\n\n".join(
            [doc.page_content for doc in retrieved_docs]
        )

        # Build prompt
        prompt = RAG_CLAIM_PROMPT.format(
            context=context,
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