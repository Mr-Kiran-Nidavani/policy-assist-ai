import streamlit as st
import sys
import os
from transformers.utils import logging

# ---------------------------------------------------
# Environment Setup
# ---------------------------------------------------

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
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="PolicyAssist AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# CSS
# ---------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* App Background */

.stApp {
    background: linear-gradient(135deg, #EEF2FF, #E3E8FF);
}

/* Hide Sidebar */

section[data-testid="stSidebar"] {
    display: none;
}

/* Streamlit Padding */

.main .block-container {
    max-width: 100%;
    padding-top: 0rem;
    padding-bottom: 0.5rem;
    padding-left: 1.5rem;
    padding-right: 1.5rem;
}

/* Main Container */

.main-container {
    width: 100%;
    overflow: hidden;
}

/* Top Banner */

.top-section {
    background:
        linear-gradient(
            135deg,
            #6D28FF 0%,
            #4F1DCC 45%,
            #2B0A78 100%
        );

    padding: 12px 32px;
    color: white;
    position: relative;
    width: 100%;
    min-height: 95px;

    border-radius: 0px 0px 22px 22px;

    box-shadow:
        0px 10px 30px rgba(91, 46, 255, 0.25);
}

/* Decorative Glow */

.top-section::before {

    content: "";

    position: absolute;

    width: 300px;
    height: 300px;

    background: rgba(255,255,255,0.08);

    border-radius: 50%;

    top: -120px;
    right: 120px;

    filter: blur(20px);
}

/* Title */

.main-title {

    font-size: 30px;
    font-weight: 700;

    margin-bottom: 2px;

    display: flex;
    align-items: center;
    gap: 10px;

    letter-spacing: -0.5px;
}

/* Subtitle */

.sub-title {

    font-size: 13px;

    opacity: 0.92;

    margin-bottom: 10px;

    margin-left: 4px;
}

/* Online Badge */

.online-badge {

    display: inline-flex;

    align-items: center;

    gap: 6px;

    background: rgba(255,255,255,0.14);

    padding: 5px 14px;

    border-radius: 50px;

    font-size: 11px;

    backdrop-filter: blur(10px);

    border: 1px solid rgba(255,255,255,0.08);

    margin-left: 2px;
}

/* Robot Image */

.robot-image {

    position: absolute;

    right: 28px;
    top: 8px;

    width: 78px;

    filter:
        drop-shadow(0px 4px 10px rgba(0,0,0,0.18));
}

/* Chat Section */

.chat-section {

    padding:
        14px 28px 18px 28px;

    background: transparent;
}

/* Section Heading */

.section-heading {

    text-align: center;

    font-size: 16px;

    font-weight: 700;

    margin-top: 4px;

    margin-bottom: 12px;

    color: #111827;
}

/* Cards */

.support-card {

    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,0.98),
            rgba(255,255,255,0.95)
        );

    padding: 14px;

    border-radius: 16px;

    border:
        1px solid rgba(255,255,255,0.7);

    box-shadow:
        0px 4px 14px rgba(91, 46, 255, 0.08);

    transition: 0.25s ease;

    min-height: 112px;

    backdrop-filter: blur(10px);
}

.support-card:hover {

    transform: translateY(-3px);

    box-shadow:
        0px 10px 22px rgba(91, 46, 255, 0.15);

    border-color: rgba(108, 75, 255, 0.25);
}

/* Card Icon */

.card-icon {

    font-size: 22px;

    margin-bottom: 6px;
}

/* Card Title */

.card-title {

    font-size: 14px;

    font-weight: 600;

    color: #111827;

    margin-bottom: 5px;
}

/* Card Description */

.card-desc {

    font-size: 11px;

    line-height: 1.45;

    color: #6B7280;
}

/* Assistant Message */

.assistant-message {

    background:
        linear-gradient(
            135deg,
            #FFF4E6 0%,
            #FFE7CC 100%
        );

    padding: 14px;

    border-radius: 16px;

    margin-bottom: 14px;

    border:
        1px solid #FFD6A5;

    box-shadow:
        0px 4px 12px rgba(255, 153, 0, 0.10);

    color: #111827;

    font-size: 14px;

    line-height: 1.65;

    width: 72%;
}

/* Assistant Heading */

.assistant-message b {
    color: #E67E22;
    font-size: 15px;
    font-weight: 700;
}

/* User Wrapper */

.user-wrapper {

    display: flex;

    justify-content: flex-end;
}

/* User Message */

.user-message {

    background:
        linear-gradient(
            135deg,
            #6A11CB,
            #2575FC
        );

    padding: 10px 16px;

    border-radius:
        16px 16px 4px 16px;

    color: white;

    margin-bottom: 12px;

    width: fit-content;

    max-width: 60%;

    font-size: 13px;

    box-shadow:
        0px 4px 12px rgba(37,117,252,0.20);
}

/* Chat Input */

div[data-testid="stChatInput"] {

    background: rgba(255,255,255,0.95);

    border-radius: 50px;

    border:
        1px solid rgba(91, 46, 255, 0.10);

    padding: 4px;

    box-shadow:
        0px 4px 14px rgba(0,0,0,0.04);
}

/* Feedback */

.feedback-title {

    font-size: 18px;

    font-weight: 600;

    margin-top: 10px;

    margin-bottom: 14px;

    color: #111827;
}

/* Buttons */

.stButton > button {

    width: 100%;

    border-radius: 12px;

    border: none;

    padding: 8px 12px;

    font-weight: 600;

    background:
        linear-gradient(
            135deg,
            #6A11CB,
            #2575FC
        );

    color: white;

    transition: 0.25s ease;
}

.stButton > button:hover {

    transform: translateY(-1px);

    opacity: 0.95;
}

/* Spinner */

.stSpinner > div {
    border-top-color: #5B2EFF !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------------------
# Main Layout Start
# ---------------------------------------------------

st.markdown("""
<div class="main-container">

<div class="top-section">

<div class="main-title">
🤖 PolicyAssist AI
</div>

<div class="sub-title">
Your General Insurance Assistant
</div>

<div class="online-badge">
🟢 Online
</div>

<img class="robot-image"
src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png">

</div>

<div class="chat-section">
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Always Show Cards
# ---------------------------------------------------

st.markdown("""
<div class="section-heading">
I can help you with
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown("""
<div class="support-card">

<div class="card-icon">📄</div>

<div class="card-title">
General Coverage Info
</div>

<div class="card-desc">
Understand policy coverage,
exclusions and benefits.
</div>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="support-card">

<div class="card-icon">📝</div>

<div class="card-title">
Claim Process
</div>

<div class="card-desc">
Learn claim raise and
tracking process.
</div>

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="support-card">

<div class="card-icon">🔍</div>

<div class="card-title">
Policy Details
</div>

<div class="card-desc">
Check validity, premium
and coverage details.
</div>

</div>
""", unsafe_allow_html=True)

with col4:

    st.markdown("""
<div class="support-card">

<div class="card-icon">⚙️</div>

<div class="card-title">
Policy Update
</div>

<div class="card-desc">
Update phone, email
and personal info.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------
# Chat Messages
# ---------------------------------------------------

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
<div class="user-wrapper">

<div class="user-message">
🧑 {message["content"]}
</div>

</div>
""",
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            message["content"],
            unsafe_allow_html=True
        )

# ---------------------------------------------------
# Chat Input
# ---------------------------------------------------

user_input = st.chat_input(
    "Ask your insurance related question..."
)
# ---------------------------------------------------
# Process Query
# ---------------------------------------------------

if user_input:

    # Add User Message Immediately
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Trigger Processing Flag
    st.session_state.pending_query = user_input

    # Refresh UI Immediately
    st.rerun()

# ---------------------------------------------------
# Handle Pending Query
# ---------------------------------------------------

if "pending_query" in st.session_state:

    latest_query = st.session_state.pending_query

    # Prevent duplicate execution
    del st.session_state.pending_query

    with st.spinner("PolicyAssist AI is thinking..."):

        response = process_user_query(latest_query)

    # Save Last Query Info
    st.session_state.last_query = latest_query

    st.session_state.last_response = response["response"]

    st.session_state.last_query_type = (
        response["intent"]
        if "intent" in response
        else None
    )

    # Format Assistant Response
    formatted_response = f"""
<div class="assistant-message">

🛡️ <b>PolicyAssist AI</b><br>

{response["response"].replace(chr(10), "<br>")}

</div>
"""

    # Save Assistant Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": formatted_response
        }
    )

    # Refresh Again
    st.rerun()

# ---------------------------------------------------
# Close Main Container
# ---------------------------------------------------

st.markdown("""
</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Feedback Section
# ---------------------------------------------------

if (
    "last_query" in st.session_state
    and "last_response" in st.session_state
    and "last_query_type" in st.session_state
    and st.session_state.last_query_type is not None
):

    st.markdown("---")

    st.markdown("""
<div class="feedback-title">
Response Feedback
</div>
""", unsafe_allow_html=True)

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

# ---------------------------------------------------
# Hidden Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.header("⚙️ Controls")

    if st.button("🗑 Reset Conversation"):

        clear_conversation_memory()

        st.session_state.messages = []

        st.success(
            "Conversation reset successfully."
        )