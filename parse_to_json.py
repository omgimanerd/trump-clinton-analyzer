#!/usr/bin/python

from collections import defaultdict

import json
import os
import re

def has_speaker(sentence):
    try:
        name = sentence.split(' ')[0]
        print(name, name[:-1] if name.isupper() and ':' in name else None)
        return name[:-1] if name.isupper() and ':' in name else None
    except:
        return None

def parse(filename):
    with open(filename) as f:
        data = f.read()
    data = re.sub('\[.+\]', '', data)
    data = re.sub('\s{2,}', '\n', data)
    data = data.split('\n')
    speakers = defaultdict(str)
    current_speaker = None
    for sentence in data:
        speaker = has_speaker(sentence)
        if speaker is not None:
            current_speaker = speaker
            sentence = sentence[len(speaker) + 2:]
        speakers[current_speaker] += sentence
    return speakers


if __name__ == '__main__':
    files = os.listdir('data')
    data = parse(os.path.join('data', files[0]))
    print(data.keys())
