import streamlit as st
import requests
from PIL import Image
import io

# ==========================================
# GROQ API KEY
# ==========================================

API_KEY = "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"

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="মুশফিক এআই স্বাস্থ্য সহকারী",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# PREMIUM CSS
# ==========================================

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.stApp{
background:linear-gradient(135deg,#071A2F,#0B2945,#133B5C);
color:white;
}

.title{

font-size:55px;
font-weight:bold;
text-align:center;
color:#00E5FF;

}

.subtitle{

font-size:22px;
text-align:center;
margin-bottom:30px;

}

.card{

background:rgba(255,255,255,.08);
padding:20px;
border-radius:20px;
backdrop-filter:blur(12px);
margin-bottom:20px;

}

</style>
""",unsafe_allow_html=True)

# ==========================================
# TITLE
# ==========================================

st.markdown(
'<div class="title">🩺 মুশফিক এআই স্বাস্থ্য সহকারী</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="subtitle">বাংলা ভাষাভিত্তিক ভার্চুয়াল এআই ডাক্তার</div>',
unsafe_allow_html=True
)

# ==========================================
# SESSION
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages=[]
# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🩺 AI ডাক্তার")

    st.success("🟢 সিস্টেম চালু আছে")

    st.markdown("---")

    st.write("### সুবিধাসমূহ")

    st.write("💬 স্বাস্থ্য পরামর্শ")
    st.write("📄 রিপোর্ট বিশ্লেষণ (শীঘ্রই)")
    st.write("❤️ সেন্সর সংযোগ (শীঘ্রই)")
    st.write("🎤 ভয়েস সহকারী (শীঘ্রই)")

    st.markdown("---")

    st.info("⚠️ এটি একজন প্রকৃত ডাক্তার নয়। এটি শুধুমাত্র স্বাস্থ্য বিষয়ক সাধারণ তথ্য প্রদান করে।")


# ==========================================
# GROQ CHAT FUNCTION
# ==========================================

def ask_ai(question):

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": """
তুমি একজন বাংলা AI স্বাস্থ্য সহকারী।

নিয়ম:

- সবসময় বাংলায় উত্তর দেবে।
- সহজ ভাষা ব্যবহার করবে।
- প্রয়োজন হলে রোগীকে আরও প্রশ্ন করবে।
- নিজেকে কখনো প্রকৃত ডাক্তার বলবে না।
- নিশ্চিত রোগ নির্ণয় করবে না।
- জরুরি সমস্যা হলে হাসপাতালে যেতে বলবে।
"""
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "temperature": 0.6
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]

    return "❌ সার্ভারের সাথে সংযোগ করা যাচ্ছে না।"


# ==========================================
# CHAT
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("আপনার সমস্যাটি লিখুন...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    answer = ask_ai(prompt)

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )
