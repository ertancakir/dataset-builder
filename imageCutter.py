import cv2
import numpy as np
import math

class ImageCutter(object):
    def __init__(self,fileName):
        self.fileName = fileName
        

    def cutImage(self, imageName):
        imageList = []
        im = cv2.imread(self.fileName,0)
        ret,thresh = cv2.threshold(im,127,255,0)
        im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        cv2.imshow("Figure 1",im)
        cv2.imshow("Figure 2",im2)

        

