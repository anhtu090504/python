import cv2
import numpy as np
import math
import time

size = 500
center = (size // 2, size // 2)
radius = 200

while True:
    img = np.zeros((size, size, 3), dtype=np.uint8)
    img[:] = (60, 60, 60)

    cv2.circle(img, center, radius, (0, 255, 0), 3)

    numbers = {
        12: ("XII", 0, -1),
        3:  ("III", 1, 0),
        6:  ("VI", 0, 1),
        9:  ("IX", -1, 0)
    }

    for _, (text, dx, dy) in numbers.items():
        x = int(center[0] + dx * (radius - 30))
        y = int(center[1] + dy * (radius - 30))
        cv2.putText(
            img,
            text,
            (x - 25, y + 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 0, 255),
            2)

    t = time.localtime()
    sec = t.tm_sec
    minute = t.tm_min
    hour = t.tm_hour % 12

    sec_angle = math.radians(sec * 6 - 90)
    min_angle = math.radians(minute * 6 - 90)
    hour_angle = math.radians(hour * 30 + minute * 0.5 - 90)

    sec_x = int(center[0] + math.cos(sec_angle) * (radius - 20))
    sec_y = int(center[1] + math.sin(sec_angle) * (radius - 20))
    cv2.line(img, center, (sec_x, sec_y), (0, 0, 255), 2)

    min_x = int(center[0] + math.cos(min_angle) * (radius - 40))
    min_y = int(center[1] + math.sin(min_angle) * (radius - 40))
    cv2.line(img, center, (min_x, min_y), (255, 0, 0), 4)

    hour_x = int(center[0] + math.cos(hour_angle) * (radius - 80))
    hour_y = int(center[1] + math.sin(hour_angle) * (radius - 80))
    cv2.line(img, center, (hour_x, hour_y), (0, 255, 255), 6)

    cv2.circle(img, center, 6, (0, 255, 255), -1)

    cv2.imshow("Analog Clock - Roman Numerals", img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cv2.destroyAllWindows()
