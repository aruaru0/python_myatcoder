a, b, c, d = map(int, input().split())


# a/b < c/d 
# a/b - c/d < 0
# (ad - cb)/bd < 0

x = (a*d - c*b)
y = b*d

if x == 0: 
    print("=")
elif (x > 0 and y > 0) or (x < 0 and y < 0) :
    print(">")
else:
    print("<") 