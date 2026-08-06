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
# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.title("🩺 AI Doctor")

    st.success("System Status: Online")

    st.markdown("---")

    st.subheader("👤 Patient Information")

    patient_name = st.text_input(
        "Patient Name",
        placeholder="Enter your name"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=18
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
            "Other"
        ]
    )

    st.markdown("---")

    st.subheader("🌍 Language")

    language = st.selectbox(
        "",
        [
            "English",
            "বাংলা"
        ]
    )

    st.markdown("---")

    st.subheader("❤️ Live Health Dashboard")

    heart_rate = st.metric(
        "Heart Rate",
        "-- BPM"
    )

    oxygen = st.metric(
        "SpO₂",
        "-- %"
    )

    temperature = st.metric(
        "Temperature",
        "-- °C"
    )

    st.markdown("---")

    st.info("ESP32 Sensor Connection: Not Connected")

# ==========================
# MAIN LAYOUT
# ==========================

left, right = st.columns([1, 2])

# ==========================
# LEFT PANEL
# ==========================

with left:

    st.markdown("""
    <div class="card">
    <h2 align="center">👨‍⚕️ AI Doctor</h2>
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=700",
        use_container_width=True
    )

    st.success("🟢 Ready to help")

    st.write(
        """
        Welcome!

        I am your AI Health Assistant.

        I can:

        ✅ Talk with you

        ✅ Analyze symptoms

        ✅ Read medical reports

        ✅ Explain reports simply

        ✅ Suggest possible causes

        ✅ Give general health advice
        """
    )

# ==========================
# RIGHT PANEL
# ==========================

with right:

    st.markdown("""
    <div class="card">
    <h2>📄 Upload Medical Report</h2>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload PDF or Image",
        type=[
            "pdf",
            "png",
            "jpg",
            "jpeg"
        ]
    )

    if uploaded_file:

        if uploaded_file.type == "application/pdf":

            reader = PyPDF2.PdfReader(uploaded_file)

            report_text = ""

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    report_text += text

            st.success("PDF uploaded successfully.")

            with st.expander("Preview Report"):
                st.write(report_text[:4000])

        else:

            image = Image.open(uploaded_file)

            st.image(
                image,
                caption="Uploaded Report",
                use_container_width=True
            )

            st.success("Image uploaded successfully.")
