from __future__ import print_function
from collections import Counter


def move(pos, direction):
    x, y = pos
    return {
        '^': (x, y + 1),
        'v': (x, y - 1),
        '<': (x - 1, y),
        '>': (x + 1, y),
    }[direction]


def run(pos, moves):
    yield pos
    for m in moves:
        pos = move(pos, m)
        yield pos


moves = open('input3.txt').read()

# Part 1
c1 = Counter(run((0, 0), moves))
print('Part 1:', len(c1))

# Part 2
c2 = Counter(run((0, 0), moves[0::2]))
c2.update(run((0, 0), moves[1::2]))
print('Part 2:', len(c2))