n, m, k = map(int, input().split())
h = list(map(int, input().split()))
b = list(map(int, input().split()))

h.sort()
b.sort()

i = j = cnt = 0
while i < n and j < m:
    if h[i] <= b[j]:
        cnt += 1
        i += 1
        j += 1
    else:
        j += 1

print("Yes" if cnt >= k else "No")

