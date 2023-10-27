a, b, c  = map(int, input().split())

# b*log(c) = log(c^b)
# log(a) < log(c^b)
# a < c^b

if c == 1 :
    print("No")
    exit()


x = c
for i in range(1, b):
    # print(a, x)
    if a//c < x :
        print("Yes")
        exit()
    x *= c

# print("last", a, x)
if a < x :
    print("Yes")
else:
    print("No")

