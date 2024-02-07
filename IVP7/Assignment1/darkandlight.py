import cv2

import numpy as np


# Load an image from file

image = cv2.imread('Kitten.jpeg')


# Ensure the image is not None

if image is not None:

    # Define a constant value for darkening or lightening

    brightness_change = 50  # You can adjust this value based on your needs


    # Darken the image

    darkened_image = np.clip(image - brightness_change, 0, 255)


    # Lighten the image

    lightened_image = np.clip(image + brightness_change, 0, 255)


    # Display the original, darkened, and lightened images (optional)

    cv2.imshow('Original Image', image)

    cv2.imshow('Darkened Image', darkened_image.astype(np.uint8))

    cv2.imshow('Lightened Image', lightened_image.astype(np.uint8))


    # Save the darkened and lightened images

    cv2.imwrite('darkened_image.jpg', darkened_image.astype(np.uint8))

    cv2.imwrite('lightened_image.jpg', lightened_image.astype(np.uint8))


    # Wait for a key press and close windows

    cv2.waitKey(0)

    cv2.destroyAllWindows()

else:

    print("Error loading the image.")

