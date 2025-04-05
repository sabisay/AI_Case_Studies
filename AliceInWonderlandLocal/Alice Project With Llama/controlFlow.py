from langgraph.graph import StateGraph
from IPython.display import Image, display
from graphState import GraphState
from main import web_search, grade_documents, retrieve, generate, route_question, decide_to_generate, grade_generation_v_documents_and_question
from langgraph.graph import END

workflow = StateGraph(GraphState)

# Define the nodes
workflow.add_node("websearch", web_search)  # web search
workflow.add_node("retrieve", retrieve)  # retrieve
workflow.add_node("grade_documents", grade_documents)  # grade documents
workflow.add_node("generate", generate)  # generate

# Build graph
workflow.set_conditional_entry_point(
    route_question,
    {
        "websearch": "websearch",
        "vectorstore": "retrieve",
    },
)
workflow.add_edge("websearch", "generate")
workflow.add_edge("retrieve", "grade_documents")
workflow.add_conditional_edges(
    "grade_documents",
    decide_to_generate,
    {
        "websearch": "websearch",
        "generate": "generate",
    },
)
workflow.add_conditional_edges(
    "generate",
    grade_generation_v_documents_and_question,
    {
        "not supported": "generate",
        "useful": END,
        "not useful": "websearch",
        "max retries": END,
    },
)

# Compile
graph = workflow.compile()

# # Save and display the graph
# image_path = r"C:\Users\ishak\Downloads\workflow_graph.png"
# with open(image_path, "wb") as f:
#     f.write(graph.get_graph().draw_mermaid_png())  # Save the PNG data to a file

# print(f"Graph saved to {image_path}.")
# display(Image(image_path))  # Display the saved graph image


inputs = {"question": "What are the types of agent memory?", "max_retries": 3}
for event in graph.stream(inputs, stream_mode="values"):
    print(event)
# # Test on current events
# inputs = {
#     "question": "What advice did the Caterpillar give Alice when they first met?",
#     "max_retries": 3,
# }
# for event in graph.stream(inputs, stream_mode="values"):
#     print(event)