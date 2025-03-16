import json

with open('merged.json', 'r') as f:
    data = json.load(f)

del data[0]
del data[0]
del data[0]

del data[len(data) - 1]
del data[len(data) - 1]
del data[len(data) - 1]

data2 = []

for row in data:
    data2.append(row[3:-3])

with open('../map.json', 'w') as f:
    json.dump(data2, f)