from PIL import Image
import io
import sys
import ast


# use default file containing bytes if none given via cli
file_name = "output.txt" if len(sys.argv) == 1 else sys.argv[1]

# read the string and evaluate it
with open(file_name, 'r') as f:
    file_bytes = ast.literal_eval(f.read())

image_bytes = io.BytesIO(file_bytes)
# open image based on bytes from the file & save it
image = Image.open(image_bytes)
image.save("output-img.png")


