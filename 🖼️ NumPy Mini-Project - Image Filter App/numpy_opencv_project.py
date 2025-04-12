import numpy as np
import cv2

image_path = 'image.png'

image = cv2.imread(image_path)
print(image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(image)

cv2.imshow('Original image', image)
cv2.waitKey(0)

alpha = 1.2
beta = 50

adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
cv2.imshow('Adjusted image', adjusted)
cv2.waitKey(0)

# Custom Kernels
# Sharpening filter

sharpen_kernel = np.array([[-1, -1, -1],
                            [-1, 9, -1],
                            [-1, -1, -1]]) # All values must summate to 1.and

sharpened = cv2.filter2D(image, -1, sharpen_kernel)

cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)

# Challenge Question: Build a kernel that blurs the image.abs

blur_kernel = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]])/9 # All values must summate to 1.and

blurred = cv2.filter2D(image, -1, blur_kernel)

cv2.imshow('Blurred Image', blurred)
cv2.waitKey(0)

mean_values = np.mean(image, axis = (0, 1))

print(f"Mean values for R, G, B: {mean_values}")

mean_color_image = np.ones_like(image) * mean_values.astype(np.uint8)
cv2.imshow('Mean Color Pixel Value: ', mean_color_image)

# Boolean Masking
threshold_value = 200

mask = np.any(image > threshold_value, axis = -1)

cv2.imshow('Pixel intensity mask', mask.astype(np.uint8) * 255)
cv2.waitKey(0)

highlighted_image = image.copy()
highlighted_image[mask] = [255, 0, 0]
cv2.imshow('Highlight Image', highlighted_image)
cv2.waitKey(0)

# Image Application

def update_image(x):
    alpha = cv2.getTrackbarPos('Contrast', 'App') / 50.0
    beta = cv2.getTrackbarPos('Contrast', 'App') - 50.0
    apply_sharpen = cv2.getTrackbarPos('Toggle Sharpening', 'App')
    show_mean_color = cv2.getTrackbarPos('Toggle Sharpening', 'App')
    highlight_threshold = cv2.getTrackbarPos('Toggle Sharpening', 'App')

    output = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    if apply_sharpen:
        output = cv2.filter2D(output, -1, sharpen_kernel)
    if show_mean_color:
        mean_values = np.mean(output, axis=(0,1))
        output = np.ones_like(output) * mean_values.astype(np.uint8)
    if highlight_threshold:
        mask = np.any(output > threshold_value, axis = -1)
        output[mask] = [255, 0, 0]

    cv2.imshow('App', output)

cv2.namedWindow('App')
cv2.createTrackbar('Brightness', 'App', 50, 100, update_image)
cv2.createTrackbar('Contrast', 'App', 50, 100, update_image)
cv2.createTrackbar('Toggle Sharpening', 'App', 0, 1, update_image)
cv2.createTrackbar('Toggle Mean Color', 'App', 0, 1, update_image)
cv2.createTrackbar('Toggle Highlighting', 'App', 0, 1, update_image)

cv2.imshow('App', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

