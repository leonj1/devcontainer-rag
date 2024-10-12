from fastapi import FastAPI, Request
import requests

app = FastAPI()

RAG_APP_URL = "http://rag_app:4342/query"  # Assuming the RAG app is running on port 4342

@app.post("/echo")
async def echo(request: Request):
    body = await request.json()
    return {"echo": body}

from pydantic import BaseModel

class QueryInput(BaseModel):
    query: str

@app.post("/query")
async def query(input_data: QueryInput):
    if not input_data.query:
        return {"error": "No query provided"}
    
    try:
        response = requests.post(RAG_APP_URL, json={"query": input_data.query})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to communicate with RAG app: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
