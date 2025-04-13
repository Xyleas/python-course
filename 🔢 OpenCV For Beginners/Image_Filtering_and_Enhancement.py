import cv2
import numpy as np

def display_image(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
def apply_blur(image, kernel_size):

    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    return blurred_image

def apply_sharpening(image):

    sharpening_kernel = np.array([[-1, -1, -1],
                                [-1, 9, -1],
                                [-1, -1, -1]])

    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

    return sharpened_image

def main():
    # Referenbce to the path of our image
    image_path = "images/tea-cup.jpeg"

    image = cv2.imread(image_path)

    # Kernal size is for blurring / defines the size of the filter
    kernal_size = 5

    blurred_image = apply_blur(image, kernel_size)

    sharpened_image = apply_sharpening(image)
    # Display original image
    display_image(image)

    # Display blurred image
    display_image(blurred_image)

    # Display sharpened image
    display_image(sharpened_image)

# Call our main function
main()