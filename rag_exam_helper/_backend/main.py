from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.auth import check_authentication, load_llm
from utils.pdf_processor import process_pdf_chunks
from utils.vector_manager import load_or_create_vectorstore
from utils.helpers import list_pdf_files
import os
from collections import OrderedDict 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

check_authentication()
llm = load_llm()

vectorstores = {}

def prepare_all():
    """Prepare vector stores for all PDFs at startup."""
    pdf_files = list_pdf_files()
    for pdf_path in pdf_files:
        pdf_name = os.path.basename(pdf_path).replace(".pdf", "")
        chunks = process_pdf_chunks(pdf_path)
        vectorstore = load_or_create_vectorstore(pdf_name, chunks)
        vectorstores[pdf_name] = vectorstore.as_retriever(k=8)

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    user_query = data.get("query", "")
    selected_pdf = data.get("pdf_name", "").replace(".pdf", "")

    if selected_pdf not in vectorstores:
        return jsonify({"error": "Invalid PDF selection."}), 400

    retriever = vectorstores[selected_pdf]
    docs = retriever.get_relevant_documents(user_query)

    # 🔹 Remove duplicates and limit retrieved docs
    unique_pages = list(OrderedDict.fromkeys(doc.page_content.strip() for doc in docs))
    context = " ".join(unique_pages[:3])  # Use top 3 unique chunks

    # 🔹 Use improved structured prompt
    full_prompt = f"""
    You are an intelligent assistant helping students answer questions based on a given document.

    **Instructions:**
    - Use **only** the provided context below to answer the question.
    - **Do not make up any information** that is not present in the context.
    - If the answer is **not in the context**, reply: "I don’t know based on the provided document."
    - Keep your answer **concise and informative**.
    - Do **not** *repeat sentences* again and again.

    **Context:**
    \"\"\"
    {context}
    \"\"\"

    **Question:** {user_query}

    **Answer**
    """

    # 🔹 Call the LLM and return the response
    answer = llm(full_prompt)
    return jsonify({"response": answer})

@app.route("/pdfs", methods=["GET"])
def get_pdfs():
    """Return a list of available PDF names."""
    pdf_files = list_pdf_files()
    pdf_names = [os.path.basename(f) for f in pdf_files]
    return jsonify({"pdfs": pdf_names})


if __name__ == "__main__":
    with app.app_context():  # Ensures the app context is created before preparing data
        prepare_all()
    app.run(debug=True)