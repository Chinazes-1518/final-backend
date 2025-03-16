from PIL import Image, ImageDraw
import json

with open('../map.json', 'r') as f:
    data = json.load(f)

# for z, chunk in enumerate(data):
    # print(i)
# w, h = len(chunk[0]), len(chunk)
w, h = len(data[0]), len(data)
img = Image.new('RGB', (w, h))
draw = ImageDraw.ImageDraw(img)
for x in range(w):
    for y in range(h):
        img.putpixel((x, y), (data[h - y - 1][x], data[h - y - 1][x], data[h - y - 1][x]))
img.save('merged.png')