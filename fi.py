# firstly we have to install this all library:
# 1) pip install face_recognition
# 2) pip install cv2
# 3) pip install opencv-python
import numpy as np
import face_recognition
# face_recognition resource: https://github.com/ageitgey/face_recognition
import csv
from datetime import datetime
import cv2
import pandas as pd
import smtplib

video_capture = cv2.VideoCapture(0)
# 0 means camera of laptop if you have any external then you can write 1,2,3.....

mail=[]
known_face_names=[]
known_face_encodings=[]

with open('file1.csv', 'r') as file:
    reader = csv.reader(file)
    # Iterate over the rows
    for row in reader:
        # Get the first column
        first_column1 = row[0]

        mail.append(first_column1)
        first_column2 = row[1]
        known_face_names.append(first_column2)

        image = face_recognition.load_image_file(f"faces/{row[2]}")
        encoding = face_recognition.face_encodings(image)[0]

        known_face_encodings.append(encoding)

#
# # Load known faces
# modi_image = face_recognition.load_image_file("faces/modi.jpg")
# # Here we need only one face out of many, So it will return only one
#
# # encoding convert image to number, so it will easy to compare image
# salaman_image = face_recognition.load_image_file("faces/salaman.jpg")
# salaman_encoding = face_recognition.face_encodings(salaman_image)[0]
#
# bhumit_image = face_recognition.load_image_file("faces/bhumit.jpg")
# bhumit_encoding = face_recognition.face_encodings(bhumit_image)[0]
#
# SD_IMAGE = face_recognition.load_image_file("faces/sd.jpg")
# sd_encoding = face_recognition.face_encodings(SD_IMAGE)[0]
#
# known_face_encodings = [modi_encoding,salaman_encoding,bhumit_encoding,sd_encoding]
# known_face_names = ["bhumit","Shrut"]
# mail = ['22bce503@nirmauni.ac.in','22bce504@nirmauni.ac.in']

# List of expected students:

students = known_face_names.copy()

face_location = []
face_encodings = []

# get current Date & Time

now = datetime.now()
current_date = now.strftime("%Y-%m-%d") # for file name

f = open(f"{current_date}.csv","w+",newline="")
# it will create new file
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    # first argument:  is your video capture success or not, The second: for frame
    small_frame = cv2.resize(frame,(0,0),fx=0.25, fy =0.25)    # for small frame
    rgb_small_frame = cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)

    # recognize_faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    # face location method for return an array of bounding boxes of human faces in image
    face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)


    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        # it will compare the faces and return true or false
        face_distance=face_recognition.face_distance(known_face_encodings,face_encoding)
        best_match_index = np.argmin(face_distance)
        # argmin - min value ki index kya hai

        if(matches[best_match_index]): # if it is true then it will execute
            name = known_face_names[best_match_index]   # we got name of person whose face match

        # display the name in frame if a person is present
            if name in known_face_names:
                font = cv2.FONT_HERSHEY_SIMPLEX  # we have to choose font for display in cvv
                bottomLeftCornerOfText = (150,40)
                fontScale = 1.5
                fontColor = (0,255, 0)
                thickness = 3
                lineType = 2
                # cv2.getText()
                cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness,
                            lineType)
                # reference -  https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
        # display the time of student when he/she was present
            if name in students:
                current_time = datetime.now().strftime("%H:%M:%S")

                aa = known_face_names.index(name)
                students.remove(name)
               # Remove the student who is present from expected student
                lnwriter.writerow([mail[aa],name,current_time])


    cv2.imshow("Attendance",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): # when you press q button it will close the cam
        break
video_capture.release()
cv2.destroyAllWindows()

f.close()

data1 = []
data2 = []
dname1 = []
dname2 = []
data = {}
# Open the CSV file
with open('file1.csv', 'r') as file:
    reader = csv.reader(file)

    # Iterate over the rows
    for row in reader:
        data1.append(row[0])
        dname1.append(row[1])
        data[row[0]] = row[1]

# Open the CSV file
with open('2023-04-26.csv', 'r') as file:
    reader = csv.reader(file)

    # Iterate over the rows
    for row in reader:
        data2.append(row[0])
        dname2.append(row[1])
reci = list(set(data1) - set(data2))
dname = list(set(dname1) - set(dname2))

# Sender and receiver email addresses
sender_email = "attendance.management.nirmauni@gmail.com"
# Gmail account login credentials
username = "attendance.management.nirmauni@gmail.com"
password = "pazmhplhinwhywsodemo"

# Email message to be sent
subject = f"Absent Report on {current_date}"



# Create a SMTP session
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Login to your Gmail account
server.login(username, password)

# Send email
print("===Absent List===")
for i in range(len(reci)):
    body = f"Dear {data[reci[i]]},\n\nI am writing this report to inform you that you were absent from our class today, {current_date}. We missed having you in class and hope everything is okay with you.\n\nIt is important that you catch up on the material covered in class as soon as possible. You can find the class notes and any assignments on our class website or by asking a classmate for their notes.\n\nIf you have any questions or need further assistance, please do not hesitate to reach out to me. I look forward to seeing you back in class soon.\n\nThanks,\n\nRachana Mehta"
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email,reci[i], message)
    print(data[reci[i]])
# Close the SMTP session
server.quit()
