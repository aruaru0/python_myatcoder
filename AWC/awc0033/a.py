n, k = map(int, input().split())

s = input()
t = input()

cnt = sum(s[i] != t[i] for i in range(n))
print(max(0, cnt-k))