n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = [x-1 for x in a]
b = [x-1 for x in b]

ans = "Yes"
for i, e in enumerate(a) :
    if b[e] != i : 
        ans = "No"
        break

print(ans)