N = int(input())
s = input()


ok = True
tot = 0
for i in range(N) :
    if s[i] == '(' :
        tot+=1
    else: 
        tot-=1
    if tot < 0 :
        ok = False

if tot != 0: ok = False

if ok :
    print("Yes")
else:
    print("No")