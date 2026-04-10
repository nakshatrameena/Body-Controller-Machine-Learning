import joblib
import os
from config.settings import MODEL_PATH

_model = None

def get_model():
    global _model

    if _model is None:
        try:
            # 🔥 Ensure absolute path (IMPORTANT for deployment)
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            model_path = os.path.abspath(os.path.join(base_dir, MODEL_PATH))

            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model not found at {model_path}")

            print(f"✅ Loading model from: {model_path}")
            _model = joblib.load(model_path)

        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise e

    return _model
