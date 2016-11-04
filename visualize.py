#!/usr/bin/python

from analyze import *

import json
import matplotlib.pyplot as pyplot

def get_word_difficulties():
    with open('difficulties.json') as f:
        return json.load(f)

def plot_difficulty_distribution(trump_words, clinton_words):
    difficulties = get_word_difficulties()
    trump_y = [0 for x in range(10)]
    trump_total = 0
    for word in trump_words:
        difficulty = difficulties.get(word, None)
        if difficulty is not None:
            assert difficulty >= 1 and difficulty <= 10
            trump_y[difficulty - 1] += 1
            trump_total += 1
    trump_x = list(range(1, 11))
    trump_y = list(map(lambda y: y / trump_total, trump_y))
    clinton_y = [0 for x in range(10)]
    clinton_total = 0
    for word in clinton_words:
        difficulty = difficulties.get(word, None)
        if difficulty is not None:
            assert difficulty >= 1 and difficulty <= 10
            clinton_y[difficulty - 1] += 1
            clinton_total += 1
    clinton_x = list(range(1, 11))
    clinton_y = list(map(lambda y: y / clinton_total, clinton_y))
    trump_plot = pyplot.plot(trump_x, trump_y, 'r-', label='Trump')
    clinton_plot = pyplot.plot(clinton_x, clinton_y, 'b-', label='Clinton')
    pyplot.title('Distribution of Word Difficulties')
    pyplot.xlabel('Difficulty of Word')
    pyplot.ylabel('Percentage of Total Words')
    pyplot.legend(loc='upper right')
    pyplot.show()

def get_average_difficulty(words):
    difficulties = get_word_difficulties()
    difficulty_total = 0
    word_total = 0
    for word in words:
        difficulty = difficulties.get(word, None)
        if difficulty is not None:
            assert difficulty >= 1 and difficulty <= 10
            difficulty_total += difficulty
            word_total += 1
    return difficulty_total / word_total

if __name__ == '__main__':
    clinton = word_frequency(aggregate('clinton.json'))
    clinton_words = clinton['sorted_words']
    trump = word_frequency(aggregate('trump.json'))
    trump_words = trump['sorted_words']
    print('Clinton\'s average difficulty: {} '.format(
        get_average_difficulty(clinton_words)))
    print('Trump\'s average difficulty: {} '.format(
        get_average_difficulty(trump_words)))
    plot_difficulty_distribution(trump_words, clinton_words)
