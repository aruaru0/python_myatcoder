n, s, t = map(int, input().split())

tot = sum(list(map(int, input().split())))
d = (t-s)*60

if d >= tot : print("Yes")
else : print("No")