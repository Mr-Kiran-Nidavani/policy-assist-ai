import json
import os
from datetime import datetime


# ---------------------------------------------------
# Feedback Storage File
# ---------------------------------------------------

FEEDBACK_LOG_PATH = os.getenv("FEEDBACK_LOG_PATH", "app/feedback/feedback_log.json")


# ---------------------------------------------------
# Ensure Feedback File Exists
# ---------------------------------------------------

if not os.path.exists(FEEDBACK_LOG_PATH):
    with open(FEEDBACK_LOG_PATH, "w") as file:
        json.dump([], file)


# ---------------------------------------------------
# Load Feedback Logs
# ---------------------------------------------------

def load_feedback_logs():
    """
    Loads feedback history.
    """

    with open(FEEDBACK_LOG_PATH, "r") as file:
        return json.load(file)


# ---------------------------------------------------
# Save Feedback
# ---------------------------------------------------

def save_feedback(query: str,  response: str,  query_type: str,   feedback: str):
    """
    Stores feedback interaction.
    """

    logs = load_feedback_logs()

    logs.append(
        {
            "query": query,
            "response": response,
            "query_type": query_type,
            "feedback": feedback,
            "timestamp": datetime.now().isoformat()
        }
    )

    with open(FEEDBACK_LOG_PATH, "w") as file:
        json.dump(logs, file, indent=2)


# ---------------------------------------------------
# Count Negative Feedback
# ---------------------------------------------------

def get_negative_feedback_count(
    query_type: str
):
    """
    Returns total negative feedback count
    for a query category.
    """

    logs = load_feedback_logs()

    count = 0

    for item in logs:

        if (
            item["query_type"] == query_type and item["feedback"] == "negative"
        ):
            count += 1

    return count


# ---------------------------------------------------
# Adaptation Decision
# ---------------------------------------------------

def should_use_adaptive_response(
    query_type: str
) -> bool:
    """
    Determines whether adaptive behaviour
    should be enabled.
    """

    negative_count = get_negative_feedback_count(query_type)
    return negative_count >= int(os.getenv("APPLY_ADAPTIVE_AFTER_NEGATIVE_FEEDBACK_COUNT", 2))