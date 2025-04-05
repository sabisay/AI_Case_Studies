import os
import getpass
from langchain_community.tools.tavily_search import TavilySearchResults

# Function to set environment variables
def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


# Set the required environment variables
_set_env("TAVILY_API_KEY")
_set_env("LANGSMITH_API_KEY")

os.environ["TOKENIZERS_PARALLELISM"] = "true"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "local-llama32-rag"
os.environ["USER_AGENT"] = "MyCustomAgent/1.0"

# Create the TavilySearchResults tool
web_search_tool = TavilySearchResults(k=3)