import cv2
import numpy as np
import face_recognition

faceClassifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

videoCapture = cv2.VideoCapture(0)
ws, hs = 1920, 1080
videoCapture.set(3, ws)
videoCapture.set(4, hs)

if not videoCapture.isOpened():
    print("Camera not accessible")
    exit()

# Put Here the picture of that person you wanna track.
img = "D:\projects\HeadShotTracking\Reference_images\img.jpg"

image = face_recognition.load_image_file(img)
face_encoding = face_recognition.face_encodings(image)[0]

known_face_encodings = [face_encoding]

qKeyPressed = False
while not qKeyPressed:

    ret, frame = videoCapture.read()

    if not ret:
        break

    if ret:
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            fx = int((left + right)/2)
            fy = top
            pos = [fx, fy]

            if matches[best_match_index]:

                cv2.circle(frame, (fx, fy), 80, (0, 0, 255), 2)
                cv2.putText(frame, str(pos), (fx + 15, fy - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                cv2.line(frame, (0, fy), (ws, fy), (0, 0, 0), 2)  # x line
                cv2.line(frame, (fx, hs), (fx, 0), (0, 0, 0), 2)  # y line
                cv2.circle(frame, (fx, fy), 15, (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, "TARGET LOCKED", (850, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
            else:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, "SAFE", (left, bottom + 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)


        cv2.imshow("Result", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            qKeyPressed = True
            break


videoCapture.release()
cv2.destroyAllWindows()
