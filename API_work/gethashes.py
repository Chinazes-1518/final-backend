from PIL import Image, ImageDraw
import json

with open('randompcs.json', 'r') as f:
    data = json.load(f)

# for z, chunk in enumerate(data):
#     # print(i)
#     img = Image.new('RGB', (64, 64))
#     draw = ImageDraw.ImageDraw(img)
#     for x in range(64):
#         for y in range(64):
#             img.putpixel((x, y), (chunk[y][x], chunk[y][x], chunk[y][x]))
#     img.save(f'img{z}.png')

for i, chunk in enumerate(data):
    # print(i, hash(tuple(list(map(tuple, chunk)))))
    if i == 7 or i == 13:
        print()
        for row in chunk:
            print('\t'.join(map(str, row)))