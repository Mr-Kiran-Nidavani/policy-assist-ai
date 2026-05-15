import re
from langchain_core.tools import tool
from tools.utils import get_customer_policy, save_customer_policy
from logs.logger import get_logger

logger = get_logger()

# ---------------------------------------------------
# Email Validation
# ---------------------------------------------------

def is_valid_email( email: str  ) -> bool:
    """
    Validates email format.
    """

    email_pattern = ( r"^[^@]+@[^@]+\.[^@]+$" )

    return bool( re.match(email_pattern, email))


# ---------------------------------------------------
# Update Email Tool
# ---------------------------------------------------

@tool
def update_email( customer_id: str,  new_email: str) -> dict:
    """
    Updates customer email address.

    Use this tool when customer wants to update or change email

    Args:
        customer_id (str):  Authenticated customer ID.
        new_email (str): New customer email address.

    Returns:
        dict:  Update operation result.
    """
    logger.info(f"Updating email for customer ID: {customer_id}")
    # ---------------------------------------------------
    # Validate Email
    # ---------------------------------------------------

    if not is_valid_email( new_email ):
        logger.warning(f"Invalid email address: {new_email}")
        return {
            "status": "INVALID_EMAIL",
            "message": "Provided email address is invalid."
        }


    # ---------------------------------------------------
    # Find Customer Policy
    # ---------------------------------------------------
    policy = get_customer_policy(customer_id)

    if not policy:
        logger.warning(f"Customer not found: {customer_id}")
        return {
            "status": "NOT_FOUND",
            "message": "Customer policy record not found."
        }

    old_email = policy.get("email")
    policy["email"] = new_email

    save_customer_policy(policy)
    logger.info(f"Email updated successfully for customer ID: {customer_id}")
    return {
        "status": "SUCCESS",
        "message": (
            "Customer email updated "
            "successfully."
        ),
        "old_email": old_email,
        "new_email": new_email
    }

  
# ---------------------------------------------------
# Local Testing
# ---------------------------------------------------

if __name__ == "__main__":

    result = update_email.invoke(
        {
            "customer_id": "C1001",
            "new_email": "john.updated@email.com"
        }
    )

    print(result)