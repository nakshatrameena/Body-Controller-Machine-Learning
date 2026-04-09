import cv2
import mediapipe as mp
import csv

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)
label = "NONE"

with open("data/gesture_dataset.csv", "a", newline="") as f:
    writer = csv.writer(f)

    while True:
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks and label != "NONE":
            for _ in range(5):  # collect multiple samples per frame
                for hand_landmarks in result.multi_hand_landmarks:
                    row = []
                for lm in hand_landmarks.landmark:
                    row.extend([lm.x, lm.y])
                row.append(label)
                writer.writerow(row)

        cv2.imshow("Collect Data", frame)

        key = cv2.waitKey(1)

        if key == ord('1'): label = "MOVE"
        elif key == ord('2'): label = "CLICK"
        elif key == ord('3'): label = "SCROLL_UP"
        elif key == ord('4'): label = "SCROLL_DOWN"
        elif key == ord('q'): break

cap.release()
cv2.destroyAllWindows()