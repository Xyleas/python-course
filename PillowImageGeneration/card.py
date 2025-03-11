from PIL import Image, ImageDraw, ImageFont
from os.path import join

# Images
image = Image.new('RGBA', (800,400), (255,255,255))
bird = Image.open(join('resources', 'bird.png'))
logo = Image.open(join('resources', 'logo.png'))

# Data
draw = ImageDraw.Draw(image)
font_large = ImageFont.truetype(
    font = join('resources', 'fontFileName.otf'),
    size = 60
)
font_small = ImageFont.truetype(
    font = join('resources', 'fontFileName.otf'),
    size = 50
)

name = 'Mr Chirpi'
jobs = [
    'Senior flutter developer',
    'feathers.js expert',
    'ui expert'
]
company = 'Birb Inc.'
color = (50,50,50)
padding = 20
logo_padding = 4
logo_top = 280

# Name
draw.text(
    xy = (padding,padding),
    text = name,
    fill = color,
    font = font_large,
)
y = draw.textbbox(
    xy = (padding,padding),
    text = name,
    font = font_large
)[-1] + logo_padding
#Testing print(y) # Expected outputs: (20,15,301,79)

text_length = font_large.getlength(name)
#Testing print(text_length) # Expected output: 281.0
draw.line(
    xy = ((padding,y), (padding+text_length,y)),
    fill = color,
    width = 5
)

# Jobs
draw.multiline_text(
    xy = (padding, y + logo_padding + 10),
    text = '\n'.join(jobs),
    fill = color,
    font = font_small,
    spacing = 15
)

# Company
image.paste(logo, (padding, logo_top), logo)
x = padding + logo.size[0] + 10
y = logo_top + logo.size[1] / 2

text_size = draw.textbbox(
    xy = (x,y),
    text = company,
    font = font_small
    anchor = 'lm'
)
text_size_padded = (
    text_size[0] - logo_padding,
    text_size[1] - logo_padding,
    text_size[2] + logo_padding,
    text_size[3] + logo_padding
)
draw.rectangle(
    xy = text_size,
    fill = color
)
draw.text(
    xy = (x, y),
    text = 'company',
    fill = (255,255,255),
    font = font_small
)

# Draw text in top left corner.
draw.text(
    xy = (0,0),
    text = 'Mr Chirpi\nSenior flutter developer\nfeathers.js expert\n ui expert',
    fill = (0,0,0),
    font = font,
    stroke_width = 1.5,
    stroke_fill = (255,0,0),
    anchor = 'mm'
)

# Draw text in bottom left corner
draw.text(
    xy = (0,750),
    text = 'Birb Inc.',
    fill = (0,0,0),
    font = font,
    stroke_width = 1.5,
    stroke_fill = (255,0,0),
    anchor = 'mm'
)

# Bird Image
image.paste(bird, (500, padding), bird)

# Show the image
image.show()