import cv2
import numpy as np

def black_white(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    return sketch

def cartoon(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(blur, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def sepia(img):
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    sepia = cv2.transform(img, kernel)
    return np.clip(sepia, 0, 255).astype(np.uint8)

def inverted(img):
    return cv2.bitwise_not(img)

def hdr(img):
    return cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)

def oil_painting(img):
    return cv2.xphoto.oilPainting(img, 7, 1)

def pencil_color(img):
    dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    return dst_color

def ghibli_style(img):
    # Placeholder: You’ll need to integrate a pre-trained model here
    return cartoon(img)  # Temporary fallback

def neural_style(img):
    # Placeholder: You’ll need to load a PyTorch model here
    return sepia(img)  # Temporary fallback