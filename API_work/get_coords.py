import json
import requests


def run(url):
    data = requests.get(url).json()['message']
    with open('../coords.json', 'w') as f:
        json.dump(data, f)