from PIL import Image, ImageEnhance

# Import an image
image = Image.open ('path/to/img.png')

# Create an enhancer
vibrance_enhancer = ImageEnhance.Color(image)
contrast_enhancer = ImageEnhance.Contrast(image)
brightness_enhancer = ImageEnhance.Brightness(image)
sharpness_enhancer = ImageEnhance.Sharpness(image)

# Apply the enhancer
ehanced_image = vibrance_enhancer.enhance(0)
ehanced_image = contrast_enhancer.enhance(2.5)

# Show
image.show()
ehanced_image.show()

