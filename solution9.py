from __future__ import print_function
from itertools import permutations
from collections import defaultdict
import re

from util import Timer, pairwise


dist = defaultdict(dict)
for line in open('input9.txt'):
    match = re.match(r'(\w+) to (\w+) = (\d+)', line)
    src, tgt, length = match.groups()
    dist[src][tgt] = dist[tgt][src] = int(length)
places = set(dist)

# Part 1
with Timer() as t:
    results = [(sum(dist[a][b] for a, b in pairwise(path)), path) for path in permutations(places)]
print('Part 1:', sorted(results, key=lambda x: x[0])[0], t)
# Part 2
print('Part 2:', sorted(results, key=lambda x: x[0], reverse=True)[0], t)