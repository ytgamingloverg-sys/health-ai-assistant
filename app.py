import requests

API_KEY = st.secrets["XAI_API_KEY"]

url = "https://api.x.ai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "grok-4",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful AI medical assistant."
        },
        {
            "role": "user",
            "content": "আমার মাথা ব্যথা করছে।"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🩺 AI Doctor")

    st.success("🟢 System Online")

    st.markdown("---")

    st.write("### Features")

    st.write("🤖 Human AI Doctor")
    st.write("💬 Chat Mode")
    st.write("📄 Medical Report Upload")
    st.write("❤️ Sensor Dashboard")
    st.write("🎤 Voice Assistant")
    st.write("🌍 Bangla + English")

    st.markdown("---")

    if api_key:
        st.success("✅ Grok API Connected")
    else:
        st.error("❌ Grok API Key Not Found")

    st.markdown("---")

    st.info(
        "⚠️ This AI provides educational information only. "
        "It is not a replacement for a licensed doctor."
    )


# ==========================================
# MAIN LAYOUT
# ==========================================

left, right = st.columns([1, 2])

with left:

    st.markdown("## 👨‍⚕️ AI Doctor")

    st.image(
        "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=500",
        use_container_width=True
    )

    st.success("AI Doctor is Ready")

with right:

    st.markdown("## 💬 Talk with AI Doctor")

    st.write(
        """
Welcome!

I am your AI Health Assistant.

You can:

- Describe your symptoms
- Upload medical reports
- Ask health questions
- Connect health sensors
"""
    )


# ==========================================
# CHAT HISTORY
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
