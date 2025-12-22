from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "ok", "message": "Backend FastAPI funcionando"}

@app.post("/predict")
def predict_placeholder():
    return {
        "status": "ok",
        "resultado": {
            "clase_op": "osteoporosis",
            "prob_op": 0.82,
            "clase_oa": "leve-moderado",
            "prob_oa": 0.74
        }
    }
