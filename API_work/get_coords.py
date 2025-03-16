import json
import requests
import pathlib


def run(url):
    data = requests.get(url).json()['message']

    with open(pathlib.Path(__file__).parent.parent.joinpath('coords.json'), 'w') as f:
        json.dump(data, f)
