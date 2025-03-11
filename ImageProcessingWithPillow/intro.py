from PIL import Image 

# Create an image via import
image = Image.open('path/to/image.png')

# Analyze the image
print(image.size)
print(image.filename)
print(image.format)

# Flip the image
image = image.transpose(Image.transpose.FLIP_LEFT_RIGHT)

# Rotate the image
image_rotated = image.rotate(30)
image_rotated.show()
image_rotated.save('nameOfNewSaveFile.png', 'png')

# Show the image
image.show()

