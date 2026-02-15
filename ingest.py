import os
import shutil
import time

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

print("Starting Document Ingestion Pipeline...")

# Cleanup old DB
if os.path.exists("chroma_db"):
    shutil.rmtree("chroma_db")
    print("Old database removed")

# PDF loader
pdf_loader = DirectoryLoader(
    "data",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

# Text loader
text_loader = DirectoryLoader(
    "data",
    glob="**/*.txt",
    loader_cls=TextLoader
)

documents = pdf_loader.load() + text_loader.load()
print("Documents Loaded:", len(documents))

# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=3000,
    chunk_overlap=200
)

docs = splitter.split_documents(documents)
print("Chunks created:", len(docs))

# Metadata cleaning
for doc in docs:
    doc.metadata = {k: str(v) for k, v in doc.metadata.items()}

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating embeddings...")

collection_name = f"docs_{int(time.time())}"

vectorstore = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="chroma_db",
    collection_name=collection_name
)

vectorstore.persist()

print("Database built successfully!")
print("Milestone 1 completed.")