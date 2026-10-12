n = int(input())
s = input()

ans, cnt = 0,0
for e in s:
    if e == 'R' : cnt+=1
    else: cnt=0
    ans = max(ans, cnt)

print(ans)