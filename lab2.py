import cv2 as cv
import numpy as np

vid = cv.VideoCapture("C:/Users/BinhMinh/Downloads/bang_chuyen.mp4")

line_y = 300
count = 0

prev_centers = []   # Lưu tâm frame trước

while True:
    ret, frame = vid.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (11, 11), 0)

    _, thresh = cv.threshold(blur, 120, 255, cv.THRESH_BINARY_INV)
    thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, None, iterations=2)

    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Vẽ line đỏ
    cv.line(frame, (0, line_y), (frame.shape[1], line_y), (0, 0, 255), 2)

    current_centers = []

    for cnt in contours:
        area = cv.contourArea(cnt)
        if area < 500:
            continue

        x, y, w, h = cv.boundingRect(cnt)
        cx = x + w // 2
        cy = y + h // 2

        current_centers.append((cx, cy))

        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.circle(frame, (cx, cy), 4, (255, 0, 0), -1)

        # So với frame trước để kiểm tra cắt line
        for (px, py) in prev_centers:
            # Gần cùng vật theo trục X
            if abs(cx - px) < 30:
                # Đi từ trên xuống và cắt qua line
                if py < line_y and cy >= line_y:
                    count += 1
                    print("Count +1")

    prev_centers = current_centers.copy()

    cv.putText(frame, f"Count: {count}", (20, 40),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv.imshow("Video", frame)
    cv.imshow("Thresh", thresh)

    if cv.waitKey(30) & 0xFF == ord("q"):
        break

vid.release()
cv.destroyAllWindows()
