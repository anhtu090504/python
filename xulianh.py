import cv2 as cv
import numpy as np
import urllib.request


# =============== ĐỌC ẢNH TỪ URL ===============
def read_img_url(url):
    req = urllib.request.urlopen(url)
    img_rw = np.asarray(bytearray(req.read()), dtype=np.uint8)
    return cv.imdecode(img_rw, cv.IMREAD_COLOR)


# =============== THÊM NHIỄU MUỐI TIÊU ===============
def add_muoi_tieu(img, ratio=0.02):
    noisy = img.copy()
    h, w, _ = img.shape
    num = int(ratio * h * w)

    x = np.random.randint(0, h, num)
    y = np.random.randint(0, w, num)
    noisy[x, y] = 255

    x = np.random.randint(0, h, num)
    y = np.random.randint(0, w, num)
    noisy[x, y] = 0

    return noisy


# =============== PHÁT HIỆN CẠNH (EDGES) ===============
def detect_edges(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    edges = cv.Canny(blur, 60, 160)
    return edges


# =============== MAIN ===============================
if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/udacity/CarND-LaneLines-P1/master/test_images/solidWhiteCurve.jpg"
    img = read_img_url(url)

    # Ảnh gốc
    cv.imshow("Original Image", img)

    # Ảnh sau khi thêm nhiễu muối tiêu
    img_muoi_tieu = add_muoi_tieu(img, 0.02)
    cv.imshow("Salt & Pepper Noise", img_muoi_tieu)

    # Ảnh phát hiện cạnh từ ảnh gốc
    edges = detect_edges(img)
    cv.imshow("Edges (Canny)", edges)

    cv.waitKey(0)
    cv.destroyAllWindows()
