import numpy as np
import cv2

img = cv2.imread("assets/chessboard.png")

# Resize the image by factor (fx, fy)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.1, minDistance=10)
corners = np.int0(corners)

for corner in corners:
    # Flatten the corner array
    # [[x, y]] -> [x, y]
    x, y = corner.ravel()

    # Draw a circle around the corner
    cv2.circle(img, (x, y), radius=5, color=(255, 0, 0), thickness=2)


cv2.imshow("Chessboard Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
