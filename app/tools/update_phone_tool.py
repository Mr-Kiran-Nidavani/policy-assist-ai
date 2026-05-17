import re

from langchain_core.tools import tool

from tools.utils import (
    get_customer_policy,
    save_customer_policy
)

from logs.logger import get_logger


# ---------------------------------------------------
# Initialize Logger
# ---------------------------------------------------

logger = get_logger()


# ---------------------------------------------------
# Phone Validation
# ---------------------------------------------------

def is_valid_phone(phone: str) -> bool:
    """
    Validates phone number format.
    """
    phone_pattern = (r"^[0-9]{10}$")
    return bool(re.match(phone_pattern, phone))


# ---------------------------------------------------
# Update Phone Tool
# ---------------------------------------------------

@tool
def update_phone(customer_id: str, new_phone: str) -> dict:
    """
    Updates customer phone number.

    Use this tool when:
    - customer wants to update phone
    - customer wants to change phone number
    - customer provides new contact number

    Args:
        customer_id (str):
            Authenticated customer ID.

        new_phone (str):
            New customer phone number.

    Returns:
        dict:
            Update operation result.
    """

    logger.info("[TOOL] Phone Update: Starting")

    # ---------------------------------------------------
    # Validate Phone
    # ---------------------------------------------------

    if not is_valid_phone(new_phone):
        logger.info("[TOOL] Phone Update: Failed - Invalid format")
        return {
            "status": "INVALID_PHONE",
            "message": (
                "Provided phone number "
                "is invalid."
            )
        }

    # ---------------------------------------------------
    # Find Customer Policy
    # ---------------------------------------------------

    policy = get_customer_policy(customer_id)

    if not policy:
        logger.warning(f"Customer not found: {customer_id}")

        return {
            "status": "NOT_FOUND",
            "message": (
                "Customer policy "
                "record not found."
            )
        }

    # ---------------------------------------------------
    # Update Phone
    # ---------------------------------------------------

    old_phone = policy.get("phone")

    policy["phone"] = new_phone

    save_customer_policy(policy)

    logger.info(f"Phone updated successfully for customer ID: {customer_id}")

    return {
        "status": "SUCCESS",
        "message": (
            "Customer phone number "
            "updated successfully."
        ),
        "old_phone": old_phone,
        "new_phone": new_phone
    }


# ---------------------------------------------------
# Local Testing
# ---------------------------------------------------

if __name__ == "__main__":

    result = update_phone.invoke(
        {
            "customer_id": "C1001",
            "new_phone": "9876543210"
        }
    )

    print(result)