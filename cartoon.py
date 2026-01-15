import cv2
import numpy as np

def cartoonize(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)

    edges = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9, 7
    )

    color = img
    for _ in range(5):
        color = cv2.bilateralFilter(color, 9, 75, 75)

    data = np.float32(color).reshape((-1, 3))
    _, label, center = cv2.kmeans(
        data, 8, None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001),
        10, cv2.KMEANS_RANDOM_CENTERS
    )
    center = np.uint8(center)
    quantized = center[label.flatten()].reshape(img.shape)

    return cv2.bitwise_and(quantized, quantized, mask=edges)
