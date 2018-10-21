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
            #I divided it to 7 because there were 7 columns and 7 rows in test image
            i_width = (x_max - x_min) / 7
            i_height = (y_max - y_min) / 7
             
            #print("{Sol Ust = (" + str(x_min) + "," + str(y_min) + ")")
            #print("Sag Ust = (" + str(x_max) + "," + str(y_min) + ")")
            #print("Sol Alt = (" + str(x_min) + "," + str(y_max) + ")")
            #print("Sag Alt = (" + str(x_max) + "," + str(y_max) + ")}\n")
            if i == 1:
                big_image = im[y_min:y_max, x_min:x_max]
                x_min = 1
                x_max = i_width + 1
                y_min = -i_height + 1
                y_max = 0 - 1
                for k in range(1,50):
                    temp = big_image
                    if math.fmod(k,7) == 1:
                        x_min = 1
                        x_max = i_width
                        y_min += i_height
                        y_max += i_height
                    cropped_image = temp[y_min:y_max, x_min:x_max]
                    cv2.imwrite(imageName + str(k) + '.png',cropped_image)
                    imageList.append(imageName + str(k) + '.png')
                    x_min += i_width
                    x_max += i_width
                break
            i+=1

        return imageList

        

