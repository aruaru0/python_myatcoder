# Contest ID: abc287
# Problem ID: abc287_d ( https://atcoder.jp/contests/abc287/tasks/abc287_d )
# Title: D. Match or Not
# Language: Python (3.8.2)
# Submitted: 2023-02-01 05:03:44 +0000 UTC ( https://atcoder.jp/contests/abc287/submissions/38519924 ) 

s = input()
t = input()

n = len(s)
m = len(t)

# 先頭からの一致個数
l = 0
for i in range(m):
    if s[i] == "?" or t[i] == "?" or s[i] == t[i]:
        l += 1
    else:
        break

# 末尾からの一致個数
r = 0
for i in range(m):
    if s[n - 1 - i] == "?" or t[m - 1 - i] == "?" or s[n - 1 - i] == t[m - 1 - i]:
        r += 1
    else:
        break

# 先頭と末尾の一致している範囲内かどうか
for i in range(m + 1):
    if i <= l and m - i <= r:
        print("Yes")
    else:
        print("No")
