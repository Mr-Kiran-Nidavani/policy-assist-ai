def handle_policy_information_query(user_input: str) -> str:
    """
    Handles policy-related support questions using
    predefined rule-based responses.
    """

    user_input = user_input.lower()

    # Coverage-related responses
    if "coverage" in user_input or "cover" in user_input:
        return (
            "Your insurance policy may provide coverage depending on "
            "policy terms, exclusions, waiting periods, and claim evaluation."
        )

    # Waiting period responses
    elif "waiting period" in user_input:
        return (
            "Waiting periods vary depending on the treatment and policy type. "
            "Please review your policy documents for exact details."
        )

    # Deductible responses
    elif "deductible" in user_input:
        return (
            "A deductible is the amount you must pay before insurance "
            "coverage applies to eligible claims."
        )

    # Exclusion responses
    elif "exclusion" in user_input:
        return (
            "Policy exclusions define situations or treatments that are not "
            "covered under the insurance plan."
        )

    # Generic policy response
    else:
        return (
            "I can help explain policy coverage, exclusions, waiting periods, "
            "and deductible-related questions."
        )