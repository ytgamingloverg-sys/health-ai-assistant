import streamlit as st
from openai import OpenAI
import os
from io import BytesIO
from PIL import Image
import PyPDF2

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="MUSHFIK AI HEALTH ASSISTANT",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# CUSTOM CSS
# ==========================

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
background:linear-gradient(135deg,#061421,#0d1b2a,#102542);
color:white;
}

.title{
font-size:55px;
font-weight:bold;
text-align:center;
color:#00E5FF;
margin-bottom:10px;
}

.subtitle{
text-align:center;
font-size:22px;
color:white;
margin-bottom:35px;
}

.card{
background:rgba(255,255,255,.08);
padding:25px;
border-radius:20px;
backdrop-filter:blur(18px);
box-shadow:0 0 30px rgba(0,255,255,.2);
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# API KEY
# ==========================

api_key = st.secrets.get("XAI_API_KEY", "")

client = None

if api_key:
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.x.ai/v1"
    )

# ==========================
# SESSION STATE
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================
# HEADER
# ==========================

st.markdown(
    '<div class="title">🩺 MUSHFIK AI HEALTH ASSISTANT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Human-like AI Doctor • Grok AI • Science Fair Project</div>',
    unsafe_allow_html=True
)
