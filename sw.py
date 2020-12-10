import cv2
import numpy as np 
x,y,z=200,200,-1
cap= cv2.VideoCapture(0)

def take_inp(event, x1,y1,flag,param):
    gloabal x,y,k
    if event == cv2.EVENT_LBUTTONDOWN:
        x=x1
        y=y1
        k=1

cv2.nameWindow("enter_point")
cv2
