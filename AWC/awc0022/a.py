n, d, k = map(int, input().split())
w = list(map(int, input().split()))

ans = sum([e - d*k > 0 for e in w])

print(ans)
