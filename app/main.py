from agents.intent_router_agent import detect_intent
from agents.policy_information_agent import handle_policy_information_query
from agents.claim_support_agent import handle_claim_support_query
from agents.policy_update_agent import handle_policy_update_request
from agents.general_query_agent import handle_general_query
from agents.customer_policy_agent import handle_customer_policy_query
from agents.safety_review_agent import review_response
from logs.logger import get_logger
import time
from memory.conversation_memory import (
    save_user_input,
    save_ai_response,
    get_conversation_history,
    clear_conversation_memory
)

logger = get_logger()

pending_query = None

def process_user_query(user_input: str) -> str:
    """
    Main orchestration workflow for the baseline
    multi-agent insurance support system.
    """

    start_time = time.time()
    try:
        
        global pending_query

        if user_input.lower() == "reset":
            clear_conversation_memory()
            latency = round(time.time() - start_time, 2)
            logger.info(f"[LATENCY] Response generated in {latency}s")
            return {
                "response": "Conversation memory cleared successfully."
            }

        save_user_input(user_input)
        # init conversation history
        conversation_history = get_conversation_history()

        # Step 1 — Detect intent
        routing_result = detect_intent(user_input, conversation_history)
        intent = routing_result.get("intent", "unknown")
        customer_id = routing_result.get("customer_id")
        missing_info = routing_result.get("missing_info", "")
        user_input = routing_result.get("query_to_process", user_input)

        if missing_info:        
            save_ai_response(missing_info)
            latency = round(time.time() - start_time, 2)
            logger.info(f"[LATENCY] Response generated in {latency}s")
            return {
                "response": missing_info
            }
        

    
        # Step 2 — Route to appropriate agent
        # Policy Information Agent
        if intent == "policy_information":
            response = handle_policy_information_query(user_input)

        # Customer Policy Query Agent
        elif intent == "customer_policy_query":
            response = handle_customer_policy_query(user_input, customer_id=customer_id)

        # Claim Support Agent
        elif intent == "claim_support":
            response = handle_claim_support_query(user_input)

        # Policy Update Agent
        elif intent == "policy_update":
            response = handle_policy_update_request(user_input, customer_id=customer_id, conversation_history=conversation_history)

        # Restricted Operations
        elif intent == "restricted_operation":
            response = "Restricted operation detected."

        # General Query Agent
        else:
            response = handle_general_query(user_input)

        # Step 3 — Safety Review
        safe_response = review_response(user_input, intent, response)
        logger.info(f"[RESPONSE] Final: {safe_response[:80]}...")
        save_ai_response(safe_response)
        latency = round(time.time() - start_time, 2)
        logger.info(f"[LATENCY] Response generated in {latency}s")
        return {
            "response": safe_response,
            "intent": intent
        }
    except Exception as error:
        logger.error(f"Error processing user query: {error}")
        return {
            "response": "Sorry, something went wrong while processing your request. Please try again later."
        }

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

        print(f"\nPolicyAssist AI: {response['response']}\n")


if __name__ == "__main__":
    main()