from PIL import Image
import io
import os
import sys
import ast


##file_name = "img-bytearray.txt"
file_name = "output.txt" if len(sys.argv) == 1 else sys.argv[1]
##array = array.array('B')
##array.fromfile(open(file_name, 'rb'), os.stat(file_name).st_size)
with open(file_name, 'rb') as f:
    bytes_read = ast.literal_eval(f.read())
##    bytes_read = bytes(f.read())


##image_bytes = io.BytesIO(array.tobytes())
image_bytes = io.BytesIO(bytes_read)
print('img bytes')
##print(bytes_read)
##print(image_bytes)
image = Image.open(image_bytes)
image.save("output-img.png")


