from PIL import Image ,ImageDraw

from PIL import ImageFilter

img = Image.open('/home/kirito/Documents/py/kirito.jpg')
img.show(img)

for i in range(0, img.size[0]-1):

    for j in range(0, img.size[1]-1):

        # Get pixel value at (x,y) position of the image

        pixelColorVals = img.getpixel((i,j));

       

        # Invert color

        redPixel    = 255 - pixelColorVals[0]; # Negate red pixel

        greenPixel  = 255 - pixelColorVals[1]; # Negate green pixel

        bluePixel   = 255 - pixelColorVals[2]; # Negate blue pixel

                   

        # Modify the image with the inverted pixel values

        img.putpixel((i,j),(redPixel, greenPixel, bluePixel));

 
img_draw = ImageDraw.Draw(img)
img_draw.text((20, 250), 'SABIN PRAJAPATI', fill='BLACK')
img.save('/home/kirito/Documents/py/negative.png')
# Display the negative image

img.show(img)