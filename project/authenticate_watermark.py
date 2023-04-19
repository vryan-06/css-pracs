import cv2
import numpy as np

# Load the watermarked image and the watermark image
watermarked_image = cv2.imread('watermarked_image.png')
watermark_image = cv2.imread('watermark.png')
watermark_image = cv2.resize(watermark_image, (watermarked_image.shape[1], watermarked_image.shape[0]))
# Convert the watermark image to grayscale
watermark_image_gray = cv2.cvtColor(watermark_image, cv2.COLOR_BGR2GRAY)

ret, watermark_mask = cv2.threshold(watermark_image_gray, 0, 255, cv2.THRESH_BINARY)
# print(watermark_image.shape)
# print(watermarked_image.shape)
print(watermark_mask.shape)

gray_watermarked_image = cv2.cvtColor(watermarked_image, cv2.COLOR_BGR2GRAY)
print(gray_watermarked_image.shape)
watermark = cv2.bitwise_and(gray_watermarked_image, watermark_mask)

# Apply thresholding to create a binary mask of the extracted watermark
ret, extracted_watermark_mask = cv2.threshold(watermark, 0, 255, cv2.THRESH_BINARY)

# Compare the extracted watermark mask with the original watermark mask
if np.array_equal(extracted_watermark_mask, watermark_mask):
    print("The watermarked image uses the exact same watermark as the original watermark image.")
else:
    print("The watermarked image does not use the same watermark as the original watermark image.")
