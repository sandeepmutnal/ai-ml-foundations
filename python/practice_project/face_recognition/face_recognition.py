# Project 13
# Face Recognition System - Step 3
# Train Face Recognition Model

import cv2
import os
import numpy as np

dataset_path = "face_dataset"

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []
label_names = {}
label_id = 0

for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_folder):
        continue

    label_names[label_id] = person_name

    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            continue

        faces.append(image)
        labels.append(label_id)

    label_id += 1

recognizer.train(faces, np.array(labels))

recognizer.save("face_model.yml")

np.save("label_names.npy", label_names)

print("✅ Face recognition model trained successfully")
print("✅ Model saved as face_model.yml")
print("✅ Labels saved as label_names.npy")