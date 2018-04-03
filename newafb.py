import PIL
import sys
from PIL import Image

im = Image.open(sys.argv[1])
w,h = im.size
pixels = []
for y in range(h):
	for x in range(w):
		r,g,b = im.getpixel((x,y))
		if r-g > 10 and r+b+g < 600:
			pixels.append((0,0,0))
		else:
			pixels.append((r,g,b))
out = Image.new('RGB',((256,256)))
#out.putdata(list(im.getdata()))
out.putdata(pixels)
out.save('output.tif')
