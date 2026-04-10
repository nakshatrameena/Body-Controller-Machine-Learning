import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import numpy as np
import mediapipe as mp

from services.model_service import get_model
from services.feature_engineering import extract_features

model = get_model()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

st.title("🧠 Gesture Recognition System (Live)")

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    gesture_text = "No Hand"

    if result.multi_hand_landmarks:
        landmarks = []
        for lm in result.multi_hand_landmarks[0].landmark:
            landmarks.extend([lm.x, lm.y])

        try:
            features = extract_features(landmarks)

            # ⚠️ adjust depending on your feature shape
            prediction = model.predict(features)

            gesture_text = prediction[0]

        except Exception as e:
            gesture_text = "Error"

    cv2.putText(img, f"Gesture: {gesture_text}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    return img

webrtc_streamer(
    key="gesture",
    video_frame_callback=video_frame_callback
)