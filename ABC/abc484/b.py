k = int(input())
a = list(map(int, input().split()))

if 9 not in a :
    print(-1)
else:
    print(min(a))