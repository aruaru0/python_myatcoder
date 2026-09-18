n, k = map(int, input().split())
p = list(map(int, input().split()))

ans = sum([e if e >= k else 0 for e in p])
print(ans)