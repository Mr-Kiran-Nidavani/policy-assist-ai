def handle_policy_update_request(user_input: str) -> str:
    """
    Handles low-risk policy update requests using
    predefined baseline responses.
    """

    user_input = user_input.lower()

    # Email update requests
    if "email" in user_input:
        return (
            "Your request to update the email address has been received. "
            "A customer support representative may contact you for verification."
        )

    # Phone update requests
    elif "phone" in user_input:
        return (
            "Your request to update the phone number has been received. "
            "Additional verification may be required."
        )

    # Address update requests
    elif "address" in user_input:
        return (
            "Your address update request has been submitted successfully."
        )

    # Add vehicle requests
    elif "vehicle" in user_input:
        return (
            "Your request to add a new vehicle has been recorded. "
            "Supporting vehicle documents may be required."
        )

    # Add driver requests
    elif "driver" in user_input:
        return (
            "Your request to add a new driver has been recorded. "
            "Driver verification documents may be required."
        )

    # Generic operational response
    else:
        return (
            "I can assist with approved low-risk policy update requests "
            "such as contact information updates or vehicle additions."
        )