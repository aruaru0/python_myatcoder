L, R = map(int, input().split())

n = int(input())

for _ in range(n):
    l, r = map(int, input().split())
    L = max(L, l)
    R = min(R, r)
    print(max(0, R-L+1))