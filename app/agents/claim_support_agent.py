def handle_claim_support_query(user_input: str) -> str:
    """
    Handles claim-related support queries using
    predefined baseline responses.
    """

    user_input = user_input.lower()

    # Claim status queries
    if "claim status" in user_input or "status" in user_input:
        return (
            "Claim status information is currently unavailable in the "
            "baseline system. Please contact customer support for assistance."
        )

    # Reimbursement-related queries
    elif "reimbursement" in user_input:
        return (
            "Reimbursement claims typically require hospital bills, "
            "medical reports, discharge summaries, and identity proof."
        )

    # Rejected claim queries
    elif "rejected" in user_input:
        return (
            "Claims may be rejected due to exclusions, incomplete documents, "
            "waiting periods, or policy limitations."
        )

    # Hospitalization claim queries
    elif "hospitalization" in user_input:
        return (
            "Hospitalization claims usually require admission records, "
            "discharge summaries, and medical expense documentation."
        )

    # Generic claims guidance
    else:
        return (
            "I can assist with claim-related guidance, reimbursement "
            "requirements, and general claims support questions."
        )