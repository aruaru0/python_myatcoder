x, a, b, c = map(int, input().split())


# x/a + c > x/b 
# bx + abc > ax

kame = a*x
usagi = b*x + a*b*c


if kame == usagi :
    print("Tie")
elif kame < usagi :
    print("Tortoise")
else :
    print("Hare")
