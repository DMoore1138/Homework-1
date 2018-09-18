import cv2
import numpy as np

image=cv2.imread("IMG_3138.JPG")
cv2.imshow('IMG_3138', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_copy=image
image_new=cv2.resize(image, (8, 8))
data=np.asarray(image)
i,j,k=image.shape

wsize=int(float(2)*i)
hsize=int(30+j)
resized_image=cv2.resize(image, (wsize, hsize))

print("Image Dimensions")
print(i,j,k)
print("Pixel Values")
print(data)
print("New Image size")
print(image_new)
print("Resized Image")
print(resized_image)


