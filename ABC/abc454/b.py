n, m = map(int, input().split())
f = list(map(int, input().split()))

s = set(f)

if len(s) == n:
    print("Yes")
else:
    print("No")

if len(s) == m:
    print("Yes")
else:
    print("No")
