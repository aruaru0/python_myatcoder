N = int(input())
p = [e-1 for e in list(map(int, input().split()))]

tot, cur = 1, 0
while cur != N-1 :
    cur = p[cur]
    tot += 1

print(tot)