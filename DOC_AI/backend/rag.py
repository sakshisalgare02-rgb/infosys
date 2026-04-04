import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# ---------------------------
# LOAD ENV VARIABLES
# ---------------------------
load_dotenv()

# ---------------------------
# EMBEDDINGS
# ---------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------------------
# VECTOR DATABASE LOAD
# ---------------------------
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings,
    collection_name="infosys_milestone1"
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# ---------------------------
# LLM (GROQ)
# ---------------------------
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------------------
# PROMPT
# ---------------------------
prompt = ChatPromptTemplate.from_template("""
You are an AI assistant.
Answer ONLY from the provided context.
If the answer is not found, say "I don't know".

Context:
{context}

Question:
{question}
""")

# ---------------------------
# MAIN FUNCTION
# ---------------------------
def ask_question(query):
    try:
        # 🔎 Retrieve documents
        docs = retriever.invoke(query)

        if not docs:
            return "No relevant documents found.", []

        # 📄 Context build
        context = "\n\n".join([doc.page_content for doc in docs])

        # 📌 Sources (clean)
        sources = []
        for doc in docs:
            src = doc.metadata.get("source", "Unknown")
            sources.append(src)

        # 🧠 Prompt create
        final_prompt = prompt.invoke({
            "context": context,
            "question": query
        })

        # 🤖 LLM response
        response = llm.invoke(final_prompt)

        return response.content, sources

    except Exception as e:
        return f"Error: {str(e)}", []