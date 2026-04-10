import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import numpy as np

from services.model_service import get_model
model = get_model()
from src.gesture_recognition import predict_gesture

st.title("🧠 Gesture Recognition System")

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    # 👉 TODO: extract landmarks using your pose_detection
    # landmarks = extract_landmarks(img)

    # Dummy placeholder (replace with real features)
    landmarks = np.zeros(42)

    gesture = predict_gesture(landmarks)

    cv2.putText(img, f"Gesture: {gesture}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    return img

webrtc_streamer(
    key="gesture",
    video_frame_callback=video_frame_callback
)
