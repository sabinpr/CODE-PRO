from PIL import Image , ImageDraw
import PIL.ImageOps  
image = Image.open('/home/kirito/Documents/py/kirito.jpg')

inverted_image = PIL.ImageOps.invert(image)
# img_draw = ImageDraw.Draw(inverted_image)
# img_draw.text((50,450),'BIKRAM TWAYANA' , fill ='red' )

inverted_image.save('/home/kirito/Documents/py/inverted_kirito.jpg')





