from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def to_base64(img):
    _, buffer = cv2.imencode(".jpg", img)
    return "data:image/jpeg;base64," + base64.b64encode(buffer).decode()

@app.get("/")
def health():
    return {"status": "ok", "message": "Backend FastAPI funcionando"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        return {"error": "Imagen inválida"}

    h, w, _ = img.shape

    return {
        "resultado": {
            "clase_op": "pendiente",
            "prob_op": 0.0,
            "clase_oa": "pendiente",
            "prob_oa": 0.0
        },
        "imagenOriginal": to_base64(img),
        "info": {
            "width": w,
            "height": h
        }
    }
