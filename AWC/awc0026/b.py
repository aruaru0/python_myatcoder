n, k = map(int, input().split())
a = list(map(int, input().split()))


tk, ao = 0,0
for e in a:
    if tk+e <= k :
        tk+=e
    else:
        ao+=e

if tk==ao : 
    print("Draw")
elif tk > ao :
    print("Takahashi")
else:
    print("Aoki")