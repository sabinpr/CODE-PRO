from PIL import Image , ImageDraw
import numpy

img = Image.open('/home/kirito/Documents/py/kirito.jpg')
img.show(img)
img = Image.open('/home/kirito/Documents/py/kirito.jpg').convert('LA')
img_draw = ImageDraw.Draw(img)
img_draw.text((20, 250), 'SABIN PRAJAPATI', fill='BLACK')
img.save('/home/kirito/Documents/py/greyscale.png')
arr = numpy.array(img)
print (arr)
img.show(img)