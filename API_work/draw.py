from PIL import Image, ImageDraw
import json

with open('randompcs.json', 'r') as f:
    data = json.load(f)

for z, chunk in enumerate(data):
    # print(i)
    w, h = len(chunk[0]), len(chunk)
    img = Image.new('RGB', (w, h))
    draw = ImageDraw.ImageDraw(img)
    for x in range(w):
        for y in range(h):
            img.putpixel((x, y), (chunk[y][x], chunk[y][x], chunk[y][x]))
    img.save(f'img{z}.png')