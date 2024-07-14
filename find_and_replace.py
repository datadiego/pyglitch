import sys
from scripts.load_image import load_image
from scripts.save_image import save_image
from scripts.find_replace import find_replace

if __name__ == "__main__":
    # Verifica que se proporcionen suficientes argumentos
    if len(sys.argv) != 5:
        print("Uso: python find_and_replace.py <input> <output> <find> <replace>")
        print(len(sys.argv))
        sys.exit(1)

    # Obtén los nombres de archivo de los argumentos de línea de comandos
    image_path = sys.argv[1]
    output_path = sys.argv[2]
    find = int(sys.argv[3])
    replace = int(sys.argv[4])

    print(f"image_path: {image_path}")
    print(f"output_path: {output_path}")
    print(f"find: {find}")
    print(f"replace: {replace}")

    # Carga la imagen
    image = load_image(image_path)

    # Encuentra y reemplaza los valores de los píxeles
    replaced = find_replace(image, find, replace)

    # Guarda la imagen en el archivo de salida especificado
    save_image(replaced, output_path)

    print(f"Imagen guardada como {output_path}")
    