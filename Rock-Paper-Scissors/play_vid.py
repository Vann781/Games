#this is the function created to play the video / pop of the video ion different conditions . Videos are in folder "Videos".
# we will be importing his file into our game.py , if we had more than one function here there aretwo methods we can use .
# 1: we can import each function  sepeartely .      2: we can import all funtions at once using " * ".
#how to import ? : see the first line of code in game.py . 
import cv2
def playVid(Path):
    while True:
        cap = cv2.VideoCapture(Path)
        ret, frame = cap.read()
        while ret:
            cv2.imshow('Result', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return
            ret, frame = cap.read()
        cap.release()
