import cv2
import mediapipe as mp

# Initialize MediaPipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Define a function to identify ASL sign (A to E) based on finger positions
def identify_asl(landmarks):
    fingers = []

    # Thumb
    if landmarks[4].x < landmarks[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Fingers: index, middle, ring, pinky
    for tip in [8, 12, 16, 20]:
        if landmarks[tip].y < landmarks[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    # Interpret based on simple finger patterns
    if fingers == [1, 0, 0, 0, 0]:
        return "A"
    elif fingers == [0, 1, 1, 1, 1]:
        return "B"
    elif fingers == [1, 1, 1, 1, 1]:  # Simplified 'C' detection
        return "C"
    elif fingers == [0, 1, 0, 0, 0]:
        return "D"
    elif fingers == [0, 0, 0, 0, 0]:
        return "E"
    else:
        return "Unknown"

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Predict ASL sign
            sign = identify_asl(handLms.landmark)
            cv2.putText(img, f'Sign: {sign}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 3)

    cv2.imshow("ASL Detector", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
