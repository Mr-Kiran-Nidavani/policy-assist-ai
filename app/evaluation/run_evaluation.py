import json
import time
from datetime import datetime
import os
import sys

APP_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(APP_ROOT)

from evaluation.evaluation_test_cases import (
    EVALUATION_TEST_CASES
)

from main import process_user_query


def evaluate_response(response: str,  evaluation_keywords: list):
    """
    Keyword-based evaluation scoring.
    """

    response_lower = response.lower()

    matched = 0

    for keyword in evaluation_keywords:
        if keyword.lower() in response_lower:
            matched += 1

    score = round((matched / len(evaluation_keywords)) * 100, 2 )

    return score


def save_evaluation_result(result):

    file_path = ("app/evaluation/evaluation_results.json")

    try:
        with open(file_path, "r") as file:
            existing_results = json.load(file)

    except Exception:
        existing_results = []

    existing_results.append(result)

    with open(file_path, "w") as file:
        json.dump(existing_results, file, indent=2  )


def run_evaluation():

    print("\n=== Phase 9 Evaluation Runner ===\n")

    results = []

    for index, test_case in enumerate(EVALUATION_TEST_CASES, start=1 ):

        query = test_case["query"]
        category = test_case["category"]
        evaluation_keywords = test_case["evaluation_keywords"]

        repeat_count = test_case.get(
            "repeat_count",
            1
        )

        print(f"\nTest Case {index}")
        print(f"Category: {category}")
        print(f"Query: {query}")

        responses = []

        scores = []

        latencies = []

        for attempt in range(repeat_count):

            start_time = time.time()

            result = process_user_query(query)

            latency = round(
                time.time() - start_time,
                2
            )

            response = result["response"]

            score = evaluate_response(response=response, evaluation_keywords=evaluation_keywords)
            responses.append(response)
            scores.append(score)
            latencies.append(latency)

        average_score = round(sum(scores) / len(scores), 2 )
        average_latency = round(sum(latencies) / len(latencies), 2)
        response = responses[-1]
        print(f"\nResponse:\n{response}")
        print(f"\nAverage Evaluation Score: {average_score}%")

        print(f"Average Latency: {average_latency}s")
        print(f"Consistency Runs: {repeat_count}")

        evaluation_result = {
            "category": category,
            "query": query,
            "score": average_score,
            "latency": average_latency,
            "repeat_count": repeat_count,
            "response": response,
            "timestamp": datetime.now().isoformat()
        }

        results.append(evaluation_result)

        save_evaluation_result(evaluation_result)
        print("\n" + "-" * 60)

    # -------------------------------------------------
    # FINAL SUMMARY
    # -------------------------------------------------

    overall_average_score = round(sum(r["score"] for r in results) / len(results), 2)

    overall_average_latency = round(sum(r["latency"] for r in results) / len(results), 2)

    print("\n=== Evaluation Summary ===\n")

    print(f"Average Quality Score: {overall_average_score}%")

    print(f"Average Latency: {overall_average_latency}s")

    print("\nEvaluation completed.\n")


if __name__ == "__main__":
    run_evaluation()