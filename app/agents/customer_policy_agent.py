import json

from langchain_core.messages import HumanMessage, ToolMessage
from llm.llm_client import LLMClient
from tools.policy_lookup_tool import lookup_policy_details
from logs.logger import get_logger
logger = get_logger()

# ---------------------------------------------------
# Initialize LLM
# ---------------------------------------------------

llm_client = LLMClient()
llm = llm_client.llm


# ---------------------------------------------------
# Register Available Tools
# ---------------------------------------------------

tools = [ lookup_policy_details ]


# ---------------------------------------------------
# Bind Tools To LLM
# ---------------------------------------------------

tool_enabled_llm = llm.bind_tools(tools)


# ---------------------------------------------------
# Customer Policy Agent
# ---------------------------------------------------

def handle_customer_policy_query(
    user_query: str,
    customer_id: str
) -> str:
    """
    Handles customer-specific policy queries using policy retrieval tools.
    """

    logger.info("Starting customer policy agent" )

    logger.info(f"Customer ID: {customer_id}")

    # ---------------------------------------------------
    # Build User Message
    # ---------------------------------------------------

    messages = [
        HumanMessage(
            content=(f"""You are PolicyAssist AI, a safety-first insurance support assistant.
    
                Authenticated Customer ID: {customer_id}

                Available Tool:
                - lookup_policy_details

                Rules:
                - Use the tool when customer
                policy information is required.
                - Never fabricate policy details.
                - Use ONLY retrieved policy data.
                - Remain professional and concise.

                Customer Query:
                {user_query}
                """
            )
        )
    ]

    # ---------------------------------------------------
    # Invoke Tool-Aware LLM
    # ---------------------------------------------------

    response = tool_enabled_llm.invoke( messages )

    # ---------------------------------------------------
    # Process Tool Calls
    # ---------------------------------------------------

    if response.tool_calls:
        logger.info(f"Tool calls detected: {len(response.tool_calls)}")
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            logger.info(f"Selected Tool: {tool_name}")

            # Ensure customer_id exists
            if ( "customer_id" not in tool_args  ):
                tool_args["customer_id"] = customer_id

            # ---------------------------------------------------
            # Execute Tool
            # ---------------------------------------------------

            if (tool_name == "lookup_policy_details"):
                tool_result = lookup_policy_details.invoke(tool_args)
                logger.info(f"Tool Result Status: {tool_result.get('status')}")

                # ---------------------------------------------------
                # Append Tool Response
                # ---------------------------------------------------

                messages.append(response)

                messages.append(
                    ToolMessage(
                        tool_call_id=tool_call["id"],
                        content=json.dumps(
                            tool_result,
                            indent=2
                        )
                    )
                )

        # ---------------------------------------------------
        # Final Grounded Response
        # ---------------------------------------------------

        final_response = llm.invoke( messages )
        logger.info("Customer policy response generated")
        return final_response.content

    # ---------------------------------------------------
    # No Tool Usage Needed
    # ---------------------------------------------------

    return response.content