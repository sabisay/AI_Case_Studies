from langchain_ollama import ChatOllama

local_llm = "llama3.2"
llm = ChatOllama(model=local_llm, temperature=0)
llm_json_mode = ChatOllama(model=local_llm, temperature=0, format="json")
