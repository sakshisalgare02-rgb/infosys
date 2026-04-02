import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.selectbox("Go to", ["Upload", "Chat", "History"])

if page == "Upload":
    import pages.upload

elif page == "Chat":
    import pages.chat

elif page == "History":
    import pages.history

