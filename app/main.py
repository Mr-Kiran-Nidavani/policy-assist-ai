from intents import detect_intent
from responses import (
    COVERAGE_RESPONSE,
    CLAIM_RESPONSE,
    DEDUCTIBLE_RESPONSE,
    UNSAFE_RESPONSE,
    UNKNOWN_RESPONSE,
)
from safety import is_unsafe_request


def generate_response(intent: str) -> str:
    """
    Returns a predefined response based on detected intent.
    """

    if intent == "coverage_query":
        return COVERAGE_RESPONSE

    elif intent == "claim_query":
        return CLAIM_RESPONSE

    elif intent == "deductible_query":
        return DEDUCTIBLE_RESPONSE

    else:
        return UNKNOWN_RESPONSE


def main():
    """
    Main CLI application loop.
    """

    print("\nWelcome to PolicyAssist AI")
    print("Type 'exit' to quit the application.\n")

    while True:
        user_input = input("Enter your question: ")

        if user_input.lower() == "exit":
            print("\nThank you for using PolicyAssist AI.")
            break

        # Step 1: Safety validation
        if is_unsafe_request(user_input):
            print(f"\nResponse: {UNSAFE_RESPONSE}\n")
            continue

        # Step 2: Intent detection
        intent = detect_intent(user_input)

        # Step 3: Generate response
        response = generate_response(intent)

        print(f"\nResponse: {response}\n")


if __name__ == "__main__":
    main()