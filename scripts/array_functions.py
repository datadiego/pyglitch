from random import shuffle, randint
from PIL import Image
def shift(image, n):
    lista = bytearray(image.tobytes())
    lista_shifted = lista[n:] + lista[:n]
    image = Image.frombytes("RGB", image.size, bytes(lista_shifted))
    return image

def randomize(image):
    lista = bytearray(image.tobytes())
    #split a random portion of the list and add it to the end
    n = len(lista)
    split = n//randint(2, 10)
    lista = lista[split:] + lista[:split]
    image = Image.frombytes("RGB", image.size, bytes(lista))
    return image

def sort_hue(image):
    hsv_image = image.convert("HSV")
    pixels = list(hsv_image.getdata())
    sorted_pixels = sorted(pixels, key=lambda pixel: pixel[0])
    sorted_hsv_image = Image.new("HSV", image.size)
    sorted_hsv_image.putdata(sorted_pixels)
    sorted_rgb_image = sorted_hsv_image.convert("RGB")
    return sorted_rgb_image


from random import randint
from PIL import Image

def replace_random_pixel(image):
    #swap groups of 3 bytes in the image
    lista = bytearray(image.tobytes())
    n = len(lista)//3
    for i in range(3):
        index = randint(0, n-1)
        index *= 3
        lista[index], lista[index+1], lista[index+2] = lista[index+2], lista[index], lista[index+1]
    new_image = Image.frombytes("RGB", image.size, bytes(lista))
    
    return new_image
