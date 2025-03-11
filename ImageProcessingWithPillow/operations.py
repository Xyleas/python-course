from PIL import images, imageops

# Create a image
image = image.open('path/to/image.png')

# Position changes
image_mirror = Image.mirror(image)
image_scale = Image.scale(image, 0.5)

# Color changes
image_inverted = ImageOps.invert(image)
image_grayscale = ImageOps.grayscale(image)
image_blur = ImageOps.blur(image, 2)
image_solarize = ImageOps.solarize(image, 2)
image_posturize = ImageOps.posturize(image, 2)

# Add and remove
image_border = ImageOps.expand(image = image, border = 50, fill = (255,255,255))
image_padded = ImageOps.pad(image, (4000,6000))
image_crop = ImageOps.crop(image = image,border = 200)


# Test
print(image.size)
image_mirror.show()
image_scale.show()

# Save
image_mirror.save('nameOfNewSaveFile.png', 'png')