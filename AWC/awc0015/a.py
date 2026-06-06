a = list(map(int, input().split()))
b = list(map(int, input().split()))


ans = sum(x*y for x, y in zip(a, b))
print(ans)