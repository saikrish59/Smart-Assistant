
import streamlit as st
from app.document_handler import handle_file_upload
from app.chat_agent import chat_with_agent

st.title("📄 Smart AI Assistant")
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])
query = st.text_input("Ask something:")

if uploaded_file:
    docs = handle_file_upload(uploaded_file)
    if query:
        response, reasoning = chat_with_agent(query, docs)
        st.markdown("### 🤖 Response")
        st.write(response)
        st.markdown("### 🧠 Reasoning")
        st.write(reasoning)
