import cv2
import random

# Load an image in colour mode
img = cv2.imread("assets/dragon_compresed.jpg", cv2.IMREAD_COLOR)

# Resize the image by factor (fx, fy)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# opencv stores image in numpy array
print(type(img))

# Randomly distort the first 100 rows
# # First 100 rows
# for i in range(100):
#     # Iterate through all coloumns
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Extract the dragon's head and paste it somewhere else
tag = img[200:320, 100:200]
img[380:500, 100:200] = tag

cv2.imwrite("assets/copy-paste-dragonhead.jpg", img)

cv2.imshow("Morphed Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()