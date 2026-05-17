import streamlit as st
import sys
import os 
from transformers.utils import logging

os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


logging.set_verbosity_error()


APP_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(APP_ROOT)


from main import process_user_query
from memory.conversation_memory import clear_conversation_memory
from feedback.feedback_utils import save_feedback


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="PolicyAssist AI",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------------------------------
# Custom Styling
# ---------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #FFFFFF;
        color: #1E293B;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 5px;
    }

    .sub-title {
        font-size: 18px;
        color: #475569;
        margin-bottom: 30px;
    }

    .user-message {
        background-color: #F8FAFC;
        padding: 14px;
        border-radius: 14px;
        margin-bottom: 10px;
        color: #111827;
        border: 1px solid #E2E8F0;
    }

    .assistant-message {
        background-color: #FFFFFF;
        padding: 14px;
        border-radius: 14px;
        margin-bottom: 18px;
        color: #111827;
        border: 1px solid #CBD5E1;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
    }

    .stButton > button {
        border-radius: 10px;
        border: 1px solid #CBD5E1;
        padding: 10px 18px;
        font-weight: 600;
        background-color: white;
        color: #111827;
    }

    .stButton > button:hover {
        border: 1px solid #94A3B8;
        background-color: #F8FAFC;
    }

    section[data-testid="stSidebar"] {
        background-color: #F8FAFC;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# Session State Initialization
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.markdown(
    '<div class="main-title">🛡️ PolicyAssist AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Smart Insurance Support Assistant</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.header("⚙️ Controls")

    if st.button("🗑 Reset Conversation"):

        clear_conversation_memory()
        st.session_state.messages = []
        st.success("Conversation reset successfully.")

    st.markdown("---")

    st.markdown(
        """
        ### Features

        - Multi-Agent Routing
        - Tool Calling
        - Memory-Aware Conversations
        - Contextual Workflow Continuity
        - Safety Review Layer
        - Adaptive Behaviour Ready
        """
    )


# ---------------------------------------------------
# Display Chat Messages
# ---------------------------------------------------

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f'<div class="user-message">🧑 {message["content"]}</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f'<div class="assistant-message">🤖 {message["content"]}</div>',
            unsafe_allow_html=True
        )


# ---------------------------------------------------
# User Input
# ---------------------------------------------------

user_input = st.chat_input(
    "Ask your insurance related question..."
)


# ---------------------------------------------------
# Process Query
# ---------------------------------------------------

if user_input:

    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Generate Response
    response = process_user_query(user_input)

    st.session_state.last_query = user_input
    st.session_state.last_response = response["response"]
    st.session_state.last_query_type = response["intent"]

    # Save Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content":  response["response"]
        }
    )

    # Refresh UI
    st.rerun()

# ---------------------------------------------------
# Feedback Section
# ---------------------------------------------------

if (
    "last_query" in st.session_state
    and "last_response" in st.session_state
    and "last_query_type" in st.session_state
):

    st.markdown("---")
    st.subheader("Response Feedback")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("👍 Helpful"):

            save_feedback(
                query=st.session_state.last_query,
                response=st.session_state.last_response,
                query_type=st.session_state.last_query_type,
                feedback="positive"
            )

            st.success(
                "Thanks for your feedback!"
            )

    with col2:

        if st.button("👎 Not Helpful"):

            save_feedback(
                query=st.session_state.last_query,
                response=st.session_state.last_response,
                query_type=st.session_state.last_query_type,
                feedback="negative"
            )

            st.warning(
                "Feedback recorded for future improvements."
            )