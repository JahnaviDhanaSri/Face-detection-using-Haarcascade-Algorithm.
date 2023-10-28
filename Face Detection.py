import imutils
import cv2

print("Give the file name of the image including the extension (.jpeg/.jpg...)")
image = input()
minNeighbors = int(input("give minNeighbors value :"))
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread(image)
image = imutils.resize(image, width=500)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rects = detector.detectMultiScale(gray_image, scaleFactor=1.05,minNeighbors=minNeighbors, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
cv2.imshow("Image", image)
cv2.waitKey(120000)
