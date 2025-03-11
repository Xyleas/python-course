from PIL import Image, ImageDraw, ImageFont
from os.path import join

# Create a new image
image = Image.new('RGB', (500,200), (30,30,30))

# Create a font
font = ImageFont.truetype(
    font = join('resources, fontFileName.otf'),
    size = 25)

# Drawable Object
draw = ImageDraw.Draw(image)

# Multiline Text
draw.multiline_text(
    xy = (100,200),
    text = 'First line\nSecond line',
    font = font,
    spacing = 200
)

# Get text size
print(font.getbbox('First line'))
draw.rectangle(
    xy = font.getbbox('First line')
)

draw.rectangle(
    xy = draw.multiline_textbbox(
        xy = (100,200),
        text = 'First line\nSecond line',
        font = font,
        spacing = 200
    )
)

# Show the image
image.show()