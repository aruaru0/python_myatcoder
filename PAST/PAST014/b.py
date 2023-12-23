d = int(input())
a = input()
b = input()


a = a[:-d-1] + a[-d:]
b = b[:-d-1] + b[-d:]


c = str(int(a) + int(b))

print(c[:-d] + "." + c[-d:])