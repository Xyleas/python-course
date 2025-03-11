from PIL import Image, ImageFilter

# Create an iamge
image = Image.open('path/to/image.png')

# Apply a filter
image_blur = image.filter(ImageFilter.BLUR)
image_contour = image.filter(ImageFilter.CONTOUR)
image_emboss = image.filter(ImageFilter.EMBOSS)
image_sharpen = image.filter(ImageFilter.SHARPEN)
image_edge = image.filter(ImageFilter.FIND_EDGES)

# Apply advanced filters
image_boxblur = image.filter(ImageFilter.BoxBlue(radius = 4))
image_gaussian = image.filter(ImageFilter.GaussianBlur(radius = 4))
image_median = image.filter(ImageFilter.MedianFilter(size = 4))
image_unsharp = image.filter(ImageFilter.UnsharpMask(radius = 4, percent = 150, threshold = 3))

# Show the image
image_blur.show()
image_contour.show()
image_emboss.show()
image_sharpen.show()
image_boxblur.show()
image_edge.show()
image_gaussian.show()
image_median.show()

# Save
image_blur.save('nameOfNewSaveFile.png', 'png')