from __future__ import print_function
import json

from util import walk


# Part 1
class AccumulatingIntParser(object):
    def __init__(self):
        self.total = 0

    def __call__(self, num_str):
        value = int(num_str)
        self.total += value
        return value

acc1 = AccumulatingIntParser()
decoder1 = json.JSONDecoder(parse_int=acc1)
obj1 = decoder1.decode(open('input12.txt').read())
print('Part 1:', acc1.total)

# Part 1, attempt 2
obj = json.load(open('input12.txt'))
value = walk(obj,
             map_func=lambda x: sum(_ for _ in x.values() if isinstance(_, int)),
             seq_func=lambda x: sum(_ for _ in x if isinstance(_, int)))
print('Part 1:', value)

# Part 2
obj = json.load(open('input12.txt'))
value = walk(obj,
             map_func=lambda x: 0 if "red" in x.values() else sum(_ for _ in x.values() if isinstance(_, int)),
             seq_func=lambda x: sum(_ for _ in x if isinstance(_, int)))
print('Part 2:', value)