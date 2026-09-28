q = int(input())
s = input()
t = input()


n, m = len(s), len(t)

o = [0] * n
for i in range(n) :
    if s[i:i+m] == t :
        o[i] = 1

sum = [0] * (n+1)
for i in range(n) :
    sum[i+1] = sum[i] + o[i]

for _ in range(q) :
    l, r = map(int, input().split())
    l -= 1
    r -= m -1
    if l < r and (sum[r] - sum[l]) >= 1 :
        print("Yes")
    else :
        print("No")

