# deepseekVSllama

Where Was That Line Again?

A few weeks ago, I was skimming through a 100+ page PDF, looking for a specific piece of information. Scrolling endlessly, using Ctrl+F, jumping back and forth—it was frustrating!

That got me thinking... 🤔

What if I could just ask a question and get the answer directly from the document? No searching, no scrolling, just instant answers.

💡 So, I built it.

I created a RAG-based Q&A system that lets you upload a document and ask questions like.

It works by:
✅ Extracting text from PDFs
✅ Splitting and indexing the content in ChromaDB
✅ Generating embeddings with HuggingFace
✅ Retrieving answers using DeepSeek-R1 70B and LLaMA-3 70B

The best part? It compares answers from both models, helping choose the most relevant one.
