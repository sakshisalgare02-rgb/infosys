import streamlit as st
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

st.title("Document Q&A Chatbot")

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load existing Chroma database
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

# Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# User input
query = st.text_input("Ask a question from documents:")

# Retrieve answer
if query:
    docs = retriever.invoke(query)

    if len(docs) == 0:
        st.write("No relevant information found.")
    else:
        st.subheader("Answer from documents:")
        for doc in docs:
            st.write(doc.page_content)
            st.write("---")