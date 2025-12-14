n = int(input())
s = input()

t = "".join(['o' for _ in range(len(s), n)])

print(t+s)