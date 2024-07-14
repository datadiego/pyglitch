import sys
import PIL.Image

def glitch(image_path, output_path, find, replace):
    # Abre la imagen
    image = PIL.Image.open(image_path)
    image = image.convert('RGB')
    
    # Saca los bytes de la imagen, esto elimina el header
    image_bytes = image.tobytes()

    # Modifica los bytes de la imagen
    modified_bytes = bytearray(image_bytes)
    for i in range(len(modified_bytes)):
        modified_bytes[i] = replace if modified_bytes[i] == find else modified_bytes[i]
        if i < len(modified_bytes) - 1:
            modified_bytes[i+1] = replace if modified_bytes[i+1] == find else modified_bytes[i+1]

    # Crea una nueva imagen, esto agrega un header con los bytes modificados
    glitched_image = PIL.Image.frombytes('RGB', image.size, bytes(modified_bytes))
    
    # Guarda la imagen en el archivo de salida especificado
    glitched_image.save(output_path)
    print(f"Imagen guardada como {output_path}")

if __name__ == "__main__":
    # Verifica que se proporcionen suficientes argumentos
    if len(sys.argv) != 3:
        print("Uso: python find.py <imagen_original> <imagen_salida>")
        sys.exit(1)

    # Obtén los nombres de archivo de los argumentos de línea de comandos
    image_path = sys.argv[1]
    output_path = sys.argv[2]
    find = sys.argv[3]
    replace = sys.argv[4]

    # Valores de reemplazo (find y replace)
    find = 0
    replace = 255

    # Llama a la función glitch con los argumentos proporcionados
    glitch(image_path, output_path, find, replace)
