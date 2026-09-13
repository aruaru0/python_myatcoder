s = input()
t = ""
for i, e in enumerate(s) :
    t += e
    if i != len(s)-1 : t += 'o'

print(t)