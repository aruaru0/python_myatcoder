from collections import Counter

n = int(input())
a = Counter(list(map(int, input().split())))


tot = 0 
for key, value in a.items() :
    if value%2 == 1 :
        tot += key

print(tot)