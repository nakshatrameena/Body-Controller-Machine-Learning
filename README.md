# 🧠 Body Controller - Gesture Recognition System

An AI-powered gesture control system that allows users to interact with their computer using hand gestures via webcam or web interface.

---

## 🚀 Live App

👉 https://body-controller-machine-learning.onrender.com/

---

## 🚀 Features

* ✋ Real-time hand gesture recognition
* 🖱️ Cursor movement using gestures *(local app)*
* 👆 Click actions
* 🔄 Scroll up / down
* 🌐 Web-based gesture prediction (Streamlit + API)
* ⚡ Fast and lightweight ML model
* 🎥 Works with webcam & uploaded images

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV**
* **MediaPipe**
* **Scikit-learn**
* **NumPy**
* **PyAutoGUI (Local only)**
* **Streamlit (Web UI)**
* **FastAPI (Backend API)**

---

## 📁 Project Structure

```
body-controller/
│
├── app.py                      # Local real-time gesture control (OpenCV + PyAutoGUI)
├── app_streamlit.py            # Streamlit web app (UI)
├── api.py                      # FastAPI backend (ML inference)
│
├── requirements.txt            # Dependencies
├── render.yaml                 # Deployment config
├── README.md                   # Documentation
│
├── data/
│   └── gesture_dataset.csv     # Raw dataset (42 features + label)
│
├── models/
│   └── gesture_model.pkl       # Trained ML model
│
├── src/
│   ├── pose_detection.py       # Hand landmark detection (MediaPipe)
│   ├── gesture_recognition.py  # Prediction logic
│   ├── action_mapper.py        # Gesture → system actions (LOCAL ONLY)
│   ├── train_model.py          # Model training script
│   ├── collect_data.py         # Dataset collection
│   └── utils.py                # Helper functions
│
├── services/                   # 🔥 Production Layer
│   ├── model_service.py        # Loads model once (singleton)
│   └── feature_engineering.py  # Feature extraction (CRITICAL)
│
├── config/
│   └── settings.py             # Paths & configs
│
├── tests/
│   └── test_model.py           # Basic model tests
│
└── .streamlit/
    └── config.toml             # Streamlit settings
```

---

## ⚙️ Installation

```bash
git clone https://github.com/nakshatrameena/Body-Controller-Machine-Learning.git
cd Body-Controller-Machine-Learning

pip install -r requirements.txt
```

---

## 📊 Step-by-Step Usage

### 1️⃣ Collect Dataset (VERY IMPORTANT)

```bash
python src/collect_data.py
```

**Controls:**

* `1` → MOVE
* `2` → CLICK
* `3` → SCROLL_UP
* `4` → SCROLL_DOWN
* `q` → Quit

👉 Collect **100+ samples per gesture** for good accuracy.

---

### 2️⃣ Train Model

```bash
python -m src.train_model
```

✔ Output:

```
models/gesture_model.pkl
```

---

### 3️⃣ Run Local Gesture Controller

```bash
python app.py
```

✔ Controls your system in real-time using gestures

---

### 4️⃣ Run Web App (UI)

```bash
streamlit run app_streamlit.py
```

---

### 5️⃣ Run Backend API (Optional)

```bash
uvicorn api:app --reload
```

✔ API endpoint:

```
POST /predict
```

---

## 🧠 How It Works

1. **MediaPipe** detects 21 hand landmarks
2. Landmarks (42 values) → converted into **engineered features (8 features)**
3. ML model predicts gesture
4. Output:

   * Local → controls mouse (PyAutoGUI)
   * Web → displays prediction

---

## ⚠️ Important Notes

* Dataset must contain:

  ```
  42 features (x,y landmarks) + 1 label
  ```
* Feature engineering must be **consistent**:

  ```
  training == prediction
  ```
* Ensure:

  * Good lighting
  * Clear hand visibility
  * Stable camera

---

## ❗ Common Errors & Fixes

### 🔴 Model not found

```bash
python -m src.train_model
```

---

### 🔴 Feature mismatch (42 vs 8)

✔ Fix:

* Always use:

```
services/feature_engineering.py
```

---

### 🔴 No hand detected

✔ Improve:

* Lighting
* Hand position
* Camera quality

---

### 🔴 ModuleNotFoundError (services)

✔ Run using:

```bash
python -m src.train_model
```

---

## 🌐 Deployment (Render)

### Start Command:

```bash
streamlit run app_streamlit.py --server.port $PORT --server.address 0.0.0.0
```

---

## 🔥 Future Improvements

* 🤖 Deep Learning (CNN / LSTM)
* 🎥 Real-time browser camera (WebRTC)
* 📱 Mobile gesture control app
* 🎤 Voice + Gesture hybrid system
* 📊 Auto dataset generation
* 🎮 Gaming controls

---

## 👨‍💻 Author

**Nakshatra Meena**

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🤝 Contribute

---

## 📜 License

This project is open-source under the MIT License.

---

# 🚀 Pro Tip

This project is now:

✅ Resume-ready
✅ Hackathon-ready
✅ Deployable
✅ Scalable (API + UI + ML pipeline)
