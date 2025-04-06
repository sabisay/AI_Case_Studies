from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import SKLearnVectorStore
from langchain_nomic.embeddings import NomicEmbeddings

# Load the document from the .md file
with open('alice_in_wonderland (1).md', 'r', encoding='utf-8') as file:
    docs = file.read()

# Create a Document object with metadata (optional)
document = Document(page_content=docs, metadata={"source": "alice_in_wonderland"})

# Split the document into chunks
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=200
)

# Split the documents
doc_splits = text_splitter.split_documents([document])  # Pass as a list of Document objects

# Debug: Print the number of chunks created
print(f"Number of chunks created: {len(doc_splits)}")

# Add to vectorDB
vectorstore = SKLearnVectorStore.from_documents(
    documents=doc_splits,
    embedding=NomicEmbeddings(model="nomic-embed-text-v1.5", inference_mode="local"),
)

# Debug: Print vectorstore information
print("Vectorstore created successfully.")

# Create retriever
retriever = vectorstore.as_retriever(k=3)

# Test the retriever
response = retriever.invoke("agent memory")
print("Retriever response:", response)
