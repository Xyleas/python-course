from PIL import Image
from os.path import join, exists
from glob import glob
from os import mkdir

logo = Image.open(join('resources', 'watermark.png'))
#testing print(glob(join('resources', 'images', '*.jpg')))
path = glob(join('resources', 'images', '*.jpg'))
images = [Image.open(path) for path in paths]
#testing print(images)
padding = 10

if not exists('watermarked'):
    mkdir('watermarked')

for image in images:
    x = image.width - padding - log.width
    y = image.height - padding - log.height
    #testing print(image.filename.split('\\')[-1][:-4])
    name = image.filename.split('\\')[-1][:-4] + '_watermark.jpg'

    image.paste(logo, (x,y), logo)
    #testing image.show()
    image.save('watermarked/{name}', 'JPEG')