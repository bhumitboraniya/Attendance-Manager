# Automated Attendance System using Face Recognition

This project implements an automated attendance system using face recognition technology. It utilizes the `face_recognition` and `OpenCV` libraries to identify and record the presence of students based on facial recognition through a webcam. Additionally, the system sends an email notification to students who were absent from the class.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [License](#license)

## Features
- Real-time face recognition using a webcam.
- Automatic attendance recording.
- CSV file generation for attendance records.
- Automated email notifications for absentees.
  
## Installation

### Prerequisites
Before you begin, ensure you have the following installed on your system:
- Python 3.x
- pip (Python package manager)

### Required Libraries
Install the required Python libraries using pip:

```bash
pip install face_recognition
pip install opencv-python
pip install numpy
pip install pandas
```

## Additional Setup
Face Data Preparation: Store images of all students in the faces/ directory. Ensure each image is named uniquely, matching the entries in file1.csv.

CSV Files:

file1.csv: Contains the email addresses, names, and filenames of the students' face images. Ensure the file is structured as follows:
email,name,filename

Example:

22bce503@nirmauni.ac.in,Bhumit Boraniya,bhumit.jpg \n
22bce504@nirmauni.ac.in,Shrut Patel,shrut.jpg

Attendance CSV: A new CSV file will be generated each day, named with the current date (e.g., 2024-09-04.csv), containing attendance records.


## Usage
Running the Program
To start the face recognition attendance system, run the following command in your terminal:

```bash
python your_script_name.py
```
The webcam will open, and the system will begin recognizing faces in real-time. The names of recognized students will be displayed on the screen, and their attendance will be recorded.

To stop the program, press the q key.

Sending Absent Notifications
After attendance is recorded, the system will automatically send email notifications to absent students, informing them of their absence.

Project Structure
your_script_name.py: Main script for running the face recognition attendance system.
faces/: Directory containing images of all students.
file1.csv: CSV file containing email addresses, names, and image filenames of students.
<date>.csv: Attendance CSV file generated daily.

## Configuration
Email Configuration
The script uses Gmail's SMTP server to send emails. Update the following details in the script:

sender_email: The email address from which the notifications will be sent.
username: The Gmail account username.
password: The Gmail account's app-specific password (generate this from your Google account settings).

Changing Camera Source:
The script uses the default camera (usually the laptop's webcam). If you're using an external camera, update the video_capture line:

```
video_capture = cv2.VideoCapture(1)  # Use 1, 2, or 3 for external cameras
```
