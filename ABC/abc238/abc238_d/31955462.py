# Contest ID: abc238
# Problem ID: abc238_d ( https://atcoder.jp/contests/abc238/tasks/abc238_d )
# Title: D. AND and SUM
# Language: Python (3.8.2)
# Submitted: 2022-05-25 22:55:33 +0000 UTC ( https://atcoder.jp/contests/abc238/submissions/31955462 ) 

T = int(input())
for _ in range(T):
    a, s = map(int, input().split())   
    x = a
    y = s - a
    if y >= 0 and x&y == a :
        print("Yes")
    else :
        print("No")