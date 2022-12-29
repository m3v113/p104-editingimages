import cv2
import random

image = cv2.imread(
    "p104/solar-system.jpg")

#this stuff is supposed to be stars
for i in range(0,10):
    cv2.circle(image, (random.randint(50, 1500), random.randint(100, 300)), 5, (0,0,255), -1)
    cv2.circle(image, (random.randint(50, 1500), random.randint(100, 300)), 5, (51, 87, 255), -1)
    cv2.circle(image, (random.randint(50, 1500), random.randint(100, 300)), 5, (255,255,255), -1)
    cv2.circle(image, (random.randint(50, 1500), random.randint(100, 300)), 5, (255, 0, 0), -1)

cv2.putText(image,
            "Sun",
            (90, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            3,
            (255,255,255))

cv2.putText(image,
            "Mercury",
            (125, 250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.3,
            (255,255,255))

cv2.putText(image,
            "Venus",
            (195, 260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255))

cv2.putText(image,
            "Earth",
            (290, 260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255))

cv2.putText(image,
            "Mars",
            (385, 250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255))

cv2.putText(image,
            "Jupiter",
            (570, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(image,
            "Saturn",
            (770, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(image,
            "Neptune",
            (970, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(image,
            "Uranus",
            (1120, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.imshow("plain", image)

cv2.waitKey(0)