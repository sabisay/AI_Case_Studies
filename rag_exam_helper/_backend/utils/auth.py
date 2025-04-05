import os
from huggingface_hub import HfApi
from langchain_huggingface import HuggingFaceEndpoint
from config import HF_API_TOKEN, LLM_MODEL_NAME

def check_authentication():
    try:
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_API_TOKEN
        user = HfApi().whoami()
        print(f"✅ Authenticated as {user.get('name', 'Unknown')}")
    except Exception as e:
        print("❌ Authentication failed:", str(e))

def load_llm(model_name=LLM_MODEL_NAME, temperature=0.8):
    return HuggingFaceEndpoint(repo_id=model_name, temperature=temperature)
