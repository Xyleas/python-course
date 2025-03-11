from PIL import Image
from os.path import join

image1 = Image.open(join('resourse','cat.jpg')).convert('RGB')
image2 = Image.open(join('resourse','raccoon.jpg')).convert('1')
#Testing image1.show()
#Testing image2.show()

#Testing print(image1.mode)
#Testing print(image2.mode)

image1.past(image2, (100,400))

image1.show()