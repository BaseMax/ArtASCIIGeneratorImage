import PIL

# Variables
# # ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
new_width = 100
image_path = "test.jpg"

# Functions
def resize_image(image, to_width=100):
    width, height = image.size
    ratio = height / width
    to_height = int(to_width * ratio)
    resized_image = image.resize((to_width, to_height))
    return resized_image

# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

# Startup
try:
    image = PIL.Image.open(image_path)

    # convert
    image = resize_image(image)
    image = image.convert("L")

    data = pixels_to_ascii(image)
    # formatting
    pixel_count = len(data)
    ascii_image = "\n".join([data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    print(ascii_image)

    # save result to "ascii_image.txt"
    with open("output.txt", "w") as f:
        f.write(ascii_image)
except:
    print(path, " is not a valid path of an image.")
