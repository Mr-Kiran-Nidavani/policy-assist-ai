from agents.intent_router_agent import detect_intent
from agents.policy_information_agent import handle_policy_information_query
from agents.claim_support_agent import handle_claim_support_query
from agents.policy_update_agent import handle_policy_update_request
from agents.general_query_agent import handle_general_query
from agents.customer_policy_agent import handle_customer_policy_query
from agents.safety_review_agent import review_response
from logs.logger import get_logger

logger = get_logger()


def process_user_query(user_input: str) -> str:
    """
    Main orchestration workflow for the baseline
    multi-agent insurance support system.
    """

    # Step 1 — Detect intent
    intent = detect_intent(user_input)

    # Step 2 — Route to appropriate agent
    # Policy Information Agent
    if intent == "policy_information":
        response = handle_policy_information_query(user_input)

    # Customer Policy Query Agent
    elif intent == "customer_policy_query":
        response = handle_customer_policy_query(user_input)

    # Claim Support Agent
    elif intent == "claim_support":
        response = handle_claim_support_query(user_input)

    # Policy Update Agent
    elif intent == "policy_update":
        response = handle_policy_update_request(user_input)

    # Restricted Operations
    elif intent == "restricted_operation":
        response = "Restricted operation detected."

    # General Query Agent
    else:
        response = handle_general_query(user_input)

    # Step 3 — Safety Review
    safe_response = review_response(user_input, intent, response)
    logger.info(f"[RESPONSE] Final: {safe_response[:80]}...")

    return safe_response


def main():
    """
    CLI entry point for PolicyAssist AI.
    """

    print("\n=== PolicyAssist AI ===")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("PolicyAssist AI: Goodbye!")
            break

        response = process_user_query(user_input)

        print(f"\nPolicyAssist AI: {response}\n")


if __name__ == "__main__":
    main()