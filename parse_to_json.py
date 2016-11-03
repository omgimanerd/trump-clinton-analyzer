#!/usr/bin/python

from collections import defaultdict

import json
import os
import re

def has_speaker(sentence):
    try:
        name = sentence.split(' ')[0]
        return name[:-1] if name.isupper() and ':' in name else None
    except:
        return None

def parse(filename):
    with open(filename) as f:
        data = f.read()
    data = re.sub('\[.+\]', '', data)
    data = re.sub('\s{2,}', '\n', data)
    data = data.split('\n')
    speakers = defaultdict(list)
    current_speaker = None
    for sentence in data:
        speaker = has_speaker(sentence)
        if speaker is not None:
            current_speaker = speaker
            sentence = sentence[len(speaker) + 2:]
        speakers[current_speaker].append(sentence)
    return speakers

def get_trump_clinton(files):
    trump = []
    clinton = []
    for f in files:
        data = parse(f)
        trump += data['TRUMP']
        clinton += data['CLINTON']
    return {
        'TRUMP': trump,
        'CLINTON': clinton
    }

if __name__ == '__main__':
    data = get_trump_clinton([os.path.join('data', f) for f in os.listdir('data')])
    with open('trump.json', 'w') as trump:
        json.dump(data['TRUMP'], trump)
    with open('clinton.json', 'w') as clinton:
        json.dump(data['CLINTON'], clinton)
