---

# Human Body Pose Detection (Console Output)

## Objective

To build a Python-based system that detects a human body from a webcam feed and prints the detected **human pose** (Standing, Sitting, Hand Raised) in the terminal using an open-source pretrained model.

---

## Approach Used

* **Pose Estimation** using MediaPipe Pose (pretrained, open-source)
* **Rule-based pose classification** using detected body keypoints
* **Console-based output only** (no GUI required for results)

---

## Technologies Used

* Python 3.10
* OpenCV
* MediaPipe Pose
* NumPy

---

## Project Structure

```
HUMAN POSE DETECTION/
│
├── pose_detection.py
├── requirements.txt
└── README.md
```

---

## Installation Instructions

### 1️. Check Python Version

Make sure Python 3.8 – 3.11 is installed.

```bash
python --version
```

---

### 2. Install Required Libraries

Run the following command in the project directory:

```bash
pip install -r requirements.txt
```

### If installing manually (recommended on Windows):

```bash
pip install numpy==1.26.4
pip install opencv-python==4.8.0.76
pip install mediapipe==0.10.9
```

---

## How to Run the Program

1. Open **Command Prompt / PowerShell**
2. Navigate to the project folder:

```bash
cd "D:\Human Pose Detection"
```

3. Run the program:

```bash
python pose_detection.py
```

---

## Output

The program captures live webcam feed and prints detected poses in the terminal:

```
Pose detected: Standing
Pose detected: Hand Raised
Pose detected: Sitting
```

* Press **Q** to exit the program.
* Output is shown **only in the terminal**, as required.

---

## Supported Poses

* Standing
* Sitting
* Hand Raised

---

## Dataset Requirement

No dataset is required.

**Reason:**
The system uses a pretrained MediaPipe Pose model. Pose classification is done using rule-based logic on detected keypoints.

---