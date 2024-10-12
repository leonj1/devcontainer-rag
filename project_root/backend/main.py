from fastapi import FastAPI, Request
import requests

app = FastAPI()

RAG_APP_URL = "http://localhost:4342/query"  # Assuming the RAG app is running on port 4342

@app.post("/echo")
async def echo(request: Request):
    body = await request.json()
    return {"echo": body}

@app.post("/query")
async def query(request: Request):
    body = await request.json()
    user_input = body.get("query")
    
    if not user_input:
        return {"error": "No query provided"}
    
    try:
        response = requests.post(RAG_APP_URL, json={"query": user_input})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to communicate with RAG app: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
