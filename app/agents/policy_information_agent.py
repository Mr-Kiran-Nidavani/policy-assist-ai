from llm.llm_client import LLMClient
from prompts.policy_prompts import RAG_POLICY_PROMPT
from retriever.retriever import get_retriever
from logs.logger import get_logger
from feedback.feedback_utils import should_use_adaptive_response

llm_client = LLMClient()
retriever = get_retriever()
logger = get_logger()


def handle_policy_information_query(user_input: str) -> str:
    """
    Handles policy information queries
    using Retrieval-Augmented Generation (RAG).
    """

    try:
        logger.info("[AGENT] Policy Information Agent: Starting execution")
        
        # Retrieve relevant policy chunks (robustly support different retriever APIs)
        if hasattr(retriever, "get_relevant_documents"):
            retrieved_docs = retriever.get_relevant_documents(user_input)
        elif hasattr(retriever, "retrieve"):
            retrieved_docs = retriever.retrieve(user_input)
        elif callable(retriever):
            try:
                retrieved_docs = retriever(user_input)
            except Exception:
                retrieved_docs = []
        else:
            retrieved_docs = []
        
        # Build retrieval context
        context = "\n\n".join(
            [doc.page_content for doc in retrieved_docs]
        )

        # ---------------------------------------------------
        # Adaptive Behaviour Logic
        # ---------------------------------------------------

        adaptive_instruction = "No adaptive behaviour required."

        if should_use_adaptive_response("policy_information"):

           adaptive_instruction = """
                Previous responses for policy information
                queries received repeated negative feedback.

                IMPORTANT:
                The customer expects a more detailed,
                better structured, and easier to understand response.

                Response Requirements:
                - Add clear section headings
                - Use bullet points
                - Include practical examples
                - Explain exclusions separately
                - Explain deductibles separately
                - Expand important considerations
                - Provide richer customer guidance
                - Use a more educational explanation style

                You may provide longer responses when needed.
            """

        # Build grounded RAG prompt
        prompt = RAG_POLICY_PROMPT.format(
            context=context,
            user_query=user_input,
            adaptive_instruction=adaptive_instruction
        )

        # Generate grounded response
        response = llm_client.ask(prompt)
        logger.info(f"[AGENT] Policy Information Agent: Response received")

        return response

    except Exception as error:
        logger.error(f"[AGENT] Policy Information Agent: Error - {str(error)}")
        return (
            "I'm unable to process the policy information request at the moment. "
            "Please try again later or contact customer support."
        )