import os
import json
import time
from dotenv import load_dotenv
import sys 

load_dotenv()

APP_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(APP_ROOT)

from evaluation.evaluation_test_cases import EVALUATION_TEST_CASES
from logs.logger import get_logger
from llm.llm_client import LLMClient
from prompts.policy_prompts import RAG_POLICY_PROMPT, SAFETY_POLICY_PROMPT
from retriever.retriever import get_retriever


logger = get_logger()


def safe_retriever_call(retriever, query):
    """
    Robustly call retriever to get relevant documents.
    Supports common LangChain retriever method names.
    """
    if retriever is None:
        return []
    if hasattr(retriever, "get_relevant_documents"):
        return retriever.get_relevant_documents(query)
    if hasattr(retriever, "retrieve"):
        return retriever.retrieve(query)
    if hasattr(retriever, "get_relevant_chunks"):
        return retriever.get_relevant_chunks(query)
    # last resort: if retriever is callable
    try:
        return retriever(query)
    except Exception:
        return []


def keyword_score(response: str, keywords: list):
    r = (response or "").lower()
    return sum(1 for k in keywords if k.lower() in r)


def run_comparison(output_path="app/evaluation/retrieval_comparison_results.json"):
    llm = LLMClient()
    retriever = get_retriever()
    results = []

    for case in EVALUATION_TEST_CASES:
        query = case.get("query")
        expected_keywords = case.get("evaluation_keywords", [])
        repeat = case.get("repeat_count", 1)

        no_rag_times = []
        rag_times = []
        no_rag_responses = []
        rag_responses = []

        for _ in range(repeat):
            t0 = time.time()
            no_rag = llm.ask(SAFETY_POLICY_PROMPT.format(user_query=query))
            t1 = time.time()
            no_rag_times.append(t1 - t0)
            no_rag_responses.append(no_rag)

            # Retrieval
            retrieved_docs = safe_retriever_call(retriever, query)
            retrieved_text = " \n ".join(getattr(d, "page_content", "") for d in retrieved_docs) if retrieved_docs else ""
            context = "\n\n".join(getattr(d, "page_content", str(d)) for d in retrieved_docs) if retrieved_docs else ""

            rag_prompt = RAG_POLICY_PROMPT.format(
                context=context,
                user_query=query,
                adaptive_instruction="No adaptive behaviour required."
            )

            t2 = time.time()
            rag = llm.ask(rag_prompt)
            t3 = time.time()
            rag_times.append(t3 - t2)
            rag_responses.append(rag)

        no_rag_resp = no_rag_responses[-1] if no_rag_responses else ""
        rag_resp = rag_responses[-1] if rag_responses else ""

        no_rag_score = keyword_score(no_rag_resp, expected_keywords)
        rag_score = keyword_score(rag_resp, expected_keywords)

        # Evaluate retrieval expectations
        retrieval_missing = False
        expected_retrieval_matches = 0
        expected_retrieval_keywords = case.get("expected_retrieval_keywords", [])

        if case.get("requires_retrieval") and not retrieved_docs:
            retrieval_missing = True

        if expected_retrieval_keywords and retrieved_text:
            for ek in expected_retrieval_keywords:
                if ek.lower() in retrieved_text.lower():
                    expected_retrieval_matches += 1

        result = {
            "category": case.get("category"),
            "query": query,
            "repeat_count": repeat,
            "no_rag": {
                "response": no_rag_resp,
                "median_latency_s": sorted(no_rag_times)[len(no_rag_times)//2] if no_rag_times else None,
                "keyword_score": no_rag_score
            },
            "rag": {
                "response": rag_resp,
                "median_latency_s": sorted(rag_times)[len(rag_times)//2] if rag_times else None,
                "keyword_score": rag_score,
                "retrieved_count": len(retrieved_docs) if 'retrieved_docs' in locals() else 0,
                "retrieval_missing": retrieval_missing,
                "expected_retrieval_matches": expected_retrieval_matches
            }
        }

        logger.info(f"[EVAL] {query} => no_rag score {no_rag_score}, rag score {rag_score}")
        results.append(result)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, ensure_ascii=False)

    print(f"Saved results to {output_path}")
    return results


if __name__ == "__main__":
    run_comparison()
