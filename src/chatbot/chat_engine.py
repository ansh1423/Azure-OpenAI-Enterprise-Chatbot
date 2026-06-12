from src.rag.retriever import Retriever

class ChatEngine:
    def __init__(self):
        self.retriever = Retriever()

    def ask(self, query):
        docs = self.retriever.retrieve(query)

        return {
            "query": query,
            "documents": docs,
            "response": "AI-generated enterprise response"
        }
