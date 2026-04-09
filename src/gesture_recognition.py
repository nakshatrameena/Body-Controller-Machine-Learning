import logging
from services.model_service import get_model
from services.feature_engineering import extract_features

logging.basicConfig(level=logging.INFO)

def predict_gesture(landmarks):
    model = get_model()

    if len(landmarks) != 42:
        return "INVALID"

    try:
        features = extract_features(landmarks)
        prediction = model.predict(features)
        return prediction[0]
    except Exception as e:
        logging.error(e)
        return "INVALID"