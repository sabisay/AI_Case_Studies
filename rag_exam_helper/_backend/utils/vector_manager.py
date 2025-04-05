import os
from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from config import VECTORSTORE_DIR, EMBEDDING_MODEL_NAME

def get_vectorstore_path(pdf_filename):
    return os.path.join(VECTORSTORE_DIR, f"{pdf_filename}.faiss")

def load_or_create_vectorstore(pdf_filename, chunks, force=False):
    path = get_vectorstore_path(pdf_filename)
    embedder = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    if not force and os.path.exists(path):
        return FAISS.load_local(path, embeddings=embedder, allow_dangerous_deserialization=True)

    vectorstore = FAISS.from_documents(chunks, embedder)
    vectorstore.save_local(path)
    return vectorstore