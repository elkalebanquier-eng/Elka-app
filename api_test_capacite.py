from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"status": "Elka AI - deploy OK ✅", "etape": "ajoute vocab.json et .pt apres"}

@app.get("/api/info")
def info():
    return {"modele": "ONE DEV AI - en attente", "status": "deploy OK, pret pour TON IA"}

@app.get("/api/capacite")
def capacite():
    return {"tests": [{"test": "bonjour", "reponse": "Salut, TON IA arrive bientot"}]}

@app.get("/api/chat")
def chat(question: str):
    return {"question": question, "reponse": f"Tu as demandé: {question} - TON IA arrive quand tu upload vocab.json et .pt"}
