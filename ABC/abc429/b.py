n, m = map(int, input().split())
a = list(map(int, input().split()))

tot = sum(a)

for e in a :
    if tot - e == m :
        print("Yes")
        exit()
    
print("No")