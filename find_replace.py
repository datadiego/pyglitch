import PIL.Image

def find_and_replace(image_path, find, replace):
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
    output = input("Nombre de la imagen de salida: ")
    # Guarda la imagen
    glitched_image.save(output)
