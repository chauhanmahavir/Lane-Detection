import cv2

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    blur=cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny
