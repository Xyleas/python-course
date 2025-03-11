from PIL import Image
from os.path import join
from glob import glob

# Imports
#Testing print(glob(join('resources', 'animation', '*.png')))
path = glob(join('resources', 'animation', '*.png'))
images = [Image.open(path) for path in paths]
#Testing print(images)

# Create the animation
images[0].save(
    fp = 'animation.gif', 
    append_images = images[1:],
    save_all = True,
    duration = 1,
    loop = 0)
