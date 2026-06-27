# Touchless Volume Control Using Hand Gestures

Touchless Volume Control is a computer vision-based project that allows users to control system volume using hand gestures. Instead of pressing physical buttons, the system uses a webcam to detect hand movements and adjusts the volume based on the distance between the thumb and index finger.

This project demonstrates the use of real-time hand tracking and gesture recognition for building an interactive and contactless human-computer interface.

---

## Abstract

The Touchless Volume Control System is designed to provide an efficient and hygienic way of controlling audio volume without touching any device. Using a webcam, the system captures live video and tracks hand landmarks in real time. By measuring the distance between the thumb and index finger, it maps the gesture to system volume levels.

The project is developed using Python, OpenCV, MediaPipe, NumPy, and Pycaw. It offers a practical implementation of computer vision and gesture-based interaction, making it useful for smart homes, healthcare systems, presentations, and accessibility applications.

---

## Features

* Real-time hand detection and tracking
* Touchless volume adjustment using hand gestures
* Volume percentage display on screen
* Stable volume retention when hand is removed
* Hand landmark visualization
* Smooth and responsive gesture control

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* Pycaw
* Comtypes

---

## Installation

Install the required dependencies:

```bash
pip install opencv-python mediapipe pycaw==20230407 comtypes numpy
```

---

## Usage

Run the Python file:

```bash
python volume_control.py
```

### Controls

* Move **thumb and index finger closer** → Decrease volume
* Move **thumb and index finger apart** → Increase volume
* Press **ESC** → Exit application

---

## How It Works

1. The webcam captures live video input.
2. MediaPipe detects hand landmarks.
3. The thumb tip and index finger tip are identified.
4. The distance between these points is calculated.
5. The distance is mapped to system volume.
6. The system updates the volume in real time.
7. When the hand is removed, the last volume level remains unchanged.

---

## Applications

* Smart home automation
* Touchless device control
* Healthcare environments
* Interactive presentations
* Accessibility systems

---

## Future Enhancements

* Add mute gesture support
* Implement volume bar visualization
* Add media control (play/pause)
* Support multiple hand gestures
* Cross-platform compatibility

---

## Author

Developed as a mini project for exploring Computer Vision and Gesture Recognition.
