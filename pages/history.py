import streamlit as st
from states.rag_state import ChatState

if "chat_state" not in st.session_state:
    st.session_state.chat_state = ChatState()

state = st.session_state.chat_state

st.title("History")

if st.button("Clear History"):
    st.session_state.chat_state.history = []
    st.success("History cleared!")

for chat in state.history:
    st.write("Q:", chat["question"])
    st.write("A:", chat["answer"])
    st.write("Sources:", chat["sources"])
    st.write("---")

    