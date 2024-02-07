import cv2

import numpy as np


# Load an image from file

image = cv2.imread('Kitten.jpeg')

# Ensure the image is not None

if image is not None:

    negated_image = 255 - image

    cv2.imshow('Original Image', image)

    cv2.imshow('Negated Image', negated_image)

    cv2.imwrite('negated_image.jpg', negated_image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
else:
    print("Error while printing the image")