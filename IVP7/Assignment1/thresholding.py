import cv2

import numpy as np


# Load an image from file in grayscale

image = cv2.imread('Kitten.jpeg', cv2.IMREAD_GRAYSCALE)


# Ensure the image is not None

if image is not None:

    # Set a threshold value (you may need to adjust this based on your image)

    threshold_value = 127


    # Apply thresholding

    _, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)


    # Display the original and thresholded images (optional)

    cv2.imshow('Original Image', image)

    cv2.imshow('Thresholded Image', thresholded_image)


    # Save the thresholded image

    cv2.imwrite('thresholded_image.jpg', thresholded_image)


    # Wait for a key press and close windows

    cv2.waitKey(0)

    cv2.destroyAllWindows()

else:

    print("Error loading the image.")