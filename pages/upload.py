import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

st.title("Upload PDF")

uploaded_files = st.file_uploader("Upload files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    all_docs = []

    for file in uploaded_files:
        file_path = os.path.join("documents", file.name)

        # Save file
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        # Load PDF
        loader = PyPDFLoader(file_path)
        docs = loader.load()

        # ✅ Add source metadata
        for doc in docs:
            doc.metadata["source"] = file.name

        all_docs.extend(docs)

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    split_docs = splitter.split_documents(all_docs)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Store in Chroma DB
    vectorstore = Chroma.from_documents(
        split_docs,
        embedding=embeddings,
        persist_directory="chroma_db",
        collection_name="infosys_milestone1"
    )

    vectorstore.persist()

    st.success("Files processed and stored successfully!")