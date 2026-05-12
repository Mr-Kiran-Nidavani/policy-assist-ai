RESTRICTED_RESPONSE = (
    "I'm unable to assist with this request because it involves restricted "
    "or unauthorized operations. Please contact an authorized insurance "
    "representative or support specialist for further assistance."
)


def review_response(intent: str, response: str) -> str:
    """
    Performs basic safety validation for restricted operations.
    """

    # Restricted operations are blocked
    if intent == "restricted_operation":
        return RESTRICTED_RESPONSE

    return response