import numpy as np
import cv2

def display_lines(image, lines):
    try:
        line_image=np.zeros_like(image)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2=line.reshape(4)
                cv2.line(line_image, (x1,y1), (x2,y2), (255,0,0), 3)
        return line_image
    except:
        pass
