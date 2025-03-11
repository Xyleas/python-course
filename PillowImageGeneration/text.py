from PIL import Image, ImageDraw, ImageFont
from os.path import join

# Create a new image
image = Image.new('RGB', (500,200), (240,240,240))

# Create a font
font = ImageFont.truetype(
    font = join('resources, fontFileName.otf'),
    size = 25)

# Drawable Object
draw = ImageDraw.Draw(image)

# Draw text
draw.text(
    xy = (0,0),
    text = 'Test',
    fill = (0,0,0),
    font = font,
    stroke_width = 1.5,
    stroke_fill = (255,0,0)
    anchor = 'mm'
)

image.show()