def detect_intent(user_input: str) -> str:
    """
    Detects the intent of the user query using simple keyword matching.
    """

    user_input = user_input.lower()

    # Coverage-related queries
    if any(keyword in user_input for keyword in [
        "cover",
        "coverage",
        "included",
        "benefit",
    ]):
        return "coverage_query"

    # Claim-related queries
    elif any(keyword in user_input for keyword in [
        "claim",
        "reimbursement",
        "hospitalization",
    ]):
        return "claim_query"

    # Deductible-related queries
    elif any(keyword in user_input for keyword in [
        "deductible",
        "copay",
        "co-pay",
    ]):
        return "deductible_query"

    # Unknown queries
    else:
        return "unknown"