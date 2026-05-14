import os

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH",
    "data/embeddings"
)

TOP_K = int(os.getenv("TOP_K", 5))


def get_retriever():
    """
    Loads persisted Chroma vector database
    and returns a semantic retriever.
    """

    embeddings = OpenAIEmbeddings(
        openai_api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.getenv("OPENAI_API_BASE"),
        model=os.getenv(
            "EMBEDDING_MODEL",
            "text-embedding-3-small"
        )
    )

    vectorstore = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings,
        collection_name="policy_assist"
    )

    print(
        "Stored vectors:",
        vectorstore._collection.count()
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K}
    )

    return retriever