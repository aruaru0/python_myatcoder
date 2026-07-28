S = input().strip()
N = len(S)
ans = 0

for c in range(2 * N - 1):
    l = c // 2
    r = (c + 1) // 2
    mm = 0
    while l >= 0 and r < N:
        if l < r and S[l] != S[r]:
            mm += 1
        if mm > 1:
            break
        ans += 1
        l -= 1
        r += 1

print(ans)
