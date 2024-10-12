import requests
from chromadb.api.types import Documents, EmbeddingFunction

OLLAMA_API_URL = "http://10.1.1.144:11434/api/embeddings"

class OllamaEmbeddingFunction(EmbeddingFunction):
    def __call__(self, texts: Documents) -> list[list[float]]:
        embeddings = []
        for text in texts:
            response = requests.post(OLLAMA_API_URL, json={"model": "nomic-embed-text:latest", "prompt": text})
            if response.status_code == 200:
                embedding = response.json()["embedding"]
                embeddings.append(embedding)
            else:
                print(f"Error embedding text: {response.status_code}")
        return embeddings

def get_embedding_function():
    return OllamaEmbeddingFunction()

def get_embedding_dimension():
    return 384  # The dimension of embeddings from nomic-embed-text:latest
