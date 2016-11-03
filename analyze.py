#!/usr/bin/python

from collections import defaultdict

import json
import re

def aggregate(filename):
    with open(filename) as f:
        return " ".join(json.load(f))

def get_stopwords():
    with open('data/stopwords.txt') as f:
        return f.read().strip().split('\n')

def word_frequency(string):
    string = re.sub('[^\w \']', '', string)
    string = re.sub('\s+', ' ', string)
    string = string.lower().split(' ')
    stopwords = get_stopwords()
    words = defaultdict(int)
    for word in string:
        if word not in stopwords:
            words[word] += 1
    return {
        'frequencies': words,
        'sorted': sorted(words, key=words.get)[::-1]
    }

if __name__ == '__main__':
    clinton = word_frequency(aggregate('clinton.json'))
    trump = word_frequency(aggregate('trump.json'))
    print(len(trump['sorted']))
    print(len(clinton['sorted']))
