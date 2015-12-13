from __future__ import print_function
from itertools import permutations
from collections import defaultdict
import re

from util import Timer, pairwise


cost = defaultdict(dict)
for line in open('input13.txt'):
    match = re.match(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).', line)
    src, sign, length, tgt = match.groups()
    length = int(length)
    if sign == 'lose':
        length = -length
    cost[src][tgt] = length
people = set(cost)


def happiness_change(arrangement):
    arrangement += arrangement[0:1]
    return (sum(cost[a][b] for a, b in pairwise(arrangement)) +
            sum(cost[a][b] for a, b in pairwise(reversed(arrangement))))


# Part 1
with Timer() as t:
    results1 = [(happiness_change(_), _) for _ in permutations(people)]
print('Part 1:', sorted(results1, key=lambda x: x[0], reverse=True)[0], t)

# Part 2
for other in people:
    cost['Me'][other] = cost[other]['Me'] = 0
people.add('Me')
with Timer() as t:
    results2 = [(happiness_change(_), _) for _ in permutations(people)]
print('Part 2:', sorted(results2, key=lambda x: x[0], reverse=True)[0], t)