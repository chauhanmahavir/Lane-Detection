import cv2
import numpy as np
import utils.region_of_interest as roi
import utils.averaged_slope_intercept as avg
import utils.canny as canny
import utils.display_lines as display_lines

left_avg=np.array([])
right_avg=np.array([])



cap = cv2.VideoCapture('HighWayRoad.mp4')
while(cap.isOpened()):
    _, frame = cap.read()
    canny_image= canny.canny(frame)
    cropped_image=roi.region_of_interest(canny_image)
    lines=cv2.HoughLinesP(cropped_image, rho=1.4, theta=np.pi/160, threshold=110, lines=np.array([]), minLineLength=30, maxLineGap=40)
    last_left_list=[]
    last_right_list=[]
    averaged_lines=avg.averaged_slope_intercept(frame, lines,last_left_list, last_right_list)
    line_image= display_lines.display_lines(frame, averaged_lines)
    try:
        combo_image= cv2.addWeighted(frame, 0.7, line_image, 1, 1)
    except:
        pass

    cv2.imshow('canny',combo_image)
    if cv2.waitKey(10)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
