n, x = map(int, input().split())
a = list(map(int, input().split()))

cnt = sum([e < x for e in a])
print(cnt)