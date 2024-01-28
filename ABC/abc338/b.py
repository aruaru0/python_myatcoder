from collections import defaultdict

s = list(input())

m = defaultdict(int)

for e in s :
    m[e]+=1

l = [(-m[e], e) for e in m]
l = sorted(l)

# print(l)
print(l[0][1])