import cv2
import numpy as np

# Load an image from file in grayscale
image = cv2.imread('Kitten.jpeg', cv2.IMREAD_GRAYSCALE)

# Ensure the image is not None
if image is not None:
    # Apply Canny edge detection
    edges = cv2.Canny(image, 50, 150)

    # Display the original and edge-detected images (optional)
    cv2.imshow('Original Image', image)
    cv2.imshow('Edge Detection', edges)

    # Save the edge-detected image
    cv2.imwrite('edge_detected_image.jpg', edges)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error loading the image.")
