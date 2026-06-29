# Project 13
# Final Face Recognition System

import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

label_names = np.load("label_names.npy", allow_pickle=True).item()

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

camera = cv2.VideoCapture(0)

print("✅ Face Recognition App Started")
print("Press 'q' to quit")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Camera not working")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        face_image = gray[y:y+h, x:x+w]

        label, confidence = recognizer.predict(face_image)

        name = label_names.get(label, "Unknown")

        if confidence > 80:
            name = "Unknown"
            color = (0, 0, 255)
            message = "Unknown Face Detected"
        else:
            color = (0, 255, 0)
            message = f"Welcome {name}"

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        cv2.putText(
            frame,
            f"{name} | Confidence: {round(confidence, 2)}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

        cv2.putText(
            frame,
            message,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2
        )

    cv2.imshow("Final Face Recognition App", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()