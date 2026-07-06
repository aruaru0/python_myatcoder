from collections import deque

n = int(input())
s = input()

d = deque() 

dir = 0
for i in range(n):
    if dir == 0 :
        d.append(i+1)
    else:
        d.appendleft(i+1)
    if s[i] == 'o' : dir ^= 1

d = list(d)

if dir == 1:
    d = d[::-1]

print(*d, sep=' ')