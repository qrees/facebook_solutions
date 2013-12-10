#!/usr/bin/env python
from collections import Counter
import sys
import string

tests = int(sys.stdin.readline())


def test_case():
    line = sys.stdin.readline()
    c = Counter(line.lower().strip())

    for key in c.keys():
        if key not in string.ascii_lowercase:
            del c[key]
    i = 26
    res = 0
    for letter, count in c.most_common():
        res += count * i
        i -= 1
    return res



for i in xrange(1, tests+1):
    print "Case #%i: %i" % (i, test_case())