import cv2
import numpy as np


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    # Get the width of video capture
    width = int(cap.get(3))

    # Get the height of video capture
    height = int(cap.get(4))

    while True:
        # Get a frame of the video
        ret, frame = cap.read()

        # Convert BGR colours to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([130, 255, 255])

        # Create a mask enabling pixels only within a certain range
        mask = cv2.inRange(hsv, lowerb=lower_blue, upperb=upper_blue)

        # Perform bitwise AND operation of the mask with the image
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Frame", result)
        cv2.imshow("Mask", mask)

        # Wait for 1 ms for a key pressed,
        # if it's q, then stop showing the video frame
        if cv2.waitKey(1) == ord('q'):
            break
