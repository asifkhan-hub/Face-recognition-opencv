# import face_recognition
# import cv2

# # Function to load known face encoding from an image file
# def load_known_face(image_path):
#     image = face_recognition.load_image_file(image_path)
#     # Use the first face encoding found in the image
#     face_encodings = face_recognition.face_encodings(image)
#     if len(face_encodings) > 0:
#         known_face_encoding = face_encodings[0]
#         return known_face_encoding
#     else:
#         return None

# # Function to recognize a face in a video stream
# def recognize_face(video_capture, known_face_encoding, known_name):
#     while True:
#         # Capture each frame from the video stream
#         ret, frame = video_capture.read()
#         if not ret:
#             break

#         # Find all face locations and encodings in the current frame
#         face_locations = face_recognition.face_locations(frame)
        
#         for face_location in face_locations:
#             top, right, bottom, left = face_location

#             # Extract the face encoding for the current face
#             face_encodings = face_recognition.face_encodings(frame, [face_location])
#             if len(face_encodings) > 0:
#                 face_encoding = face_encodings[0]

#                 # Compare the face with the known face
#                 match = face_recognition.compare_faces([known_face_encoding], face_encoding, tolerance=0.6)[0]
#                 name = known_name if match else "Unknown"

#                 # Draw a rectangle around the face and display the name
#                 cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#                 font = cv2.FONT_HERSHEY_DUPLEX
#                 cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

#                 # Debug print statements
#                 print("Recognized Name:", name)

#         # Display the resulting frame
#         cv2.imshow('Video', frame)

#         # Break the loop when 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the video capture object and close all windows
#     video_capture.release()
#     cv2.destroyAllWindows()

# # Specify the path to the person's image file
# person_image_path = "/home/apycoder/Downloads/Face-Mask-Detection-master/face-recognition/Image/srk (1).jpeg"

# # Specify the name associated with the person
# person_name = "Sharukh Khan"

# # Load the known face encoding and name
# known_face_encoding = load_known_face(person_image_path)

# # Open the webcam (0 corresponds to the default webcam)
# video_capture = cv2.VideoCapture(0)

# # Run face recognition on the live video stream
# recognize_face(video_capture, known_face_encoding, person_name)
import face_recognition
import cv2

# Function to load known face encodings and names from image files
def load_known_faces(image_paths, names):
    known_face_encodings = []
    known_names = []

    for image_path, name in zip(image_paths, names):
        image = face_recognition.load_image_file(image_path)
        # Use all face encodings found in the image
        face_encodings = face_recognition.face_encodings(image)
        known_face_encodings.extend(face_encodings)
        known_names.extend([name] * len(face_encodings))

    return known_face_encodings, known_names

# Function to recognize faces in a video stream
def recognize_faces(video_capture, known_face_encodings, known_names):
    while True:
        # Capture each frame from the video stream
        ret, frame = video_capture.read()
        if not ret:
            break

        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        
        for face_location in face_locations:
            top, right, bottom, left = face_location

            # Extract the face encoding for the current face
            face_encoding = face_recognition.face_encodings(frame, [face_location])[0]

            # Compare the face with the known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
            name = "Unknown"

            # If a match is found, use the first known name
            if True in matches:
                first_match_index = matches.index(True)
                name = known_names[first_match_index]

            # Draw a rectangle around the face and display the name
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

            # Debug print statements
            print("Recognized Name:", name)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

# Specify the paths to the persons' image files
person_image_paths = [
    "Image/download.jpeg",
    "Image/srk (1).jpeg",
    # Add more image paths for person 1
    # "/path/to/person2_image1.jpg",
    # "/path/to/person2_image2.jpg",
    # Add more image paths for person 2
]

# Specify the names associated with each person
person_names = [
    "Salman Khan",
    # Add more names as needed
    "Sharukh Khan",
    # Add more names as needed
]

# Load the known face encodings and names
known_face_encodings, known_names = load_known_faces(person_image_paths, person_names)

# Open the webcam (0 corresponds to the default webcam)
video_capture = cv2.VideoCapture(0)

# Run face recognition on the live video stream
recognize_faces(video_capture, known_face_encodings, known_names)
