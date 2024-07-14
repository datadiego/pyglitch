import PIL.Image
def find_replace(image, find, replace):
    image_bytes = image.tobytes()
    modified_bytes = bytearray(image_bytes)
    for i in range(len(modified_bytes)):
        modified_bytes[i] = replace if modified_bytes[i] == find else modified_bytes[i]
    image = PIL.Image.frombytes('RGB', image.size, bytes(modified_bytes))
    return image