x, y, z = map(int, input().split())

num = x - z * y  
den = z - 1 

if num >= 0 and num % den == 0:
    print("Yes")
else:
    print("No")
