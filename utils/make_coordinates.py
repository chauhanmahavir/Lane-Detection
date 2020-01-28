import numpy as np

def make_coordinates(img, line_para):
    slope, intercept = line_para
    try:
        y1 = img.shape[0]
        y2 = int(y1*(4/5))
        x1 = int((y1 - intercept)/slope)
        x2 = int((y2 - intercept)/slope)
        return np.array([x1, y1, x2, y2])
    except Exception as e:
        print("OverflowError")
