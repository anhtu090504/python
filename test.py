import cv2 as cv
import numpy as np
import urllib.request

def read_img_url(url):
    req = urllib.request.urlopen(url)
    img_rw = np.asarray(bytearray(req.read()), dtype=np.uint8)
    return cv.imdecode(img_rw, cv.IMREAD_COLOR)

def enhance_contrast_gray(bgr):
    # Chuyển sang ảnh xám và cân bằng sáng (CLAHE)
    gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(gray)

def get_edges_only(img):
    # 1. Tăng tương phản (để bắt vạch rõ hơn)
    gray = enhance_contrast_gray(img)
    
    # 2. Làm mờ nhẹ để giảm nhiễu hạt
    blur = cv.GaussianBlur(gray, (5,5), 0)

    # 3. Canny Edge Detection -> Đây là hàm tạo ra ảnh "Edges"
    edges = cv.Canny(blur, 60, 160)
    
    return edges

if __name__ == "__main__":
    url = "file:///C:/Users/BinhMinh/Downloads/banghieu.jpg"
    img = read_img_url(url)

    # Lấy ảnh Edges
    edges_image = get_edges_only(img)

    # Hiển thị giống hệt ảnh bạn gửi
    cv.imshow("Edges", edges_image)
    cv.waitKey(0)
    cv.destroyAllWindows()