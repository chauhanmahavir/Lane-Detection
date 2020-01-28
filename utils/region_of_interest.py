import numpy as np
import cv2

def region_of_interest(image):
    height=image.shape[0]
    tringle = np.array([[(150, height), (860, height), (550,300), (450,300)]])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask, tringle, 255)
    mask_image=cv2.bitwise_and(image, mask)
    return mask_image
