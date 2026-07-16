n, k = map(int, input().split())

cnt = 0
for _ in range(n) :
    d = sum(e == '!' for e in list(input()))
    if d >= k : cnt += 1

print(cnt)