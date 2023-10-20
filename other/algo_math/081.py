N = int(input())

x = N//10000
N %= 10000
y = N//5000
N %= 5000
z = N//1000

print(x+y+z)