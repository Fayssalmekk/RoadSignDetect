import cv2
import numpy as np
import pytesseract
from imageio import imread
from matplotlib import pyplot as plt
from matplotlib import style

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
cap = cv2.VideoCapture(1)

crpd=0
speed_data=[0]

while(True):
    # Lancer la lecture du camera et appliquer les filtres
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)
    cimg = frame.copy()

    # detecter les cercles
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

    if np.any(circles) != None:

        for i in circles[0,:]:

            # countourer les cercles detecte
            cv2.circle(frame, (int(i[0]), int(i[1])), int(i[2]), (255, 200, 0), 4)
        # Rogner la partie de l'image qui contient un cercle
        for j in range(len(circles)):
            x=int(circles[0][j][0])
            y=int(circles[0][j][1])
            r=int(circles[0][j][2] )
            R=int((r*0.7))
        try:
            crpd = gray[y-R : y+R , x-R : x+R]


        # Lire l'image Rogner
            text = pytesseract.image_to_string(crpd)


        #Afficher la resultat
            try:
                text = int(text)
                L=[20,30,40,60,70,80,90,100,120]
                if text in L:
                    print("Speed limit:" , text , "km/h")
                    speed_data.append(text)

            except:
                pass

        except:
            pass
    cv2.imshow('frame',frame)
    if np.any(crpd):
        cv2.imshow("crpd",crpd)


    if cv2.waitKey(1) & 0xFF == 27:
        break

style.use('fivethirtyeight')

plt.plot(speed_data)
plt.title("Detected Speed")
plt.ylabel('Km/h')

plt.show()


cap.release()
cv2.destroyAllWindows()
