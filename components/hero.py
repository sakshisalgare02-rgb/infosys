import streamlit as st

def hero():
    st.markdown("""
    <div style='text-align:center;padding:20px'>
        <h1>Welcome to AI Document Chatbot</h1>
        <p>Ask questions from your uploaded documents</p>
    </div>
    """, unsafe_allow_html=True)