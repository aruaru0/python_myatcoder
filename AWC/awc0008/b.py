n = int(input())
h = list(map(int, input().split()))

ans = 0 
mx = 0

for x in h:
    if x > mx:
        ans += 1
        mx = x 
        
print(ans)
