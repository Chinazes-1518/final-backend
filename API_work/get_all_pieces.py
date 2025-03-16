import requests
import json
import time


def download_unique_pieces(url):
    # url = 'https://olimp.miet.ru/ppo_it/api'

    pcs = set()

    hashes = []

    while len(pcs) != 16:
        data = requests.get(url).json()['message']['data']
        data2 = tuple(list(map(tuple, data)))
        # print(hash(data2))
        # pcs.add(data2)
        hh = hash(data2)
        if hh not in hashes:
            hashes.append(hh)
            pcs.add(data2)

    with open('randompcs.json', 'w') as f:
        json.dump(list(pcs), f)
    
