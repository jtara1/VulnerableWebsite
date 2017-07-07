import sys
import io
from PIL import Image


if len(sys.argv) < 2:
	raise Exception("no file name given via command line interface")

file_name = sys.argv[1]
output_file_name = sys.argv[2] if len(sys.argv) > 2 else "output.txt"

# save bytes
with open(file_name, 'rb') as infile:
	with open(output_file_name, 'w') as outfile:
		outfile.write(str(bytes(infile.read())))

