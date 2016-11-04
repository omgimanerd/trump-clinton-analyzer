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
    string = re.sub('[^\w \']', ' ', string)
    string = re.sub('\s+', ' ', string)
    string = string.lower().split(' ')
    stopwords = get_stopwords()
    words = defaultdict(int)
    for word in string:
        if word not in stopwords:
            words[word] += 1
    return {
        'total_words': len(string),
        'frequencies': words,
        'sorted_words': sorted(words, key=words.get)[::-1]
    }

if __name__ == '__main__':
    clinton = word_frequency(aggregate('clinton.json'))
    clinton_freq = clinton['frequencies']
    trump = word_frequency(aggregate('trump.json'))
    trump_freq = trump['frequencies']
    print("Trump's 35 most used words:")
    for word in trump['sorted_words'][:35]:
        print("{} {}".format(word, trump_freq[word]))
    print("Clinton's 35 most used words:")
    for word in clinton['sorted_words'][:35]:
        print("{} {}".format(word, clinton_freq[word]))
    print(len(trump['sorted_words']))
    print(len(clinton['sorted_words']))
