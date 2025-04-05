import os
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME")
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME")
PDF_DIR = os.getenv("PDF_DIR")
CHUNK_DIR = os.getenv("CHUNK_DIR")
VECTORSTORE_DIR = os.getenv("VECTORSTORE_DIR")