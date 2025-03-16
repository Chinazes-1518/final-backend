import json

with open('FULL.txt', 'r') as f:
    jj = []
    values = []
    for line in f.read().splitlines():
        values.append(list(map(int, line.split('\t'))))
    with open('FULL.json', 'w') as f:
        json.dump(values, f)