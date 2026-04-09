import pyautogui

def perform_action(gesture):
    if gesture == "MOVE":
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 10, y)

    elif gesture == "CLICK":
        pyautogui.click()

    elif gesture == "SCROLL_UP":
        pyautogui.scroll(20)

    elif gesture == "SCROLL_DOWN":
        pyautogui.scroll(-20)
        
        print("Gesture detected:", gesture)