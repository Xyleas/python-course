from PIL import Image
import numpy as np
from os.path import join

# Grab Image
image = Image.open(join('resources', 'images', 'cat.jpg'))

#testing a = np.arange(15).reshape(3,5)
#testing print(a[0][3])
#testing print(a.sum())

# Image Data > Array
#testing print(image.size)
red_array = np.asarray(image.getchannel('R'))
green_array = np.asarray(image.getchannel('G'))
blue_array = np.asarray(image.getchannel('B'))
#testing print(a)
#testing print(a.shape)
#testing print(red_array)

average_color = (
    int(np.average_color(red_array)),
    int(np.average_color(green_array)), 
    int(np.average_color(blue_array))
)

new_image = Image.new('RGB', (100,100), average_color)
show.(new_image)