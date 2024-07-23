import sys
from scripts.load_image import load_image
from scripts.save_image import save_image
from scripts.array_functions import randomize, shift, sort_hue, replace_random_pixel
from scripts.get_argv import get_args
from random import randint
if __name__ == "__main__":
    filename = __file__.split("/")[-1]
    image_path, output_path, iteraciones = get_args(3, f"python {filename} <string image_path> <string output_path> <int iteraciones>")
    iteraciones = int(iteraciones)

    print(f"image_path: {image_path}")
    print(f"output_path: {output_path}")
    print(f"iteraciones: {iteraciones}")

    image = load_image(image_path)
    replaced = image
    for i in range(iteraciones):
        if i % 500 == 0:
            print(f"iteracion {i}")
            save_image(replaced, output_path)
        replaced = replace_random_pixel(replaced)
    save_image(replaced, output_path)

    print(f"Imagen guardada como {output_path}")
    