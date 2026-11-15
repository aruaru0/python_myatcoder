n = int(input())

events = []
for i in range(n):
    s, e = map(int, input().split())
    events.append((s, 1))
    events.append((e, -1))

events.sort()

ans, cur = 0,0
for [t, e] in events:
    cur += e
    ans = max(ans, cur)


print(ans)