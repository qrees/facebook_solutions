#!/usr/bin/env python
from collections import Counter
import sys
import heapq

tests = int(sys.stdin.readline())

def test_case():
    n, k = [int(x) for x in sys.stdin.readline().split(' ')]
    a, b, c, r = [int(x) for x in sys.stdin.readline().split(' ')]
    head = [0] * (k+1)
    heap = []
    head[0] = a
    heapq.heappush(heap, head[0])
    for i in xrange(1, k):
        head[i] = (b*head[i-1] +c ) % r
        heapq.heappush(heap, head[i])


    remain = range(k+1)
    remain = list(set(remain) - set(head[:k]))
    used_set = Counter(head[:k])
    heapq.heapify(remain)
    for i in xrange(k+1):
        smallest = heapq.heappop(remain)
        used_set[smallest] = 1
        old = head[i]
        used_set.subtract({old: 1})
        if used_set[old] == 0 and  old < k+1:
            heapq.heappush(remain, old)
        head[i] = smallest
    mod = n % (k+1)
    return head[mod]

for i in xrange(1, tests+1):
    print "Case #%i: %i" % (i, test_case())