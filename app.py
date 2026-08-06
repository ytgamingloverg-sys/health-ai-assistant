import streamlit as st
import requests
import PyPDF2
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
