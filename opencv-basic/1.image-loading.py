import cv2


# Load an image in colour mode
img = cv2.imread("assets/dragon_compresed.jpg", cv2.IMREAD_COLOR)

# Resize the image by factor (fx, fy)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Rotate the image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Save the image
cv2.imwrite("assets/rotated_dragon.jpg", img)

cv2.imshow("Dragon", img)

# Wait for an infinite amount of time (until any key is pressed)
cv2.waitKey(0)

cv2.destroyAllWindows()
