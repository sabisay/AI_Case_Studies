import os
from config import PDF_DIR

def list_pdf_files():
    return [os.path.join(PDF_DIR, f) for f in os.listdir(PDF_DIR) if f.endswith(".pdf")]