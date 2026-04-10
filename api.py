from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.model_service import get_model
from services.feature_engineering import extract_features
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🔥 Enable CORS (IMPORTANT for Streamlit frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = get_model()

from typing import List
# ✅ Request schema (clean & safe)
class GestureInput(BaseModel):
    landmarks: list[float]


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/predict")
def predict(data: GestureInput):
    try:
        landmarks = data.landmarks

        if not landmarks or len(landmarks) < 10:
            raise HTTPException(status_code=400, detail="Invalid landmarks")

        # 🔥 Feature engineering
        features = extract_features(landmarks)

        # 🔥 Correct shape for model
        prediction = model.predict(features)

        return {"gesture": prediction[0]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))