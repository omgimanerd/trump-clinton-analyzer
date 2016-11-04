#!/usr/bin/python

from analyze import *

import json
import requests
import os

def get_word_difficulty(word):
    try:
        url = 'https://twinword-word-graph-dictionary.p.mashape.com/difficulty/'
        params = {
            'entry': word
        }
        headers = {
            'X-Mashape-Key': os.environ['MASHAPE_KEY'],
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json().get('ten_degree', None)
    except:
        return None

def get_words_difficulties(words):
    difficulties = {}
    for word in words:
        difficulties[word] = get_word_difficulty(word)
        print(word, difficulties[word])
    return difficulties

if __name__ == '__main__':
    clinton = word_frequency(aggregate('clinton.json'))
    clinton_words = clinton['sorted_words']
    trump = word_frequency(aggregate('trump.json'))
    trump_words = trump['sorted_words']
    unique_words = clinton_words
    unique_words.extend(
        [word for word in trump_words if word not in clinton_words])
    difficulties = get_words_difficulties(unique_words)
    with open('difficulties.json', 'w') as f:
        json.dump(difficulties, f)
