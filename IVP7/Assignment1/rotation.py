import cv2
import numpy as np

# Load an image from file
image = cv2.imread('Kitten.jpeg')

# Ensure the image is not None
if image is not None:
    # Define the rotation angle
    angle = 45

    # Rotate the image
    rows, cols, _ = image.shape
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))

    # Display the original and rotated images (optional)
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', rotated_image)

    # Save the rotated image
    cv2.imwrite('rotated_image.jpg', rotated_image)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error loading the image.")
