from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(__file__)
MODEL_DIR = os.path.join(BASE_DIR, "models")

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.get("/generate")
def generate(prompt: str):
    model_file = f"{prompt}.glb"
    model_path = os.path.join(MODEL_DIR, model_file)

    if not os.path.exists(model_path):
        return {"error": "Model not found"}

    return FileResponse(
        model_path,
        media_type="model/gltf-binary",
        filename=model_file
    )
