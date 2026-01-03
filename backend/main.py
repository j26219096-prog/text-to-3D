from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- SMART PROMPT MAP ----
MODEL_MAP = {
    "human": {
        "keywords": [
            "human", "man", "woman", "person", "body",
            "anatomy", "male", "female"
        ],
        "path": "models/human.glb",
        "description": "This is a 3D model of the human body anatomy."
    },
    "heart": {
        "keywords": [
            "heart", "cardiac", "cardiology", "organ"
        ],
        "path": "models/heart.glb",
        "description": "This model represents the human heart used for medical visualization."
    },
    "chair": {
        "keywords": [
            "chair", "seat", "sofa", "stool", "furniture"
        ],
        "path": "models/chair.glb",
        "description": "This is a 3D furniture model of a chair."
    }
}


@app.get("/generate")
def generate_model(prompt: str):
    prompt = prompt.lower()

    for model_name, data in MODEL_MAP.items():
        for keyword in data["keywords"]:
            if keyword in prompt:
                return {
                    "model": data["path"],
                    "reply": f"✅ I understood your request.\n{data['description']}"
                }

    return {
        "reply": "❌ Sorry, I couldn’t understand this request yet. Try something like 'human body' or 'heart organ'."
    }




