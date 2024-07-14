import PIL.Image

image_path = "./yo.bmp"

def glitch(image_path, find, replace):
    # Abre la imagen
    image = PIL.Image.open(image_path)
    image = image.convert('RGB')
    
    # Saca los bytes de la imagen, esto elimina el header
    image_bytes = image.tobytes()
    print(image_bytes)
    # sort by value
    modified_bytes = sorted(image_bytes)

    # Crea una nueva imagen, esto agrega un header con los bytes modificados
    glitched_image = PIL.Image.frombytes('RGB', image.size, bytes(modified_bytes))

    # Guarda la imagen
#random values
from random import randint

glitch(image_path, 255, 0)
