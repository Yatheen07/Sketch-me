# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 11:56:10 2018

@author: yatheen!
"""
"""Import Necessary Packages """
import cv2
import numpy as np
import matplotlib.pyplot as plt

def sketchIt(image):
    
    """Step 1 : Remove noise using image denoising"""
    
    #image = cv2.fastNlMeansDenoisingColored( image , None , 10,10,7,21)
    
    """Step 2 : Convert the input image into grapyscale image
                This makes the processing faster """
    image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    
    """Step 3 : Gaussian blur to improvise and remove noise further """
    
    image = cv2.GaussianBlur(image , (5,5) , 0)

    """Step 4 : Edge Detection """
    
    alteredImage = cv2.Canny(image,10,70)
    
    """Step 5 : Invert and Binarise the Image """
    
    ret , mask = cv2.threshold(alteredImage , 100 ,255 , cv2.THRESH_BINARY_INV)
    
    return mask

cap = cv2.VideoCapture(0)

while True:
    ret , image_frame = cap.read()
    cv2.imwrite("Your Sketch" , sketchIt(image_frame))
    if cv2.waitKey(1) == 13 :
        break
    
cap.release()
cv2.destroyAllWindows()
    