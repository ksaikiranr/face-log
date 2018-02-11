import cv2
import os
import numpy as np


def detect_face(img):
    # grayscling images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # LBP face detector
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

    # if no faces are detected then return original img
    if (len(faces) == 0):
        return None, None

    # when only one face is found extract the face area
    (x, y, w, h) = faces[0]

    # face part of the image
    return gray[y:y + w, x:x + h]


def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue
        label = int(dir_name.replace("s", ""))
        subject_dir_path = data_folder_path + "/" + dir_name
        subject_images_names = os.listdir(subject_dir_path)
        for image_name in subject_images_names:
            if image_name.startswith("."):
                continue
            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)
            cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(100)
            # detect face
            face = detect_face(image)
            cv2.imwrite(image_path,face)
    
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    

prepare_training_data("test-imgs")