import PIL.Image

def dither(image, colors=8):
    return image.convert("P").quantize(colors=colors, method=PIL.Image.Quantize.MEDIANCUT, dither=PIL.Image.FLOYDSTEINBERG)