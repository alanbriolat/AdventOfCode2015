from __future__ import print_function
import hashlib
import itertools

from util import Timer


secret = 'iwrupvqb'

# Part 1
with Timer() as t:
    for i in itertools.count(1):
        hash = hashlib.md5(secret + str(i)).hexdigest()
        if hash.startswith('00000'):
            break
print('Part 1:', i, t)

# Part 2
with Timer() as t:
    for i in itertools.count(1):
        hash = hashlib.md5(secret + str(i)).hexdigest()
        if hash.startswith('000000'):
            break
print('Part 2:', i, t)