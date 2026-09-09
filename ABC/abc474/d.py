n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


ok = False
for e, v in zip(a, b) :
    if e > v : 
        ok = True
        break

if not ok :
    print("No")
else :
    print("Yes")
    inf = int(1e18)
    ans = [inf if e > v else 1 for e, v in zip(a, b)]
    print(*ans)