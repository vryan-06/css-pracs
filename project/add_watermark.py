import cv2
import numpy as np

# Load the original image and the watermark image
original_image = cv2.imread('luffy_1015.png')
watermark_image = cv2.imread('watermark.png')
# print(original_image.shape)
# print(watermark_image.shape)

watermark_image = cv2.resize(watermark_image, (original_image.shape[1], original_image.shape[0]))

# Convert the watermark image to grayscale
watermark_image_gray = cv2.cvtColor(watermark_image, cv2.COLOR_BGR2GRAY)

# Threshold the watermark image to create a binary mask
ret, watermark_mask = cv2.threshold(watermark_image_gray, 0, 255, cv2.THRESH_BINARY)

# Invert the binary mask
watermark_mask_inv = cv2.bitwise_not(watermark_mask)

# Convert the binary masks to BGR format
watermark_mask = cv2.cvtColor(watermark_mask, cv2.COLOR_GRAY2BGR)
watermark_mask_inv = cv2.cvtColor(watermark_mask_inv, cv2.COLOR_GRAY2BGR)

# Normalize the alpha value
alpha = 0.3

# Add the watermark to the original image
watermarked_image = cv2.addWeighted(original_image, 1 - alpha, watermark_image, alpha, 0)
cv2.imwrite('watermarked_image.png', watermarked_image)

# Resize the watermarked image for display
resized_image = cv2.resize(watermarked_image, (600, 400))
# Display the watermarked image
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()