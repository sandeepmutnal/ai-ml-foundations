# Project 13
# Face Recognition System - Step 2
# Capture and Save Face Images

import cv2
import os

print("🙂 Face Dataset Collection Started")

# Create dataset folder
dataset_path = "face_dataset"
os.makedirs(dataset_path, exist_ok=True)

person_name = input("Enter person name: ")

person_folder = os.path.join(dataset_path, person_name)
os.makedirs(person_folder, exist_ok=True)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

camera = cv2.VideoCapture(0)

count = 0

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
        count += 1

        face_image = gray[y:y+h, x:x+w]

        file_path = os.path.join(
            person_folder,
            f"{person_name}_{count}.jpg"
        )

        cv2.imwrite(file_path, face_image)

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Saved: {count}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Collecting Face Dataset", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    if count >= 50:
        break

camera.release()
cv2.destroyAllWindows()

print(f"✅ Saved {count} face images for {person_name}")