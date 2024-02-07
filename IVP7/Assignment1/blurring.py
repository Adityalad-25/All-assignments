import cv2
import numpy as np

# Load an image from file
image = cv2.imread('Kitten.jpeg')

# Ensure the image is not None
if image is not None:
    # Apply Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Display the original and blurred images (optional)
    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image', blurred_image)

    # Save the blurred image
    cv2.imwrite('blurred_image.jpg', blurred_image)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error loading the image.")
