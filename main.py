import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Define HSV ranges for colors
colors = {
    "PINK": {
        "lower": np.array([140, 40, 40]),
        "upper": np.array([165, 255, 255]),
        "box": (255, 0, 255)
    },
    "GREEN": {
        "lower": np.array([35, 40, 40]),
        "upper": np.array([85, 255, 255]),
        "box": (0, 255, 0)
    },
    "YELLOW": {
        "lower": np.array([15, 40, 40]),
        "upper": np.array([40, 255, 255]),
        "box": (0, 255, 255)
    },
    "BLUE": {
        "lower": np.array([100, 40, 40]),
        "upper": np.array([130, 255, 255]),
        "box": (255, 0, 0)
    },
    "WHITE": {
        "lower": np.array([0, 0, 200]),
        "upper": np.array([179, 40, 255]),
        "box": (255, 255, 255)
    }
}

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not detected")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, data in colors.items():
        lower = data["lower"]
        upper = data["upper"]
        box_color = data["box"]

        mask = cv2.inRange(hsv, lower, upper)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            if cv2.contourArea(cnt) > 800:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h),
                              box_color, 2)
                cv2.putText(frame, color_name,
                            (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, box_color, 2)

    cv2.imshow("Multi Color Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()