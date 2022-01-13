import cv2
import pandas as pd
import time

def draw_function(event, x, y, flags, params):
    if event==cv2.EVENT_LBUTTONDOWN:
        global r, g, b, xpos, ypos
        xpos=x
        ypos=y
        b, g, r = image[ypos,xpos]
        r=int(r)
        g=int(g)
        b=int(b)

def getColourName(R, G, B):
    min=10000
    for i in range(len(Colors)):
        d = abs(R- int(Colors.loc[i,"R"])) + abs(G- int(Colors.loc[i,"G"]))+ abs(B- int(Colors.loc[i,"B"]))
        if (d<=min):
            min=d
            colorname=Colors.loc[i,"colorname"]
    return colorname


image=cv2.imread("D:\GIT\Colour-Detection-On-Image\colorpic.jpg")

r = g = b = xpos = ypos = 0

Colors=pd.read_csv('D:\GIT\Colour-Detection-On-Image\colors.csv')

cv2.namedWindow('Image')
cv2.imshow("Image", image)
cv2.setMouseCallback('Image', draw_function)

while(True):
    cv2.rectangle(image, (20, 20), (750, 60), (0, 0, 0), -1)
    text= getColourName(r, g, b) + "  R= " + str(r) + "  G= " + str(g) + "  B= " + str(b)
    cv2.putText (image, text, (50, 50), 2, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
    print(xpos)
    cv2.imshow("Image", image)
    
    if(cv2.waitKey(0) and 0xFF==27):
        break
        
cv2.destroyAllWindows()