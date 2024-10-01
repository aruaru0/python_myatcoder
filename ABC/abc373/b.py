s = {ord(v)-ord('A'):i for i, v in enumerate(list(input()))}


tot = 0
for i in range(1, 26):
    tot += abs(s[i] - s[i-1])

print(tot)
