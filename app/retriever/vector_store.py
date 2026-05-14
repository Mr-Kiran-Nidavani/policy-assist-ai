from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from retriever.document_loader import load_policy_documents
from retriever.text_splitter import split_documents

from logs.logger import get_logger

import os


logger = get_logger()

VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH",
    "data/embeddings"
)


def build_vector_store():
    """
    Loads documents, splits them into chunks,
    generates embeddings, and stores them in ChromaDB.
    """

    logger.info("Starting vector database build process")

    # Load documents
    documents = load_policy_documents()

    logger.info(f"Loaded documents/pages: {len(documents)}")

    # Split into chunks
    chunks = split_documents(documents)

    logger.info(f"Generated text chunks: {len(chunks)}")

    if chunks:

        logger.info("Sample chunk preview:")
        logger.info(chunks[0].page_content[:300])

    # Create embeddings model
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.getenv("OPENAI_API_BASE"),
        model=os.getenv(
            "EMBEDDING_MODEL",
            "text-embedding-3-small"
        )
    )

    logger.info("Embedding model initialized")

    # Build vector database
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH,
        collection_name="policy_assist"
    )

    logger.info("Chroma vector database created successfully")

    logger.info(f"Persisted vector DB path: {VECTOR_DB_PATH}")

    logger.info(f"Stored vectors: {vector_store._collection.count()}")

    return vector_store