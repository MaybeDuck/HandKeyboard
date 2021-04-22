import cv2
import mediapipe as mp
import time
from ActiveFingerTracker import indentify
cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands
hands = mpHand.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils


timenew = 0
timeOld = 0


while True:
    if cv2.waitKey(1) == 13:
        break

    suc, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h,w,c = img.shape

    result = hands.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    landmarkList = []
    if result.multi_hand_landmarks:
        for handMS in result.multi_hand_landmarks:
            for id, mark in enumerate(handMS.landmark):
                x = int(mark.x * w)
                y = int(mark.y * h)
                landmarkList.append((id, int(x) ,int(y)))
                mpDraw.draw_landmarks(img, handMS, mpHand.HAND_CONNECTIONS)


    img = cv2.flip(img,1)
    indentify(landmarkList, w, img)

    timenew = time.time()
    if timenew != timeOld:
        fps = 1 / (timenew - timeOld)
        timeOld = timenew
        black = (0, 0, 0)
        cv2.putText(img, str(int(fps)), (25, 50), cv2.FONT_HERSHEY_PLAIN, 3, black, 3)
    cv2.imshow("Finger Keyboard", img)