UNSAFE_KEYWORDS = [
    "approve",
    "reject",
    "modify",
    "change policy",
    "update policy",
    "process payment",
    "cancel policy",
    "add spouse",
]


def is_unsafe_request(user_input: str) -> bool:
    """
    Checks whether the user request contains unsafe operations.
    """

    user_input = user_input.lower()

    for keyword in UNSAFE_KEYWORDS:
        if keyword in user_input:
            return True

    return False