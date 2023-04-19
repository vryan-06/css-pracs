import cv2
import numpy as np
original_image = cv2.imread('luffy_1015.png')
watermark_image = cv2.imread('watermark.png')
# print(original_image.shape)
# print(watermark_image.shape)

watermark_image = cv2.resize(watermark_image, (original_image.shape[1], original_image.shape[0]))
watermark_image_gray = cv2.cvtColor(watermark_image, cv2.COLOR_BGR2GRAY)

ret, watermark_mask = cv2.threshold(watermark_image_gray, 0, 255, cv2.THRESH_BINARY)
watermark_mask_inv = cv2.bitwise_not(watermark_mask)

watermark_mask = cv2.cvtColor(watermark_mask, cv2.COLOR_GRAY2BGR)
watermark_mask_inv = cv2.cvtColor(watermark_mask_inv, cv2.COLOR_GRAY2BGR)

alpha = 0.3
watermarked_image = cv2.addWeighted(original_image, 1 - alpha, watermark_image, alpha, 0)
cv2.imwrite('watermarked_image.png', watermarked_image)

resized_image = cv2.resize(watermarked_image, (600, 400))
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()