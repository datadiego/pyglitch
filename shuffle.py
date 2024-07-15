from scripts.load_image import load_image
from scripts.resize import resize
from scripts.save_image import save_image
from scripts.array_functions import shuffle

def main():
    image = load_image("image.jpg")
    resized_image = resize(image, (100, 100))
    shuffled_image = shuffle(resized_image)
    save_image(shuffled_image, "output.jpg")
    