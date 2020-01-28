import numpy as np
import utils.make_coordinates as make_coordinates

def averaged_slope_intercept(image, lines, left, right):
    left_fit=[]
    right_fit=[]
    global left_avg
    global right_avg

    try:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            parameters = np.polyfit((x1, x2), (y1,y2), 1)
            slope = parameters[0]
            intercept= parameters[1]
            if slope < 0:
                left_fit.append((slope, intercept))
                left = left_fit.copy()
            elif slope > 0:
                right_fit.append((slope, intercept))
                right = right_fit.copy()
    except Exception as e:
        left_fit = left
        right_fit = right
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    if str(left_fit_average) != str('nan'):
        left_avg=left_fit_average
    if str(right_fit_average) != str('nan'):
        right_avg=right_fit_average
    left_line = make_coordinates.make_coordinates(image, left_avg)
    right_line = make_coordinates.make_coordinates(image, right_avg)
    return np.array([left_line, right_line])
