import numpy as np

def extract_features(landmarks):
    lm = np.array(landmarks).reshape(21, 2)

    features = [
        np.linalg.norm(lm[0] - lm[5]),
        np.linalg.norm(lm[0] - lm[9]),
        np.linalg.norm(lm[0] - lm[13]),
        np.linalg.norm(lm[0] - lm[17]),
        np.linalg.norm(lm[5] - lm[9]),
        np.linalg.norm(lm[9] - lm[13]),
        np.linalg.norm(lm[13] - lm[17]),
        np.linalg.norm(lm[17] - lm[20]),
    ]

    return np.array([features])