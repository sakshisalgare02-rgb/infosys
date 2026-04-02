import streamlit as st
from components.navbar import navbar
from components.hero import hero
from components.footer import footer




# ✅ Navbar
navbar()

# ✅ Background + Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e6f0ff, #ffffff);
}

.title {
    font-size:40px;
    font-weight:bold;
    text-align:center;
    color:#003366;
}

.subtitle {
    font-size:22px;
    text-align:center;
    color:#004080;
}

.section {
    text-align:center;
    padding:20px;
}
</style>
""", unsafe_allow_html=True)

# ✅ Hero Section
hero()

# ✅ Extra Content (Project Intro)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<p class="title">Welcome to AI Document Chatbot</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload documents and ask questions intelligently using AI</p>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <h3>✨ Features</h3>
    <p>✔ Ask questions from documents</p>
    <p>✔ Multiple PDF support</p>
    <p>✔ Chat history</p>
    <p>✔ AI-powered answers</p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ✅ Footer
footer()