import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

watermarked_image = cv2.imread('watermarked_image.png')
# watermarked_image = cv2.imread('fake_ss.png')
watermark_image = cv2.imread('watermark.png')
watermark_image = cv2.resize(watermark_image, (watermarked_image.shape[1], watermarked_image.shape[0]))

watermark_image_gray = cv2.cvtColor(watermark_image, cv2.COLOR_BGR2GRAY)

gray_watermarked_image = cv2.cvtColor(watermarked_image, cv2.COLOR_BGR2GRAY)
watermark = cv2.bitwise_and(gray_watermarked_image, watermark_image_gray)
ret, extracted_watermark_mask = cv2.threshold(watermark, 0, 255, cv2.THRESH_BINARY)

ssim_score = ssim(watermark_image_gray, extracted_watermark_mask, multichannel=True)
if ssim_score > 0.9:
    print("The image is authenticate.")
else:
    print("The image could be a fake.")
