from collections import defaultdict
from copy import copy

n, m = map(int, input().split())

p = [0] * n 
sel = [defaultdict(int) for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    p[a] += 1
    sel[a][b]+=1


class P :
    cnt = -1
    idx = -1


top1, top2 = P(), P()
for i in range(n) : 
    if top1.cnt < p[i] :
        top2 = copy(top1)
        top1.cnt = p[i]
        top1.idx = i
    elif top2.cnt < p[i] :
        top2.cnt = p[i]
        top2.idx = i


for i in range(n) :
    top = copy(top1)
    if top1.idx == i :
        top = copy(top2)
    for idx, cnt in sel[i].items() :
        newCnt = cnt + p[idx]
        # print(idx, cnt, p, newCnt, "top", top.idx, top.cnt)
        if newCnt == top.cnt and idx < top.idx :
            top.cnt = newCnt
            top.idx = idx
        elif newCnt > top.cnt :
            top.cnt = newCnt
            top.idx = idx
    print(top.idx+1)


