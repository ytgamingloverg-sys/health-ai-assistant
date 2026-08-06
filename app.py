import streamlit as st
import requests

# ===========================
# PAGE CONFIG
# ===========================

st.set_page_config(
    page_title="MUSHFIK AI HEALTH ASSISTANT",
    page_icon="🩺",
    layout="wide"
)

# ===========================
# GROQ API KEY
# ===========================

API_KEY = "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"   # <-- এখানে তোমার API Key বসাও

# ===========================
# TITLE
# ===========================

st.title("🩺 MUSHFIK AI HEALTH ASSISTANT")
st.write("Powered by Groq AI")

# ===========================
# CHAT
# ===========================

user_input = st.chat_input("আপনার সমস্যা লিখুন...")

if user_input:

    st.chat_message("user").write(user_input)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an AI Health Assistant. "
                    "Never claim to be a licensed doctor. "
                    "Ask follow-up questions when needed and advise users to seek professional care for emergencies."
                )
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:

        reply = response.json()["choices"][0]["message"]["content"]

        st.chat_message("assistant").write(reply)

    else:

        st.error(response.text)
