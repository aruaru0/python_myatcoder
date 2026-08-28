n, m = map(int, input().split())
d = list(map(int, input().split()))
d.append(0)

d.sort()

print(max(d[:n-m+1]))