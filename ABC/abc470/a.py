n = int(input())

s = ["Fizz" if i%3 == 0 else i for i in range(1, n+1)]

for e in s :
    print(e)
