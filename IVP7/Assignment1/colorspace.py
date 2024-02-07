import cv2
import numpy as np

# Load an image from file
image = cv2.imread('Kitten.jpeg')

# Ensure the image is not None
if image is not None:
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Display the original and HSV images (optional)
    cv2.imshow('Original Image', image)
    cv2.imshow('HSV Image', hsv_image)

    # Save the HSV image
    cv2.imwrite('hsv_image.jpg', hsv_image)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error loading the image.")
