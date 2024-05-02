import cv2
import matplotlib.pyplot as plt
import numpy as np

'''
python 3.9.13
'''
pathPic     = "LearnOpenCV/Resource/pic/TNT.png"
pathVideo   = "LearnOpenCV/Resource/video/video1.mp4"

def showPic_cv(name, img, time=0):
    cv2.imshow(name, img)
    cv2.waitKey(time)
    cv2.destroyAllWindows()

def showVideo_cv(name, vc : cv2.VideoCapture, gray:bool = False, time=40):
    if vc.isOpened():
        open, frame = vc.read()
    else:
        return
    
    while open:
        ret, frame = vc.read()
        if frame is None:
            break
        if ret == True:
            if gray:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow(name, frame)
            if cv2.waitKey(time) & 0xFF == 27:
                break

    cv2.destroyAllWindows()

img = cv2.imread(pathPic, cv2.IMREAD_GRAYSCALE)
vc = cv2.VideoCapture(pathVideo)

showVideo_cv(pathVideo, vc)
vc.release()