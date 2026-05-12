def handle_general_query(user_input: str) -> str:
    """
    Handles greetings, help requests,
    and unsupported general interactions.
    """

    user_input = user_input.lower()

    # Greeting responses
    if any(keyword in user_input for keyword in [
        "hello",
        "hi",
        "hey",
    ]):
        return (
            "Hello! I’m PolicyAssist AI. "
            "How can I help you with your insurance support needs today?"
        )

    # Help responses
    elif "help" in user_input:
        return (
            "I can assist with policy coverage questions, claims guidance, "
            "and approved low-risk policy update requests."
        )

    # Thank you responses
    elif "thanks" in user_input or "thank you" in user_input:
        return (
            "You’re welcome! Let me know if you need further insurance support assistance."
        )

    # Unknown/general fallback
    else:
        return (
            "I’m unable to understand the request clearly. "
            "Please provide additional details about your insurance support question."
        )