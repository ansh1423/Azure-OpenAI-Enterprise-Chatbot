from fastapi import FastAPI
from src.chatbot.chat_engine import ChatEngine

app = FastAPI(title="Azure OpenAI Enterprise Chatbot")

engine = ChatEngine()

@app.get("/")
def health():
    return {"status": "healthy"}

@app.get("/chat")
def chat(query: str):
    return engine.ask(query)
