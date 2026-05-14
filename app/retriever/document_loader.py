from pathlib import Path
import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader


POLICY_DATA_PATH = os.getenv(
    "POLICY_DATA_PATH",
    "data/policies"
)


def load_policy_documents():
    """
    Loads policy documents from the policies directory.
    Supports:
    - PDF
    - TXT
    """

    documents = []

    folder_path = Path(POLICY_DATA_PATH)

    for file_path in folder_path.iterdir():

        try:
            if file_path.suffix == ".pdf":
                loader = PyPDFLoader(str(file_path))
                documents.extend(loader.load())

            elif file_path.suffix == ".txt":
                loader = TextLoader(
                    str(file_path),
                    encoding="utf-8"
                )
                documents.extend(loader.load())

        except Exception as error:
            print(f"Error loading {file_path.name}: {error}")

    print(f"Loaded {len(documents)} documents/pages")

    return documents