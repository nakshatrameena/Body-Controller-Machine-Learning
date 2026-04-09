from services.model_service import get_model
import numpy as np

def test_model():
    model = get_model()
    dummy = np.zeros((1,8))
    pred = model.predict(dummy)
    print("Test prediction:", pred)

if __name__ == "__main__":
    test_model()