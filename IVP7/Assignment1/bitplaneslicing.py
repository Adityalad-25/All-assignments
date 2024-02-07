import cv2

import numpy as np


# Load an image from file in grayscale

image = cv2.imread('Kitten.jpeg', cv2.IMREAD_GRAYSCALE)


# Ensure the image is not None

if image is not None:

    # Get the height and width of the image

    height, width = image.shape


    # Initialize an array to store the bit planes

    bit_planes = np.zeros((8, height, width), dtype=np.uint8)


    # Iterate through each bit position (from 0 to 7)

    for bit_position in range(8):

        # Extract the bit plane by masking with 2^bit_position

        bit_planes[bit_position] = (image >> bit_position) & 1


        # Convert the bit plane to a 0-255 range for visualization

        bit_planes[bit_position] *= 255


        # Display the bit plane (optional)

        cv2.imshow(f'Bit Plane {bit_position}', bit_planes[bit_position])


    # Wait for a key press and close windows

    cv2.waitKey(0)

    cv2.destroyAllWindows()

else:

    print("Error loading the image.")