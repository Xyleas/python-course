import cv2

def display_image(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
def apply_blur(image, kernel_size):

    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    return blurred_image
def main():
    # Referenbce to the path of our image
    image_path = "images/tea-cup.jpeg"

    image = cv2.imread(image_path)

    # Kernal size is for blurring / defines the size of the filter
    kernal_size = 5

    blurred_image = apply_blur(image, kernel_size)

    display_image(blurred_image)

# Call our main function
main()