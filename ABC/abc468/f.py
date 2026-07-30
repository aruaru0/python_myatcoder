#!/usr/bin/env python3
import bisect

n = int(input())
p = list(map(int, input().split()))

cur = 0
pref = 0
tails = []

for v in p:
    if v > cur:
        cur = v
        pref += 1
    else:
        i = bisect.bisect_left(tails, v)
        if i == len(tails):
            tails.append(v)
        else:
            tails[i] = v

print(pref + len(tails))
