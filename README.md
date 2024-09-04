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
