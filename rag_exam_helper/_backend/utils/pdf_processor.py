import os, json
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from config import CHUNK_DIR

def process_pdf_chunks(pdf_path, chunk_size=1500, chunk_overlap=150, force=False):
    filename = os.path.basename(pdf_path).replace(".pdf", "")
    chunk_file = os.path.join(CHUNK_DIR, f"{filename}.json")
    
    if not force and os.path.exists(chunk_file):
        with open(chunk_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Document(page_content=d["page_content"], metadata=d["metadata"]) for d in data]

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(docs)

    with open(chunk_file, "w", encoding="utf-8") as f:
        json.dump([{"page_content": c.page_content, "metadata": c.metadata} for c in chunks], f, indent=2, ensure_ascii=False)
    
    return chunks