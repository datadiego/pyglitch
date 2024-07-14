import PIL.Image
from PIL import Image
image_path = "./gatocrimen.jpeg"

def dither(image_path, colors=8, resizeFactor=2):
    # Abre la imagen
    image = PIL.Image.open(image_path)
    image = image.resize((image.width/resizeFactor, image.height/resizeFactor), Image.NEAREST)
    image = image.convert("P").quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.FLOYDSTEINBERG)
    image = add_saturation(image, 160)
    image = image.resize((image.width*resizeFactor, image.height*resizeFactor), Image.NEAREST)


    # Guarda la imagen ditherizada
    image.save("a.bmp")

def resize(image, factor):
    return image.resize((int(image.width/factor), int(image.height/factor)))

def add_saturation(image, saturation):
    image = image.convert("HSV")
    data = image.getdata()
    newData = []
    for item in data:
        # higher saturation
        newData.append((item[0], saturation, item[2]))
    image.putdata(newData)
    image = image.convert("RGB")
    return image

dither(image_path, colors=64, resizeFactor=4)
