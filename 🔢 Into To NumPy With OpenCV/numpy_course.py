import numpy as np
import cv2 

a = np.array([1,2,3,4])
print(a)

# N-Dimensional Arrays
one_dim_array = np.array([1,2,3,4])
print("One Dimensional Array: ", one_dim_array)

two_dim_array = np.array([[1,2,], [3,4], [5,6]])
print("Two Dimensional Array: ", two_dim_array)

three_dim_array = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print("Three Dimensional Array: ", three_dim_array)

print("Shape of 1D array: ", one_dim_array.shape)
print("Shape of 2D array: ", two_dim_array.shape)
print("Shape of 3D array: ", three_dim_array.shape)
print("Dimensions of 3D array: ", three_dim_array.ndim)
print("Data type of 3D array: ", three_dim_array.dtype)
print("Size of 3D array: ", three_dim_array.size)

chessboard = np.zeros((8,8))
print("Total squares on the chessboard: ", chessboard.size)
print(chessboard)

ones_array = np.ones((3,2))
print(ones_array)

range_array = np.arange(10)
print(range_array)

# Array Indexing and Slicing

# 1D
one_d = np.array([0,1,2,3,4,5])

# Indexing
print(one_d[2])
print(one_d[-1]) # Prints the last element

# Slicing
# array[start:stop:step] # Start = Inclusive, Stop = Exclusive, Step = Increment between indecies # Similar to python lists
print(one_d[1:4])
print(one_d[::2])

two_d = np.array([[1,2,3], [4,5,6], [7,8,9]])

# 2D Indexing
print(two_d[1,2])
print(two_d[1])

# 2D Slicing
print(two_d[0:2, 0:2])

# Array Operations

# Addition
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)

# Multiplication
print(a * 2)

# Broadcasting
matrix = np.array([1,2],[3,4],[5,6])
vector = np.array([0.5, 2.5])
print(matrix * vector)

# Universal Functions (ufuncs)
print(np.sqrt(a))
print(np.exp(a))

# A NumPy use case: OpenCV
image = cv2.imread('image.png')

print("Type of imagel: ", type(image))

print("Shape of image array: ", image.shape)

b,g,r = cv2.split(image)

print(b)
print(b.shape)

cv2.imshow('Blue Channel', b)

cv2.waitKey(0)
cv2.destroyAllWindows()

image - cv2.imread('image.png')

resized_image = cv2.resize(image, (300,200))
print(image.shape)
print(resized_image.shape)

greyscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(greyscale_image.shape)

pixel_value = image[100,100]
print("pixel value: ", pixel_value)

greyscale_pixel = greyscale_image[100, 100]
print("greyscale_pixel")

# Challenge Question
# Invert the colors of the image by subtracting the pixel values from 255.
# Hint: Use NumPy's array broadcasting feature to subtract 255 from all pixel values at once.

inverted_image = 255 - image

cv2.imshow('Original Image', image)
cv2.imshow('Inverted Image', inverted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Image Arithmetic
image1 = cv2.imread('image.png')
image2 = cv2.imread('image2.png')

image2 = cv2.resize(image2, (image1.shape[0], image2.shape[1]))

added_image = cv2.add(image1, image2)
subtracted_image = cv2.subtract(image1, image2)

alpha = 0.7
beta = 0.3
blended_image = cv2.addWeighted(image1, alpha, image2, beta, 0)

cv2.imshow("added image", added_image)
cv2.imshow("subtracted image", subtracted_image )
cv2.imshow("blended image", blended_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
