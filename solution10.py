from __future__ import print_function
import re

from util import Timer


matcher = re.compile(r'(\d)\1*')

def replacement(matchobj):
    value = matchobj.group(0)
    return str(len(value)) + value[0]


input = "1321131112"

# Part 1
with Timer() as t:
    value1 = input
    for i in xrange(40):
        value1 = matcher.sub(replacement, value1)
print('Part 1:', len(value1), t)

# Part 2
with Timer() as t:
    value2 = input
    for i in xrange(50):
        value2 = matcher.sub(replacement, value2)
print('Part 2:', len(value2), t)