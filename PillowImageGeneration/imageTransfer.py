from PIL import Image, ImageChops
from os.path import join

cat = Image.open(join('resources', 'cat.jpg'))
dog = Image.open(join('resources', 'dog.jpg'))
bird = Image.open(join('resources', 'cardPath', 'bird.png'))
raccoon = Image.open(join('resources', 'raccoon.jpg'))
checkerboard = Image.open(join('resources', 'checkerboard.jpg'))
circle = Image.open(join('resources', 'circle.jpg'))

## Paste an image with a mask
#print(checkerboard.mode)
#cat.paste(
#    im = bird,
#    box = (100,200),
#    mask = checkerboard.resize(raccoon.size).convert('L'))
#cat.show()

# Past an image with a blending mode
image_chops = ImageChops.difference(dog, cat)
image_chops = ImageChops.subtract(dog, cat)
image_chops = ImageChops.overlay(dog, cat)