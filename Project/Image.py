import sys  # to access the system
import cv2

img = cv2.imread("pokemon1.png", cv2.IMREAD_ANYCOLOR)

while True:
    cv2.imshow("Pokemon", img)
    cv2.waitKey(0)
    sys.exit()  # to exit from all the processes

cv2.destroyAllWindows()  # destroy all windows