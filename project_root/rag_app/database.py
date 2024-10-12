import chromadb
from embedder import get_embedding_function

def create_database():
    client = chromadb.Client()
    embedding_function = get_embedding_function()
    return client.create_collection("dev_containers_docs", embedding_function=embedding_function)

def add_documents(collection, texts):
    collection.add(
        documents=texts,
        ids=[f"doc_{i}" for i in range(len(texts))]
    )

def query_database(collection, query):
    results = collection.query(
        query_texts=[query],
        n_results=3
    )
    return results["documents"][0]
