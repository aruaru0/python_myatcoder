n = int(input())
a = list(map(int, input().split()))

ans = sum(a[::2])

print(ans)