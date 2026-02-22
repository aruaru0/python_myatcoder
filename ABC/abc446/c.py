
from collections import deque


def solve() :
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    stock = deque()
    for i in range(n) :
        stock.append([a[i], i])
        cnt = b[i]
        while cnt > 0 :
            if stock[0][0] < cnt :
                cnt -= stock[0][0]
                stock.popleft()
            else :
                stock[0][0] -= cnt
                cnt = 0

        while len(stock) > 0 and i-stock[0][1] >= d :
            stock.popleft()

    tot = sum([e[0] for e in stock])
    print(tot)


t = int(input()) 
for _ in range(t) :
    solve()