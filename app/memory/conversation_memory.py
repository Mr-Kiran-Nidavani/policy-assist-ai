from langchain_classic.memory import ConversationBufferMemory

# ---------------------------------------------------
# Shared Conversation Memory
# ---------------------------------------------------

memory = ConversationBufferMemory(
    return_messages=True
)


# ---------------------------------------------------
# Save Interaction
# ---------------------------------------------------

def save_user_input(user_input: str):
    """
    Saves user input into conversation memory.
    """

    memory.chat_memory.add_user_message(user_input)

def save_ai_response(ai_response: str):
    """
    Saves AI response into conversation memory.
    """

    memory.chat_memory.add_ai_message(ai_response)


# ---------------------------------------------------
# Get Conversation History
# ---------------------------------------------------

def get_conversation_history():
    """
    Returns conversation history.
    """

    return memory.load_memory_variables({})


# ---------------------------------------------------
# Clear Conversation Memory
# ---------------------------------------------------

def clear_conversation_memory():
    """
    Clears all conversation memory.
    """

    memory.clear()