import time
import collections


class Timer(object):
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start

    def __str__(self):
        return '(took %.03f seconds)' % self.interval


def identity(x):
    return x


def item_identity(k, v):
    return k, v


def walk(o, item_func=None, map_func=None, seq_func=None, other_func=None):
    """Recursively walk *o*, applying mutation functions.

    Performs a depth-first post-order traversal of *o*, a "tree" structure
    made of nested mappings and sequences.

    Mapping items are replaced by ``k, v = item_func(k, v)``.

    Mappings are replaced by ``m = map_func(m)``.

    Sequences are replaced by ``s = seq_func(s)``.

    Leaf nodes (values that are not mappings or sequences) are replaced by
    ``o = other_func(o)``.

    All functions default to the identity function, i.e. directly passing
    the argument(s) through.

    It is assumed that all mappings and sequences follow the basic conventions:
    ``m.__class__(m.iteritems()) == m`` and ``s.__class__(iter(s)) == s``.
    """
    item_func = item_func or item_identity
    map_func = map_func or identity
    seq_func = seq_func or identity
    other_func = other_func or identity

    def _walk(o):
        if isinstance(o, collections.Mapping):
            return map_func(o.__class__(item_func(k, _walk(v)) for k, v in o.iteritems()))
        elif isinstance(o, collections.Sequence) and not isinstance(o, basestring):
            return seq_func(o.__class__(_walk(v) for v in o))
        else:
            return other_func(o)

    return _walk(o)