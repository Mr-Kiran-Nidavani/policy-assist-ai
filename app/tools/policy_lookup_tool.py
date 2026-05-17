from langchain_core.tools import tool
from tools.utils import get_customer_policy
from logs.logger import get_logger

logger = get_logger()

# ---------------------------------------------------
# LangChain Tool
# ---------------------------------------------------

@tool
def lookup_policy_details(
    customer_id: str
) -> dict:
    """
    Retrieves customer policy details using customer ID.

    Use this tool when:
    - You need to access specific policy information for a given customer id.
    Args:
        customer_id (str):
            Authenticated customer ID.

    Returns:
        dict:
            Customer policy details.
    """

    logger.info("[TOOL] Policy Lookup: Starting")
    policy = get_customer_policy(customer_id )

    if not policy:
        logger.info("[TOOL] Policy Lookup: Failed - Not found")
        return {
            "status": "NOT_FOUND",
            "message": "Customer policy record not found."
        }

    logger.info("[TOOL] Policy Lookup: Success")
    return {
        "status": "SUCCESS",
        "policy_details": policy
    }


# ---------------------------------------------------
# Local Testing
# ---------------------------------------------------

if __name__ == "__main__":

    result = lookup_policy_details.invoke(
        {
            "customer_id": "C1001"
        }
    )

    print(result)