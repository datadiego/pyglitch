from PIL import Image
from random import randint
import sys
if __name__ == "__main__":
    image_path = sys.argv[1]
    image = Image.open(image_path)
    image = image.resize((image.width // 2, image.height // 2), Image.NEAREST)
    width = randint(10, 1000)
    height = randint(10, 1000)
    image = image.resize((width, height), Image.NEAREST)
    image.save(image_path, quality=0.1, optimize=False)