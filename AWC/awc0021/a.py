n, k = map(int, input().split())

cnt = 0
for _ in range(n) :
    x = list(map(int, input().split()))
    cnt += sum([e >= k for e in x[1:]])

print(cnt)