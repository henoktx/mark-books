import cv2 as cv
import easyocr

reader = easyocr.Reader(['pt'], gpu=True)
img = cv.imread(cv.samples.findFile('../docs/mark-books.png'))

text_detected = reader.readtext(img)

for bbox, text, score in text_detected:
    if score > 0.65:
        cv.rectangle(img, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 1)

cv.imwrite('output.png', img)
cv.imshow('Image', img)
cv.waitKey(0)