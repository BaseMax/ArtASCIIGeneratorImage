import PIL
import matplotlib

# Variables
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
NEW_WIDTH = 50 # Change the size
IMAGE_PATH = "input.png"

# Functions
def resize_image(image, to_width=100):
    width, height = image.size
    ratio = height / width
    to_height = int(to_width * ratio) - 20 # Change the -20 to change the padding
    resized_image = image.resize((to_width, to_height))
    return resized_image

# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

# Startup
try:
    image = PIL.Image.open(IMAGE_PATH)

    # convert
    image = resize_image(image, NEW_WIDTH)
    image = image.convert("L")

    data = pixels_to_ascii(image)
    # formatting
    pixel_count = len(data)
    ascii_image = "\n".join([data[index:(index+NEW_WIDTH)] for index in range(0, pixel_count, NEW_WIDTH)])

    print(ascii_image)

    # save result to "ascii_image.txt"
    with open("output.txt", "w") as f:
        f.write(ascii_image)
except Exception as e:
    print(e)
    print(IMAGE_PATH, " is not a valid path of an image.")

