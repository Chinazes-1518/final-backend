import json
import requests
import pathlib


def run(url):
    data = requests.get(url).json()['message']
    data['sender'][0] -= 3
    data['sender'][1] -= 3
    data['listener'][0] -= 3
    data['listener'][1] -= 3
    with open(pathlib.Path(__file__).parent.parent.joinpath('coords.json'), 'w') as f:
        json.dump(data, f)
