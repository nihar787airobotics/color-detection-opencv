# 🎨 Colour Detection using OpenCV & Python

---

## 👋 About Me & This Project

Hey there! I'm currently at the **very beginning** of my journey into **Image Processing** and **Computer Vision**. This colour detection project is one of my first hands-on experiments — keeping it simple, keeping it foundational. But trust me, this is just the start. 🚀

> *"Every expert was once a beginner."*

I'm intentionally starting with the basics right now to build a strong understanding of how computers see and interpret visual data. In the upcoming days, I plan to move into **more unique, advanced, and complex projects** in the world of Computer Vision and AI. Stay tuned — bigger things are coming! 💡

---

## 📌 What is Colour Detection?

Colour Detection is the process of identifying and tracking specific colours in an image or a video stream. Using **OpenCV** (Open Source Computer Vision Library) in Python, we can:

- Detect specific colours in real-time using a webcam
- Isolate colour regions from an image
- Track objects based on their colour

It works by converting an image from **BGR** (default in OpenCV) to **HSV** (Hue, Saturation, Value) colour space, which makes it much easier to define and detect colour ranges.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core programming language |
| OpenCV (`cv2`) | Image processing & computer vision |
| NumPy | Array/matrix operations |

---

## 📦 Installation

Make sure you have Python installed, then run:

```bash
pip install opencv-python numpy
```

---

## 🚀 How It Works

### Step 1 — Capture Image / Video
```python
import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # 0 = default webcam
```

### Step 2 — Convert BGR to HSV
```python
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

### Step 3 — Define Colour Range (e.g., Red)
```python
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
```

> 🎨 **Want to detect a different colour?** It's super simple — just replace the HSV numbers in `lower_red` and `upper_red` with the values for your desired colour! For example, swap in the Blue or Green values from the HSV table below and you're good to go. No other changes needed!

### Step 4 — Create a Mask & Apply It
```python
    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)
```

### Step 5 — Display the Output
```python
    cv2.imshow("Original", frame)
    cv2.imshow("Detected Colour", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 🎯 HSV Colour Ranges (Quick Reference)

| Colour | Lower HSV | Upper HSV |
|--------|-----------|-----------|
| Red | [0, 120, 70] | [10, 255, 255] |
| Green | [36, 100, 100] | [86, 255, 255] |
| Blue | [94, 80, 2] | [126, 255, 255] |
| Yellow | [20, 100, 100] | [30, 255, 255] |

> 💡 **Tip:** Want to detect a different colour? Just grab the HSV values from the table above (or use an online HSV colour picker) and replace the numbers in your `lower` and `upper` arrays. That's literally all you need to change — one line, new colour! 🎯

---

## 📁 Project Structure

```
colour-detection/
│
├── colour_detection.py      # Main script
├── README.md                # This file
└── sample_images/           # Test images (optional)
```

---

## 🔮 What's Next?

This is just the beginning. Here's a glimpse of where I'm headed:

- 🔲 **Object Detection** using YOLO / SSD
- 🧠 **Deep Learning** with TensorFlow & PyTorch
- 👁️ **Face Recognition & Emotion Detection**
- 🖐️ **Hand Gesture Control**
- 🚗 **Lane Detection for Autonomous Vehicles**
- 📊 **Real-time Object Tracking & Counting**

The goal is to go from **detecting colours** today to building **full-scale AI vision systems** tomorrow. Every line of code written now is a step toward something much bigger. 💪

---


