from __future__ import print_function
import re


# Part 1
def is_nice_1(s):
    vowels = re.compile(r'([aeiou].*){3}')
    double = re.compile(r'(.)\1')
    bad = re.compile(r'ab|cd|pq|xy')
    return vowels.search(s) and double.search(s) and not bad.search(s)
print('Part 1:', len(filter(is_nice_1, open('input5.txt'))))


# Part 2
def is_nice_2(s):
    pairs = re.compile(r'(.{2}).*\1')
    xyx = re.compile(r'(.).\1')
    return pairs.search(s) and xyx.search(s)
print('Part 2:', len(filter(is_nice_2, open('input5.txt'))))