# Face-recognition-opencv
Face Recognition with OpenCV and face_recognition
This repository contains a Python script for performing face recognition using the OpenCV and face_recognition libraries. The script captures live video from a webcam, detects faces in the video stream, and recognizes known faces by comparing them with pre-loaded images.

Features
Dynamic Loading: Easily load multiple face images for recognition.
Real-time Recognition: Recognize faces in real-time video streams.
Multiple Person Support: Recognize and differentiate between multiple persons.
Requirements
OpenCV
face_recognition
Usage
Install the required libraries:


pip install opencv-python face_recognition

Specify the paths to the persons' image files and associated names in the script.

Run the script:

python Face-detect-vdo.py
Press 'q' to exit the video stream.

Configuration
Adjust the tolerance parameter in compare_faces for fine-tuning recognition accuracy.
Contributing
Contributions are welcome! Feel free to open issues or pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

