n, k = map(int, input().split())
s = list(map(int, input().split()))

cnt = sum([e >= k for e in s])
print(cnt)