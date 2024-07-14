import sys
import PIL.Image

def find_and_replace(image_path, output_path, find, replace):
    # Abre la imagen
    image = PIL.Image.open(image_path)
    image = image.convert('RGB')
    # Saca los bytes de la imagen, esto elimina el header
    image_bytes = image.tobytes()
    # Modifica los bytes de la imagen
    modified_bytes = bytearray(image_bytes)
    for i in range(len(modified_bytes)):
        modified_bytes[i] = replace if modified_bytes[i] == find else modified_bytes[i]
    # Crea una nueva imagen, esto agrega un header con los bytes modificados
    glitched_image = PIL.Image.frombytes('RGB', image.size, bytes(modified_bytes))
    # Guarda la imagen
    glitched_image.save(output_path)

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
    
    find_and_replace(image_path, output_path, find, replace)