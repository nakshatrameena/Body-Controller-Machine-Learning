import cv2
from src.pose_detection import get_hand_landmarks
from src.gesture_recognition import predict_gesture
from src.action_mapper import perform_action

def main():
    cap = cv2.VideoCapture(0)
    print("✅ Camera started")

    while True:
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)

        landmarks = get_hand_landmarks(frame)

        if landmarks:
            gesture = predict_gesture(landmarks)
            perform_action(gesture)

            cv2.putText(frame, gesture, (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.imshow("Body Controller", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()