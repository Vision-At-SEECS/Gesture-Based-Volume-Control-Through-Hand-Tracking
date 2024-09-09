import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode = False, max_hand = 2 , minConfidence = 0.5, minTrackingConfidence=0.5):

        self.mode = mode
        self.max_hand = max_hand
        self.minConfidence = minConfidence
        self.minTrackingConfidence = minTrackingConfidence

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(
                    static_image_mode=self.mode,
                    max_num_hands=self.max_hand,
                    # model_complexity=self.model_complexity,
                    min_detection_confidence=self.minConfidence,
                    min_tracking_confidence=self.minTrackingConfidence
                )        
        self.mpdraw = mp.solutions.drawing_utils
        
    def findHands(self, frame, draw= True):
        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.res = self.hands.process(rgbFrame)
        # print(res.multi_hand_landmarks)
        if self.res.multi_hand_landmarks:
            for handLM in self.res.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(frame, handLM, self.mphands.HAND_CONNECTIONS)
                    
        return frame
    def getPos(self, frame, numHands = 0, draw = False):
        lmList = []

        height, width,_ = frame.shape
        if self.res.multi_hand_landmarks:
            handLM = self.res.multi_hand_landmarks[numHands]
            for id,lm in enumerate(handLM.landmark):
                # print(id,lm)
                cx,cy = int(width*lm.x), int(height*lm.y)
                lmList.append([id,cx,cy])
                if draw:     
                    cv2.circle(frame, (cx,cy), 4, (0,255,0), 3, lineType=cv2.LINE_AA)
        return lmList
    

# cv2.destroyAllWindows()

def main():
    ctime = 0
    ptime = 0
    vid = cv2.VideoCapture(0)

    detector = handDetector()

    while True:
        success, frame = vid.read()
        if success:
            frame = detector.findHands(frame)
            lmlist = detector.getPos(frame)
            if len(lmlist)!=0:
                print(lmlist[18])
        # fps measure
        ptime = time.time()
        fps = 1/(ptime-ctime)
        ctime = ptime
        # print(fps)
        
        frame = cv2.flip(frame, 1)
        frame = cv2.putText(frame, str(int(fps)), (100,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 1,cv2.LINE_AA)
        # cv2.imshow("vid", res)
        cv2.imshow("vid", frame)
        if cv2.waitKey(1) == ord("q"):
            break


if __name__ == "__main__":
    main()