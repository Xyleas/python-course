from PIL import Image, ImageDraw

# Create a new image
image = Image.new('RGB', (1000,600), (255,255,255))
image.show()

# Draw shapes
draw = ImageDraw.Draw(image)
draw.rectangle(
    xy = ((0,0),(100,200)), 
    fill = (200,0,0), 
    outline = (0,20,20),
    width = 20)
draw.ellipse(
    xy = (100,200,120,220)
    fill = (132,200,115)
)
draw.line(
    xy = ([0,0), (100,50), (1000,600)]
    fill = (30,20,230),
    width = 10,
)
