from PIL import Image

image = Image.open('path/to/image.png')

# Get one pixel
image.getpixel((0,0))

# Grayscale images
red_grayscale_image = image.getchannel('R')
blue_grayscale_image = image.getchannel('B')

# Change the pixel color
image.putpixel((0,0), (255,0,0))

# Exercise, change the black squares of the checkerboard to red.
print(image.getpixel((00)))
for x in range(image.size[0]):
    for y in range(image.size[1]):
        if image.getpixel((x,y)) == (255,255,255):
            image.putpixel((x,y), (200,20,20))

# Test Space
image.show()
print(image.getpixel((0,0)))
red_grayscale_image.show()
blue_grayscale_image.show()