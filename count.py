from cvzone.HandTrackingModule import HandDetector
import cv2   

# Initialize webcam 
cap = cv2.VideoCapture(0) 

# Set fullscreen window
cv2.namedWindow("Finger Counter", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Finger Counter", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Initialize hand detector with max 2 hands
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    if not success:
        break

    # Detect hands and get landmarks
    hands, img = detector.findHands(img)

    total_fingers = 0
    if hands:
        for hand in hands:
            fingers = detector.fingersUp(hand)
            total_fingers += fingers.count(1)

    # Text setup
    text = f'Fingers: {total_fingers}'
    position = (50, 100)
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Black border
    cv2.putText(img, text, position, font, 2, (0, 0, 0), 6, cv2.LINE_AA)
    # White text
    cv2.putText(img, text, position, font, 2, (255, 255, 255), 2, cv2.LINE_AA)

    # Show full screen window
    cv2.imshow("Finger Counter", img)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



