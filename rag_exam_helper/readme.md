# 🧠 RAG Exam Helper

**RAG Exam Helper** is a full-stack AI-powered application that uses **LangChain RAG (Retrieval-Augmented Generation)** on the backend and **React** on the frontend. It allows users to upload exam papers and intelligently extract relevant answers or feedback using large language models.
This project combines a **Retrieval-Augmented Generation (RAG)** backend with a modern **React + Vite** frontend. It is designed to provide a fast and interactive user experience while leveraging cutting-edge language model capabilities.

*project has its own <pre>requirements.txt</pre>*
---

## 🧠 Technologies Used

### 🔗 LangChain
- **Purpose**: LangChain is used as the orchestration framework for building the RAG pipeline.
- **Why**: It simplifies the integration of large language models with vector stores, memory, prompt templates, and document loaders. LangChain is modular, flexible, and widely supported.

### 🧪 Flask API
- **Purpose**: Acts as the backend interface between the React frontend and the LangChain-powered RAG system.
- **Why**: Flask is lightweight, easy to set up, and great for creating APIs that serve Python-based logic like LLMs and vector search tools.

### 🔍 Retrieval-Augmented Generation (RAG)
- **Purpose**: Enhances the response of the language model by retrieving relevant context from a document store before generating a response.
- **Why**: Pure LLMs can hallucinate. RAG reduces this by grounding answers in your own documents or datasets.

### 📄 Chunking
- **Purpose**: Breaks down documents into manageable and meaningful segments.
- **Why**: Improves semantic search accuracy and context relevance during retrieval. Helps the model focus on smaller, more coherent pieces of information.

### 📦 Vector Stores (FAISS)
- **Purpose**: Store document embeddings for efficient semantic similarity search.
- **Why**: They enable fast retrieval of the most relevant chunks based on a user's query. FAISS is highly optimized for performance.

---

## 💻 Frontend Technologies

### ⚛️ React
- **Purpose**: Provides a dynamic and component-based frontend interface.
- **Why**: React allows for fast development of responsive UIs and integrates smoothly with modern tooling and backend APIs.

### ⚡ Vite
- **Purpose**: Serves as the build tool and development server.
- **Why**: Vite is faster than traditional bundlers like Webpack. It offers instant server startup, lightning-fast HMR (Hot Module Replacement), and native ES module support.

---

## 🌐 Summary

This project demonstrates the powerful synergy between:
- **LLM tools (LangChain + RAG) for intelligent Q&A**,
- **Vector search for context-aware responses**, and
- **Modern frontend development (React + Vite) for user experience**.

---

> If you plan to contribute or deploy this project, please make sure to configure your `.env` file and install all dependencies in both the frontend and backend directories.
<pre> HUGGINGFACEHUB_API_TOKEN= your_api_token
LLM_MODEL_NAME=gpt2
EMBEDDING_MODEL_NAME=sentence-transformers/all-MiniLM-L6-v2
PDF_DIR=_backend/data/pdfs
CHUNK_DIR=_backend/data/chunks
VECTORSTORE_DIR=_backend/data/vectorstores </pre>
