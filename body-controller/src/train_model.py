import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.feature_engineering import extract_features

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from services.feature_engineering import extract_features
from config.settings import DATA_PATH, MODEL_PATH

def train_model():
    print("📊 Loading dataset...")

    data = pd.read_csv(DATA_PATH)

    if data.shape[1] != 43:
        print(f"❌ Invalid dataset shape: {data.shape}")
        print("Expected: 42 features + 1 label")
        return

    X_raw = data.iloc[:, :-1].values
    y = data.iloc[:, -1]

    # Convert 42 → 8 features
    X = []
    for row in X_raw:
        X.append(extract_features(row)[0])

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    print("✅ Model trained and saved")

if __name__ == "__main__":
    train_model()