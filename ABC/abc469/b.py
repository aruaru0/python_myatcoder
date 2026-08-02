n = int(input())
s = "x" + input() + "x"

cnt = 0
for i in range(1, len(s)-1) :
    if s[i] == 'x' and s[i-1] == 'x' and s[i+1] == 'x' :
        cnt += 1

print(cnt)