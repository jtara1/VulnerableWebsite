import sys
import io
from PIL import Image


if len(sys.argv) < 2:
	raise Exception("no file name given via command line interface")

file_name = sys.argv[1]

# save bytes
with open(file_name, 'rb') as infile:
	with open('output.txt', 'w') as outfile:
		img_bytes = infile.read()
		outfile.write(str(bytes(img_bytes)))

# save new image with the bytes
# image = Image.open(io.BytesIO(img_bytes))
# image.save('new_img.png')
