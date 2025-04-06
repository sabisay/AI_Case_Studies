🙏 Acknowledgements
This project was inspired by Underfitted YouTube channel's video: "Building a RAG application using open-source models (Asking questions from a PDF using Llama2)."

*project has its own <pre>requirements.txt</pre>*

🌐 Summary
This project demonstrates advanced exam grading capabilities by combining:

Local LLM integration for private, efficient text processing
Document chunking and embedding for semantic understanding
Vector stores for efficient knowledge retrieval
Intelligent routing between local knowledge and web search
Retrieval grading techniques for accurate evaluation

📚 Alice in Wonderland Exam Grader
Alice in Wonderland Exam Grader is an advanced natural language processing application that evaluates exam responses based on the classic novel "Alice in Wonderland." Using a combination of local LLM integration, vector search, and retrieval grading techniques, this project enables automated assessment of literary comprehension with high accuracy.
🧠 Technologies Used
🤖 LLM Integration

Purpose: Powers the core language understanding and response evaluation capabilities.
Why: Local models offer privacy, reduced latency, and no usage costs while maintaining high-quality assessments.
Implementation:

<h4> A RAG project can be generalized into key steps: embedding the language, importing datasets, and creating chunks, crafting an effective prompt, and adding a grader to evaluate results. Beyond this, incorporating memory and retrieval mechanisms, such as Chroma or FAISS, is essential for efficient data access. Evaluation metrics like BLEU or ROUGE help measure performance, while deployment considerations ensure real-world usability. Optimizing each of these steps, particularly prompt design and data chunking, is crucial for building robust and scalable RAG solutions.</h4></br>

<h5>for setup the llm into our project we can use these seperate steps:</h5>
<pre>
    //Local LLM setup
    local_llm = "llama3.2"
    local_llm_instance = ChatOllama(model=local_llm, temperature=0)
    local_llm_json_mode = ChatOllama(model=local_llm, temperature=0, format="json")
</pre>

<pre>
    //API-based LLM setup (e.g., OpenAI)
    api_llm = ChatOpenAI(
    model="gpt-4",
    openai_api_key="your-api-key-here",
    temperature=0,
    max_tokens=1000  # Optional: set token limits
)
</pre>

<h5>loading and splitting the documents:</h5>
<pre>
    with open(r'yourFilePath.md', 'r', encoding='utf-8') as file: 
    document = file.read()
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=200
    )
    doc_splits = text_splitter.split_documents([document])
    print(f"Number of chunks created: {len(doc_splits)}")
</pre>

<h5>setting up embeddings and creating chunks:</h5>
<pre>
    // Load the document from the .md file
    with open(r'yourFilePath.md', 'r', encoding='utf-8') as file: 
    document = file.read()
    // Split the document into chunks
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=200
    )
    doc_splits = text_splitter.split_documents([document]) </br>
    // Local Embedding Setup
    local_embedding = LocalEmbedding(model="nomic-embed-text-v1.5", inference_mode="local")
    vectorstore_local = SKLearnVectorStore.from_documents(
    documents=doc_splits,
    embedding=local_embedding,
    )</br>
    // API Embedding Setup (e.g., OpenAI)
    openai_embedding = OpenAIEmbeddings(model="text-embedding-ada-002")
    vectorstore_openai = SKLearnVectorStore.from_documents(
    documents=doc_splits,
    embedding=openai_embedding,
    )</br>
    // Qdrant Embedding Setup
    from qdrant_client import QdrantClient
    from qdrant_client.models import VectorParams, Distance
    from langchain.embeddings import OpenAIEmbeddings  # or any other embeddings
    from langchain.vectorstores import Qdrant</br>
    // Initialize Qdrant client
    qdrant_client = QdrantClient(url="http://localhost:6333")  // replace with your Qdrant server URL if necessary</br>
    // Create a new collection in Qdrant (or use an existing one)
    collection_name = "my_vector_store"
    qdrant_client.create_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE)  // Adjust size and distance based on your embeddings
    )</br>
    // Create vector store using Qdrant
    qdrant_vectorstore = Qdrant.from_documents(
    documents=doc_splits,
    embedding=openai_embedding,  // You can use any other embedding model
    client=qdrant_client,
    collection_name=collection_name
    )
</pre>

<h5>Setting up Environment Variables and Search Tool (OPTIONAL):</h5>
<pre>
    def _set_env(var: str):
        if not os.environ.get(var):
            os.environ[var] = getpass.getpass(f"{var}: ")
    _set_env("TAVILY_API_KEY")
    _set_env("LANGSMITH_API_KEY")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "local-llama32-rag"
    os.environ["USER_AGENT"] = "MyCustomAgent/1.0"
    web_search_tool = TavilySearchResults(k=3)
</pre>

<h5>Writing a router prompt: </h5>
<pre>
    import json
    from langchain_core.messages import HumanMessage, SystemMessage
    from embeddings import llm_json_mode</br>
    Updated prompt for Alice in Wonderland questions
    router_instructions = """You are an expert at routing a user question to a vector store or web search.
    The vector store contains documents related to 'Alice in Wonderland'.
    Use the vector store for questions related to plot, characters, summary, and any specific book detail.
    Use web search for all other general knowledge topics.
    Return JSON with 'datasource': 'websearch' or 'vectorestore' based on the query context."""</br>
    //Example question about the book
    question = [HumanMessage(content="Can you provide a summary of Alice in Wonderland?")]
    //Query the vector store
    test_vectore_store = llm_json_mode.invoke([SystemMessage(content=router_instructions)] +     question)</br>
    //Print the output to check the routing
    output = json.loads(test_vectore_store.content)
    print(output)
</pre>
