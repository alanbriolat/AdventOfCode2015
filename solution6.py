from __future__ import print_function
import re

import numpy as np


instruction_pattern = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')

def read_instruction(s):
    match = instruction_pattern.match(s)
    method, x1, y1, x2, y2 = match.groups()
    return method, slice(int(x1), int(x2) + 1), slice(int(y1), int(y2) + 1)


# Part 1
a1 = np.zeros((1000, 1000), dtype=bool)
for line in open('input6.txt'):
    method, xs, ys = read_instruction(line)
    if method == 'toggle':
        value = np.logical_not(a1[xs, ys])
    elif method == 'turn on':
        value = True
    else:
        value = False
    a1[xs, ys] = value
print('Part 1:', np.count_nonzero(a1))

# Part 2
a2 = np.zeros((1000, 1000), dtype=int)
for line in open('input6.txt'):
    method, xs, ys = read_instruction(line)
    if method == 'toggle':
        value = 2
    elif method == 'turn on':
        value = 1
    else:
        value = -1
    a2[xs, ys] += value
    a2[a2 < 0] = 0
print('Part 2:', np.sum(a2))