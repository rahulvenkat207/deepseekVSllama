import os

import streamlit as st

from rag_utility import process_document_to_chromadb, answer_question


# Set working directory (optional, ensures saving in project dir)
working_dir = os.getcwd()

st.title("🐋 DeepSeek-R1 vs 🦙 Llama-3")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Define save path
    save_path = os.path.join(working_dir, uploaded_file.name)
    # Save file
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    process_documents = process_document_to_chromadb(uploaded_file.name)
    st.info("Document Processed Successfully")


user_question = st.text_area("Ask your question from the document")

if st.button("Answer"):
    answer = answer_question(user_question)
    answer_deepseek = answer["answer_deepseek"]
    answer_llama3 = answer["answer_llama3"]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### DeepSeek-r1 Response")
        st.code(answer_deepseek, language="markdown")

    with col2:
        st.markdown("### Llama-3 Response")
        st.code(answer_llama3, language="markdown")
