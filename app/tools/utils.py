import os
import json

# ---------------------------------------------------
# Data Source Configuration
# ---------------------------------------------------

DATA_PATH = os.getenv("CUSTOMER_POLICY_DATA_PATH")


# ---------------------------------------------------
# Load Customer Policies
# ---------------------------------------------------

def load_customer_policies():
    """
    Loads customer policy records
    from the configured JSON file.
    """

    if not DATA_PATH:

        raise ValueError("CUSTOMER_POLICY_DATA_PATH not set")

    with open(DATA_PATH, "r") as file:
        return json.load(file)


# ---------------------------------------------------
# Retrieve Customer Policy
# ---------------------------------------------------

def get_customer_policy(customer_id: str):
    """
    Retrieves a customer policy
    record using customer ID.

    Args:
        customer_id (str): Unique customer identifier.

    Returns:
        dict | None:
            Matching customer policy record if found.
    """

    policies = load_customer_policies()

    for policy in policies:

        if (policy["customer_id"] == customer_id ):
            return policy

    return None

# ---------------------------------------------------
# Save Customer Policies
# ---------------------------------------------------
# ---------------------------------------------------
# Save Customer Policies
# ---------------------------------------------------

def save_customer_policy(
    updated_policy
):
    """
    Updates and saves a customer policy record using policy number.
    """

    # ---------------------------------------------------
    # Validate Input
    # ---------------------------------------------------

    if ("policy_number"  not in updated_policy):
        raise ValueError("Updated policy missing policy_number.")

    # ---------------------------------------------------
    # Load Existing Policies
    # ---------------------------------------------------

    policies = load_customer_policies()
    updated = False

    # ---------------------------------------------------
    # Replace Matching Policy
    # ---------------------------------------------------

    for index, policy in enumerate(policies):

        if (policy["policy_number"] == updated_policy["policy_number"]):
            policies[index] = updated_policy
            updated = True
            break

    # ---------------------------------------------------
    # Policy Not Found
    # ---------------------------------------------------

    if not updated:
        raise ValueError("Policy number not found.")

    # ---------------------------------------------------
    # Save Updated Policies
    # ---------------------------------------------------

    with open(DATA_PATH, "w") as file:
        json.dump(policies, file, indent=2)

    return True