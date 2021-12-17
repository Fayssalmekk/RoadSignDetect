import cv2
import numpy as np
import pytesseract
from imageio import imread

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
cap = cv2.VideoCapture(1)


while(True):

    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)
    cimg = frame.copy()
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 40)
    cv2.imshow('frame',circles)


    if np.any(circles) != None:
        for i in circles[0,:]:


            cv2.circle(frame, (int(i[0]), int(i[1])), int(i[2]), (255, 200, 0), 4)

        for j in range(len(circles)):
            x=int(circles[0][j][0])
            y=int(circles[0][j][1])
            r=int(circles[0][j][2] )
            R=int((r*0.59))
            crpd = gray[y-R : y+R , x-R : x+R]


        text = pytesseract.image_to_string(crpd)
        L=["10","20","30","40","50","60","70","80","90","100","120"]
        T=["10.jpg", "20.jpg" , "30.jpg" , "40.jpg" , "50.jpg" , "60.jpg" , "70.jpg" , "80.jpg" , "90.jpg" , "100.jpg" , "120.jpg"]



        for i in range(len(L)):
            if text==L[i]:

                print (int(text) , "Km/h")


    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()