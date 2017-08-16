import cv2 as c
import matplotlib.pyplot as plt
im= c.imread('image.jpg',c.IMREAD_GRAYSCALE)
c.imshow("IMage",im)
c.waitKey(0)
c.destroyWindow()