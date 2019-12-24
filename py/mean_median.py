import numpy as np
import cv2
from matplotlib import pyplot as plt
image2 = cv2.imread('/home/kirito/Documents/py/kirito.jpg')

figure_size = 9
new_image = cv2.blur(image2,(figure_size, figure_size))
cv2.imshow('Mean_SABINpjpt',new_image)

image = cv2.imread("/home/kirito/Documents/py/kirito.jpg", cv2.COLOR_BGR2GRAY)
image = cv2.medianBlur(image, 5)
cv2.imshow("Median_SABINpjpt", image)
cv2.waitKey(0)