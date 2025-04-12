import cv2

image_path = "images/tea-cup.jpeg"

scale_percent = 50

# Read the image
image = cv2.imread(image_path)

# Function to display an image
def display_image(image):
    # Display the image
    cv2.imshow("Tea cup Image", image)

    # Wait Key
    cv2.waitKey(0)


# Function to resize an image
def resize_image(image, scale_percent):

    # Calculate the new dimensions

    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    
    new_dim = (width, height)

    # Resize the image
    resized = cv2.resize(image, new_dim)
    return resized

# Coordinates to crop an image
start_row, start_col = 50, 50
end_row, end_col = 200, 200

# Function to cop an image
def crop_image(images, start_row, start_col, end_row, end_col):
    cropped = images[start_row:end_row, start_col:end_col]
    return cropped

# Resize the image
resized_image = resize_image(image, scale_percent)

# Crop image
cropped_image = crop_image(image, start_row, start_col, end_row, end_col)

# Display the cropped image
display_image(cropped_image)

# Call function to display the resized image.
display_image(resized_image)