n = int(input())
s = input()

p = [i+1 for i in range(n) if s[i] == 'x']
idx = 0
for _ in range(n) :
    if idx == len(p) :
        print(n)
    else :
        print(p[idx])
        idx+=1