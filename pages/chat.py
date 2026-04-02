import streamlit as st
from states.rag_state import ChatState
from components.navbar import navbar
from components.footer import footer

# ✅ Navbar
navbar()

# ✅ Session State Fix (VERY IMPORTANT)
if "chat_state" not in st.session_state:
    st.session_state.chat_state = ChatState()

state = st.session_state.chat_state

# ✅ CSS Styling
st.markdown("""
<style>
.stApp {
    background-color: #e6f0ff;
}

.title {
    font-size:36px;
    font-weight:bold;
    text-align:center;
    color:#003366;
}

.subtitle {
    font-size:20px;
    text-align:center;
    color:#004080;
}

.chat-user {
    background-color: #cce5ff;
    padding:10px;
    border-radius:10px;
    margin:5px;
    text-align:right;
}

.chat-bot {
    background-color: #e6ffe6;
    padding:10px;
    border-radius:10px;
    margin:5px;
    text-align:left;
}
</style>
""", unsafe_allow_html=True)

# ✅ Title
st.markdown('<p class="title">🤖 AI Document Chatbot</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ask questions from your uploaded documents</p>', unsafe_allow_html=True)

# ✅ Input
query = st.text_input("Ask your question")

# ✅ Button Action
if st.button("Ask"):
    if query.strip() != "":
        answer, sources = state.ask(query)

# ✅ Chat Display (ChatGPT style 💬)
for chat in state.history:
    st.markdown(f'<div class="chat-user">🧑 {chat["question"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-bot">🤖 {chat["answer"]}</div>', unsafe_allow_html=True)
    
    # Sources
    st.markdown(
        f"<small>Sources: {', '.join([str(s) for s in chat['sources']])}</small>",
        unsafe_allow_html=True
    )

# ✅ Footer
footer()