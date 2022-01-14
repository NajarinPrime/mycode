#!/usr/bin/env python3

import pandas as pd

import requests

def main():
    pokedex_url: 'https://raw.githubusercontent.com/csfeeser/Python/master/pokedex.txt'

    response = requests.get(url=pokedex_url).csv()

    print(response)

main()
