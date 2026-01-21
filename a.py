import cv2 as cv
import numpy as np

cell = 50
board_size = 8
N = cell * board_size

img = np.zeros((N, N, 3), dtype=np.uint8)

for i in range(board_size):
    for j in range(board_size):
        if (i + j) % 2 == 0:
            img[i*cell:(i+1)*cell, j*cell:(j+1)*cell] = [255, 255, 255]
        else:
            img[i*cell:(i+1)*cell, j*cell:(j+1)*cell] = [255, 0, 0]

cv.imshow("Chessboard Color", img)
cv.waitKey(0)
cv.destroyAllWindows()
#if (m+n )% 2 == 0,
    #cv.rectangle(img, (j+100, i*100), (j+1)*100, (i+1)*100,(255, 255, 255))