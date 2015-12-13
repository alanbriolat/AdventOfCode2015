from __future__ import print_function
from collections import Counter


# Part 1
c1 = Counter(open('input1.txt').read())
print('Part 1:', c1['('] - c1[')'])

# Part 2
c2 = Counter()
for i, x in enumerate(open('input1.txt').read(), start=1):
    c2[x] += 1
    if c2['('] - c2[')'] == -1:
        break
print('Part 2:', i)