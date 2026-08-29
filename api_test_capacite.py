from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"status": "Elka AI - deploy OK, ajoute vocab.json et.pt pour TON IA"}

@app.get("/api/info")
def info():
    return {"modele": "ONE DEV AI - en attente de ton.pt", "fichiers_manques": ["vocab.json", "one_dev_ai_v3_best.pt"]}

@app.get("/api/capacite")
def capacite():
    return {"message": "Ajoute ton modele pour tester la capacite"}
