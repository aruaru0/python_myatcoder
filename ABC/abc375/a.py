n = int(input())
s = input()

cnt = 0
for i in range(n-2):
    if s[i] == '#' and s[i+1] == '.' and s[i+2] == '#' :
        cnt += 1

print(cnt)