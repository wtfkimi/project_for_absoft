import requests

class LinksRequest:
    '''This module genetate links'''
    cats = requests.get('https://aws.random.cat/meow')
    cat_json = cats.json()
    CAT = cat_json['file']

    woof = requests.get('https://random.dog/woof.json')
    woof_json = woof.json()
    WOOF = woof_json['url']

    floof = requests.get('https://randomfox.ca/floof/')
    floof_json = floof.json()
    FLOOF_LINK = floof_json['link']
    FLOOF_IMG = floof_json['image']