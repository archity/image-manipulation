import cv2


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    # Get the width of video capture
    width = int(cap.get(3))

    # Get the height of video capture
    height = int(cap.get(4))

    while True:
        # Get a frame of the video
        ret, frame = cap.read()

        # Line 1
        img = cv2.line(frame, pt1=(0, 0), pt2=(width, height), color=(255, 0, 0), thickness=10)
        # Line 2
        img = cv2.line(img, pt1=(0, height), pt2=(width, 0), color=(0, 255, 0), thickness=5)
        # Rectangle
        img = cv2.rectangle(img, pt1=(100, 100), pt2=(200, 200), color=(0, 256, 256), thickness=5)
        # Circle
        img = cv2.circle(img, center=(300, 300), radius=60, color=(0, 0, 256), thickness=-1)
        # Text
        font = cv2.FONT_HERSHEY_SIMPLEX
        img = cv2.putText(img, text="This is a text!",
                          org=(200, height-10),
                          fontFace=font,
                          color=(0, 0, 0),
                          thickness=2,
                          lineType=cv2.LINE_AA,
                          fontScale=1)

        cv2.imshow("Frame", img)

        # Wait for 1 ms for a key pressed,
        # if it's q, then stop showing the video frame
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the camera resource
    cap.release()

    cv2.destroyAllWindows()
