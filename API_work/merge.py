import json

with open('randompcs.json', 'r') as f:
    data = json.load(f)

# mtx = [[0] * 4 for _ in range(4)]

newchunks = []

for i, chunk in enumerate(data):
    edgetop = chunk[63]
    edgebottom = chunk[0]
    edgeright = [chunk[i][63] for i in range(63)]
    edgeleft = [chunk[i][0] for i in range(63)]
    newchunks.append((i, edgetop, edgebottom, edgeright, edgeleft))

print(newchunks)

