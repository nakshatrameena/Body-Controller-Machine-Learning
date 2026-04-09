import streamlit as st
import cv2
import numpy as np
import requests
import mediapipe as mp

API_URL = "https://your-api-url/predict"

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

st.title("🧠 Gesture Recognition")

img_file = st.file_uploader("Upload Image")

if img_file:
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        landmarks = []
        for lm in result.multi_hand_landmarks[0].landmark:
            landmarks.extend([lm.x, lm.y])

        res = requests.post(API_URL, json={"landmarks": landmarks})
        st.success(res.json()["gesture"])