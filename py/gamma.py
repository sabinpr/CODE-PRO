import numpy as np
import cv2

img = cv2.imread('/home/kirito/Documents/py/kirito.jpg')
gamma_two_point_two = np.array(255*(img/255)**2.2,dtype='uint8')

img3 = cv2.hconcat([gamma_two_point_two])
cv2.imshow('Gamma_SABINpjpt',img3)
cv2.waitKey(0)