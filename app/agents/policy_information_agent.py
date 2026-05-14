from llm.llm_client import LLMClient
from prompts.policy_prompts import RAG_POLICY_PROMPT
from retriever.retriever import get_retriever

llm_client = LLMClient()
retriever = get_retriever()

def handle_policy_information_query(user_input: str) -> str:
    """
    Handles policy information queries
    using Retrieval-Augmented Generation (RAG).
    """

    # Retrieve relevant policy chunks
    retrieved_docs = retriever.invoke(user_input)
  
    # Build retrieval context
    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    # Build grounded RAG prompt
    prompt = RAG_POLICY_PROMPT.format(
        context=context,
        user_query=user_input
    )

    # Generate grounded response
    response = llm_client.ask(prompt)

    return response