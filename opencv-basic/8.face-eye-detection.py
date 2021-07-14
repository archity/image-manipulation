import cv2


def detect_face_eye():
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    while True:
        # Get a frame of the video
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Locations (positions) of all the faces
        faces = face_cascade.detectMultiScale(gray, 1.3, minNeighbors=5)

        # Loop through all the possible (detected) faces
        for (x, y, w, h) in faces:
            # Draw a box around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

            # Actual area of the face (pixels that represent it)
            # In both grayscale and colour
            roi_gray = gray[y:y + w, x: x + w]
            roi_color = frame[y:y + h, x: x + w]

            # `eyes` tell us the location of the eyes relative to the `roi_gray` (aka face)
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

            for (ex, ey, ew, eh) in eyes:
                # Draw a box on the `roi_color`, at positions determined by `eyes`
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

        cv2.imshow("Frame", frame)

        # Wait for 1 ms for a key pressed,
        # if it's q, then stop showing the video frame
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the camera resource
    cap.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_face_eye()
