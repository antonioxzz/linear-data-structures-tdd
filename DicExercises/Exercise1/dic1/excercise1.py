import string
from collections import defaultdict
from itertools import chain


def read_text_file(file_path):
    lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines
file_path = 'dic1\txt_file.txt'
lines = read_text_file(file_path)


def count_words_from_file(text_from_file: str) -> dict:
    frequency = defaultdict(int)
    text_lines = text_from_file.split('\n')
    words = chain.from_iterable(line.translate(str.maketrans('', '', string.punctuation)).lower().split() for line in text_lines)
    for word in words:
        frequency[word] += 1
    
    return dict(sorted(frequency.items()))
