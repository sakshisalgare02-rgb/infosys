from backend.rag import ask_question

class ChatState:
    def __init__(self):
        self.history = []

    def ask(self, question):
        answer, sources = ask_question(question)

        self.history.append({
            "question": question,
            "answer": answer,
            "sources": sources
        })

        return answer, sources
