from agents.intent_router_agent import detect_intent
from agents.policy_information_agent import handle_policy_information_query
from agents.claim_support_agent import handle_claim_support_query
from agents.policy_update_agent import handle_policy_update_request
from agents.general_query_agent import handle_general_query
from agents.customer_policy_agent import handle_customer_policy_query
from agents.safety_review_agent import review_response
from logs.logger import get_logger

logger = get_logger()


# ---------------------------------------------------
# Temporary Conversation State
# ---------------------------------------------------

awaiting_customer_number = False
pending_intent = None
pending_user_query = None
active_customer_id = None

def handle_customer_lookup_flow(customer_number: str) -> str:
    """
    Handles customer lookup workflow after
    customer number is provided.
    """

    global awaiting_customer_number
    global pending_intent
    global pending_user_query
    global active_customer_id

    # ---------------------------------------------------
    # Store Active Customer Session
    # ---------------------------------------------------
    logger.info(f"Received customer number: {customer_number}")
    active_customer_id = customer_number    

    logger.info(f"Active customer session set: {active_customer_id}")

    # Generate customer-specific response
    response = handle_customer_policy_query(
        user_query=pending_user_query,
        customer_id=customer_number
    )

    # Reset temporary state
    awaiting_customer_number = False
    pending_intent = None
    pending_user_query = None

    # Safety review
    logger.info("Running safety review agent")

    safe_response = review_response(
        user_input=customer_number,
        intent="customer_policy_query",
        response=response
    )

    return safe_response

def process_user_query(user_input: str) -> str:
    """
    Main orchestration workflow for the baseline
    multi-agent insurance support system.
    """

    global awaiting_customer_number
    global pending_intent
    global pending_user_query
    global active_customer_id

    # This it to comtinue the customer policy query flow after intent detection has prompted for customer number 
    # and user has provided it
    if awaiting_customer_number:
        return handle_customer_lookup_flow(user_input.strip())



    # Step 1 — Detect intent
    intent = detect_intent(user_input)
    logger.info(f"Detected intent: {intent}")

    # Step 2 — Route to appropriate agent

    # Policy Information Agent
    if intent == "policy_information":
        response = handle_policy_information_query(user_input)

    # Customer Policy Query Agent
    elif intent == "customer_policy_query":
        if active_customer_id:
            logger.info(f"Using active customer session: {active_customer_id}")
            response = handle_customer_policy_query(
                user_query=user_input,
                customer_id=active_customer_id
            )
        else:
            pending_user_query = user_input
            awaiting_customer_number = True
            pending_intent = intent

            return "Please provide your customer number to continue."

    # Claim Support Agent
    elif intent == "claim_support":
        response = handle_claim_support_query(user_input)

    # Policy Update Agent
    elif intent == "policy_update":
        if active_customer_id:
            logger.info(f"Using active customer session: {active_customer_id}")
            response = handle_policy_update_request(
                user_query=user_input,
                customer_id=active_customer_id
            )
        else:
            pending_user_query = user_input
            awaiting_customer_number = True
            pending_intent = intent

            return "Please provide your customer number to continue."
        

    # Restricted Operations
    elif intent == "restricted_operation":
        response = "Restricted operation detected."

    # General Query Agent
    else:
        response = handle_general_query(user_input)

    # Step 3 — Safety Review
    logger.info("Running safety review agent")
    safe_response = review_response(
        user_input=user_input,
        intent=intent,
        response=response
    )

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

        if not user_input.strip():
            print(
                "\nPolicyAssist AI: Please enter a valid insurance-related question.\n"
            )
            continue

        response = process_user_query(user_input)

        print(f"\nPolicyAssist AI: {response}\n")


if __name__ == "__main__":
    main()