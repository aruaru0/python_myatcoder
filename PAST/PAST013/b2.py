a, b, c, d = map(int, input().split())


# a/b < c/d 
# a/b - c/d < 0
# (ad - cb)/bd < 0

x = (a*d - c*b) / (b*d)
e = 10**-5


if -e < x and x < e :
    print("=")
elif x < 0 :
    print("<")
else :
    print(">")
