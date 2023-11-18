from collections import defaultdict

s = input()

x = defaultdict(int)

for i in range(len(s)-1) :
    x[s[i:i+2]] += 1
    # print(s[i:i+2])



y = [[x[i], i] for i in x]
y.sort()

pos = len(y) - 1
val = y[pos][0]

while pos > 0 and val == y[pos-1][0] :
    pos -= 1

# print(y)
# print(pos, val)
print(y[pos][1])