n, q = map(int, input().split())
a = list(map(int, input().split()))

c = [(a[i], i + 1) for i in range(n)]
c.sort(key=lambda x: x[0])

out = []
for _ in range(q):
    k = int(input())
    b = list(map(int, input().split())) if k > 0 else []
    rem = set(b)

    ans = None

    for i in range(k + 1):
        val, idx = c[i]
        if idx not in rem:
            ans = val
            break

    print(ans)
