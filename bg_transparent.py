import cv2
import numpy as np

# Load the grayscale image
image_path = './Image.jpg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Ensure the image was loaded
# Convert the grayscale image to BGR (still grayscale in appearance but has 3 channels)
bgr_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Create an alpha channel based on the intensity of the grayscale image
# White pixels (255) become fully transparent (0 in the alpha channel)
# Black pixels (0) remain fully opaque (255 in the alpha channel)
# alpha_channel = 255 - gray_image
_, mask = cv2.threshold(gray_image, 63, 255, cv2.THRESH_BINARY_INV)

# Merge the BGR image and the alpha channel to create an RGBA image
rgba_image = cv2.merge((bgr_image[:,:,0], bgr_image[:,:,1], bgr_image[:,:,2], mask))

# Save the resulting image
output_path = 'stripped_Image.png'
cv2.imwrite(output_path, rgba_image)
print("Image saved with white pixels converted to transparent.")
