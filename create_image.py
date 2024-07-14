import PIL.Image
from random import randint

def random_element(list):
    return list[randint(0, len(list) - 1)]

def generate_random_array(length):
    from random import randint
    array = []
    for i in range(length):
        array.append(random_element([0, 255]))
    return array

def create(width, height):
    # Modifica los bytes de la imagen
    lista = generate_random_array(width*height)
    image_bytes = bytearray(lista)
    for i in range(len(image_bytes)):
        print(image_bytes[i])

    image = PIL.Image.frombytes('L', (width, height), bytes(image_bytes))

    # Guarda la imagen
    image.save("gener.bmp")
#random values
create(50, 50)