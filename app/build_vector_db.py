from retriever.vector_store import build_vector_store
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    vector_store = build_vector_store()

    print("Vector database created successfully.")