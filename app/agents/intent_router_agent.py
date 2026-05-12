def detect_intent(user_input: str) -> str:
    """
    Detects the user intent using simple keyword matching.
    This is a baseline implementation for Phase 2.
    """

    user_input = user_input.lower()

    # Restricted operations
    if (
        (
            any(action in user_input for action in [
                "reduce",
                "change",
                "backdate",
                "waive",
                "cancel",
                "approve"
            ])
            and
            any(target in user_input for target in [
                "premium",
                "effective date",
                "deductible",
                "policy",
                "coverage",
                "claim"
            ])
        )
        or
        (
            any(action in user_input for action in [
                "approve",
                "reject",
            ])
            and "claim" in user_input
        )
    ):
        return "restricted_operation"
    # Policy information queries
    elif any(keyword in user_input for keyword in [
        "coverage",
        "cover",
        "included",
        "benefit",
        "deductible",
        "exclusion",
        "policy",
    ]):
        return "policy_information"

    # Claim support queries
    elif any(keyword in user_input for keyword in [
        "claim",
        "reimbursement",
        "hospitalization"
    ]):
        return "claim_support"

    # Policy update requests
    elif (
        any(action in user_input for action in [
            "update",
            "change",
            "add",
        ])
        and
        any(target in user_input for target in [
            "email",
            "phone",
            "address",
            "vehicle",
            "driver",
        ])
    ):
        return "policy_update"

    # Greetings and general queries
    elif any(keyword in user_input for keyword in [
        "hello",
        "hi",
        "help",
        "thanks",
    ]):
        return "general_query"

    # Unknown requests
    else:
        return "unknown"