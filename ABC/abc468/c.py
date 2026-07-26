from itertools import permutations

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

a = [i+1 for i in range(n)]

cnt = 0

for e in permutations(a) :
    if p < e and e < q : cnt+=1

print(cnt)
