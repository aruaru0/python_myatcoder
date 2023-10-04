N, K = map(int, input().split())
a = list(map(int, input().split()))
tot = sum(a)

if tot > K : 
    print("No")
    exit()

tot -= K
if tot%2 == 0 :
    print("Yes")
    exit()


print("No")