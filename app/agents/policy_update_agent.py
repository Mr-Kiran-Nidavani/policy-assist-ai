import json

from langchain_core.messages import HumanMessage, ToolMessage
from llm.llm_client import LLMClient
from tools.update_email_tool import update_email
from tools.update_phone_tool import update_phone
from logs.logger import get_logger


# ---------------------------------------------------
# Initialize Logger
# ---------------------------------------------------

logger = get_logger()


# ---------------------------------------------------
# Initialize LLM
# ---------------------------------------------------

llm_client = LLMClient()
llm = llm_client.llm


# ---------------------------------------------------
# Register Available Tools
# ---------------------------------------------------

tools = [
    update_email,
    update_phone
]


# ---------------------------------------------------
# Bind Tools To LLM
# ---------------------------------------------------

tool_enabled_llm = llm.bind_tools(tools)


# ---------------------------------------------------
# Policy Update Agent
# ---------------------------------------------------

def handle_policy_update_request(user_query: str, customer_id: str) -> str:
    """
    Handles customer policy
    update requests using
    controlled tool calling.
    """

    logger.info("Starting policy update agent")

    logger.info(f"Customer ID: {customer_id}")

    # ---------------------------------------------------
    # Build User Message
    # ---------------------------------------------------

    messages = [
        HumanMessage(
            content=(
                f"""
You are PolicyAssist AI,
a safety-first insurance
support assistant.

Authenticated Customer ID:
{customer_id}

Available Tools:
- update_email
- update_phone

Rules:
- Use tools ONLY for:
  - email updates
  - phone updates
- Any other policy update
  requests require
  human review.
- Never fabricate updates.
- Never approve restricted
  operations.
- Remain professional
  and concise.

Customer Query:
{user_query}
"""
            )
        )
    ]

    logger.info("Invoking tool-enabled LLM")
    response = tool_enabled_llm.invoke(messages)

    # ---------------------------------------------------
    # Process Tool Calls
    # ---------------------------------------------------

    if response.tool_calls:
        logger.info(f"Tool calls detected: {len(response.tool_calls)}")
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            logger.info(f"Selected Tool: {tool_name}")
            logger.info(f"Tool Arguments: {tool_args}")

            # Ensure customer_id exists
            if ("customer_id" not in tool_args):
                tool_args["customer_id"] = customer_id

            # ---------------------------------------------------
            # Execute Tool
            # ---------------------------------------------------

            selected_tool = next(
                (
                    tool
                    for tool in tools
                    if tool.name == tool_name
                ),
                None
            )

            if not selected_tool:
                continue

            tool_result = selected_tool.invoke(tool_args)

            logger.info(f"Tool Result Status: {tool_result.get('status')}")

            # ---------------------------------------------------
            # Append Tool Result
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
        # Generate Final Response
        # ---------------------------------------------------

        logger.info("Generating final policy update response")
        final_response = llm.invoke(messages)
        logger.info("Policy update response generated")
        return final_response.content

    # ---------------------------------------------------
    # Unsupported Update Request
    # ---------------------------------------------------

    logger.warning("Unsupported update request requires human review" )

    return (
        "This policy update request "
        "requires review by a licensed "
        "insurance representative and "
        "cannot be handled by the bot "
        "at this time."
    )