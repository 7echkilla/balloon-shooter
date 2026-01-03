import os


path = os.path.join(os.path.realpath(os.path.dirname(__file__)), "assets", "cannon.png")

from PIL import Image

try:
    image = Image.open(path)
    print(f"Image format: {image.format}, Image size: {image.size}")
    image.show()

except IOError:
    print("An error occured")

image.close()