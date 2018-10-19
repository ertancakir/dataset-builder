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

        i = 0
        for c in contours:
            c = np.array(c)
            c = c.reshape(len(c),2)

            x_max = np.max(c[:,0])
            x_min = np.min(c[:,0])
            y_max = np.max(c[:,1])
            y_min = np.min(c[:,1])

            
            #print("{Sol Ust = (" + str(x_min) + "," + str(y_min) + ")")
            #print("Sag Ust = (" + str(x_max) + "," + str(y_min) + ")")
            #print("Sol Alt = (" + str(x_min) + "," + str(y_max) + ")")
            #print("Sag Alt = (" + str(x_max) + "," + str(y_max) + ")}\n")

            
            if math.fmod(i,3) == 2:
                tmpImage = im
                crop_img = tmpImage[y_min:y_max, x_min:x_max]
                cv2.imwrite(imageName + str(i) + '.png',crop_img)
            i+=1
            

        

