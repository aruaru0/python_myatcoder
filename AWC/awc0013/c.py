n, k = map(int, input().split())
s = list(map(int, input().split()))

sk = s[k-1]
ans = sum(1 for x in s if x < sk)

print(ans)
