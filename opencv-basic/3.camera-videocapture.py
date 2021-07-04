import numpy as np
import cv2


def four_frames(frame, width, height):
    """
    Create a blank canvas and put four video frames onto it.

    :param frame: the video frame
    :param width: Width of the video frame
    :param height: Height of the video frame
    :return: The image canvas with 4 frames
    """
    image = np.zeros(frame.shape, dtype=np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Top-left
    image[:height // 2, :width // 2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)

    # Bottom-left
    image[height // 2:, :width // 2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)

    # Top-right
    image[:height // 2, width // 2:] = smaller_frame

    # Bottom-right
    image[height // 2:, width // 2:] = smaller_frame

    return image


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    # Get the width of video capture
    width = int(cap.get(3))

    # Get the height of video capture
    height = int(cap.get(4))

    while True:
        # Get a frame of the video
        ret, frame = cap.read()

        image = four_frames(frame, width, height)

        cv2.imshow("Frame", image)

        # Wait for 1 ms for a key pressed,
        # if it's q, then stop showing the video frame
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the camera resource
    cap.release()

    cv2.destroyAllWindows()
