# Contest ID: abc189
# Problem ID: abc189_c ( https://atcoder.jp/contests/abc189/tasks/abc189_c )
# Title: C. Mandarin Orange
# Language: Python (3.8.2)
# Submitted: 2021-01-24 23:06:42 +0000 UTC ( https://atcoder.jp/contests/abc189/submissions/19682879 ) 

n = int(input())
a = tuple(map(int, input().split()))
a = a + (0,)

s = [-1]
ans = 0
for i, e in enumerate(a):
    while len(s) != 0:
        if a[s[-1]] > e:
            ans = max(ans, (i - 1 - s[-2]) * a[s[-1]])
            s.pop()
        else:
            break
    s.append(i)

print(ans)
