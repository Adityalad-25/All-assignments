import cv2


# Load an image from file

image = cv2.imread('Kitten.jpeg')


# Convert the image to grayscale

gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


# Save the grayscale image

cv2.imwrite('grayscale_image.jpg', gray_image)


# Display the original and grayscale images (optional)

cv2.imshow('Original Image', image)

cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0)

cv2.destroyAllWindows()