import PIL.Image

image_path = "./xor.bmp"

def glitch(image_path):
    # Abre la imagen
    image = PIL.Image.open(image_path)
    image = image.convert('RGB')
    
    # Saca los bytes de la imagen, esto elimina el header
    image_bytes = image.tobytes()

    # Modifica los bytes de la imagen
    modified_bytes = bytearray(image_bytes)
    for i in range(len(modified_bytes)):
        print(modified_bytes[i])

    # Crea una nueva imagen, esto agrega un header con los bytes modificados
    glitched_image = PIL.Image.frombytes('RGB', image.size, bytes(modified_bytes))

    # Guarda la imagen
    glitched_image.save("yo.bmp")
#random values
from random import randint

for i in range(255, 0, -5):
    replace = randint(0, 255)
    glitch(image_path)
