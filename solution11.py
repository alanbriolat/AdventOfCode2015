from __future__ import print_function
from itertools import islice

from util import Timer


def increment(s, pos=None):
    if pos is None:
        pos = len(s) - 1
    c = chr(ord(s[pos]) + 1)
    if c > 'z':
        s = increment(s, pos - 1)
        c = 'a'
    return s[:pos] + c + s[pos+1:]


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


alphabet = 'abcdefghijklmnopqrstuvwxyz'


def good_pw(s):
    return (any(''.join(x) in s for x in window(alphabet, 3)) and
            not {'i', 'o', 'l'} & set(s) and
            len(filter(lambda x: x+x in s, alphabet)) >= 2)


input = 'hepxcrrq'

# Part 1
with Timer() as t:
    pw1 = increment(input)
    while not good_pw(pw1):
        pw1 = increment(pw1)
print('Part 1:', pw1, t)

# Part 2
with Timer() as t:
    pw2 = increment(pw1)
    while not good_pw(pw2):
        pw2 = increment(pw2)
print('Part 2:', pw2, t)