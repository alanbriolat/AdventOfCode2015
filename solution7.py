from __future__ import print_function
import collections

from util import Timer


Connection = collections.namedtuple('Connection', ['sink', 'dummy', 'right', 'op', 'left'])
Connection.__new__.__defaults__ = (None, None)  # Make last 2 arguments optional


def try_int(s):
    try:
        return int(s)
    except ValueError:
        return s


def read_connection(s):
    return Connection(*reversed(map(try_int, s.strip().split())))


class Circuit(object):
    def __init__(self, fp):
        self.connections = {}
        self.cache = {}

        for line in fp:
            c = read_connection(line)
            self.connections[c.sink] = c

    def value_at(self, x):
        if isinstance(x, int):
            return x
        if x in self.cache:
            return self.cache[x]
        c = self.connections[x]
        if c.op is None:
            val = self.value_at(c.right)
        elif c.op == 'NOT':
            val = ~self.value_at(c.right)
        elif c.op == 'AND':
            val = self.value_at(c.left) & self.value_at(c.right)
        elif c.op == 'OR':
            val = self.value_at(c.left) | self.value_at(c.right)
        elif c.op == 'LSHIFT':
            val = self.value_at(c.left) << self.value_at(c.right)
        elif c.op == 'RSHIFT':
            val = self.value_at(c.left) >> self.value_at(c.right)
        else:
            raise ValueError("Connection not understood", c)
        self.cache[x] = val
        return val


# Part 1
with Timer() as t:
    circuit1 = Circuit(open('input7.txt'))
    val1 = circuit1.value_at('a')
print('Part 1:', val1, t)

# Part 2
with Timer() as t:
    circuit2 = Circuit(open('input7.txt'))
    circuit2.connections['b'] = Connection('b', '->', val1)
    val2 = circuit2.value_at('a')
print('Part 2:', val2, t)