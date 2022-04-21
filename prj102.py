import cv2 

def captureImage () :
    vidObj = cv2.VideoCapture(0)
    result = True
    while (result) :
        ret,frame = vidObj.read()
        cv2.imwrite("img1.png", frame)
        result = False
    vidObj.release()
    cv2.destroyAllWindows()

captureImage()