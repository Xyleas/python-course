from PIL import Image

# Import an image
Image.open('path/to/image.png')

#Flip
image_transpose = image.transpose(Image.transpose.ROTATE_90)

# Rotation
image_rotate = image.rotate(45, expand = False, center = (0,0))

# Crop
image_crop = image.crop((800,600,1600,1000))

# Resize
image_resize = image.resize((1000,600))

# Combine
combined_image = image.transpose(Image.Transpose.Rotate_90).resize((2000,1500)).rotate(10)

# Display image
combined_image.show()

# Save
combined_image.save('nameOfNewSaveFile.png', 'png')