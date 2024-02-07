import cv2
import numpy as np

# Load an image from file
image = cv2.imread('Kitten.jpeg')

# Ensure the image is not None
if image is not None:
    # Define the region to crop (x, y, width, height)
    x, y, w, h = 100, 50, 300, 200

    # Crop the image
    cropped_image = image[y:y + h, x:x + w]

    # Display the original and cropped images (optional)
    cv2.imshow('Original Image', image)
    cv2.imshow('Cropped Image', cropped_image)

    # Save the cropped image
    cv2.imwrite('cropped_image.jpg', cropped_image)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error loading the image.")
