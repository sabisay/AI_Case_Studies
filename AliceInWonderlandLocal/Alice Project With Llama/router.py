import json
from langchain_core.messages import HumanMessage, SystemMessage
from embeddings import llm_json_mode


# Updated prompt for Alice in Wonderland questions
router_instructions = """You are an expert at routing a user question to a vector store or web search.
The vector store contains documents related to 'Alice in Wonderland'.
Use the vector store for questions related to plot, characters, summary, and any specific book detail.
Use web search for all other general knowledge topics.
Return JSON with 'datasource': 'websearch' or 'vectorestore' based on the query context."""

# Example question about the book
question = [HumanMessage(content="Can you provide a summary of Alice in Wonderland?")]

# Query the vector store
test_vectore_store = llm_json_mode.invoke([SystemMessage(content=router_instructions)] + question)

# Print the output to check the routing
output = json.loads(test_vectore_store.content)
print(output)
