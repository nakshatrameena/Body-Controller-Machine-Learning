from fastapi import FastAPI
from services.model_service import get_model
from services.feature_engineering import extract_features

app = FastAPI()
model = get_model()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/predict")
def predict(data: dict):
    landmarks = data["landmarks"]
    features = extract_features(landmarks)
    prediction = model.predict(features)
    return {"gesture": prediction[0]}