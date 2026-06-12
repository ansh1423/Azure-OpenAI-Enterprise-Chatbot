from fastapi import FastAPI

app = FastAPI(title="Azure OpenAI Enterprise Chatbot")

@app.get("/")
def health():
    return {"status":"healthy"}
