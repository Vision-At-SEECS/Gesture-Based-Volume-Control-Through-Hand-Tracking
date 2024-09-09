import cv2
import mediapipe as mp
import handTrackerModule as htm
import numpy as np
import time
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

hCam, wCam = 480, 640


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
vol_range = volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-20.0, None)
minvol = vol_range[0]
maxvol = vol_range[1]
vol = 0

vid = cv2.VideoCapture(0)
vid.set(3, wCam)
vid.set(4, hCam)
pTime = 0
volBar = 380
volper = 0

detector = htm.handDetector(minConfidence=0.7)

while True:
    success, img = vid.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmlist = detector.getPos(img, draw=False)
    if lmlist:
        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(img, (x1, y1), 5, (0, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 5, (0, 0, 0), cv2.FILLED)
        cv2.circle(img, (cx, cy), 5, (0, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 2)

        # print("1")
        # if abs(lmlist[4][1]-lmlist[8][1]) < 8:
        #     print("close")

        length = math.hypot(x2 - x1, y2 - y1)
        # print("2")
        # print(length)

        # hand range = 150 - 12
        #  vol range = 0 - -65
        vol = np.interp(length, [12, 150], [minvol, maxvol])
        volBar = np.interp(length, [12, 150], [380, 150])
        volper = np.interp(length, [12, 150], [0, 100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)
        if length < 18:
            cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 380), (0, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 380), (0, 0, 0), cv2.FILLED)
    cv2.putText(
        img,
        f"{int(volper)}%",
        (50, 420),
        cv2.FONT_HERSHEY_TRIPLEX,
        1,
        (0, 0, 0),
        1,
        cv2.LINE_AA,
    )

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(
        img,
        f"FPS: {int(fps)}",
        (50, 50),
        cv2.FONT_HERSHEY_TRIPLEX,
        1,
        (0, 0, 0),
        1,
        cv2.LINE_AA,
    )

    cv2.imshow("vid", img)
    if cv2.waitKey(1) == ord("q"):
        break
