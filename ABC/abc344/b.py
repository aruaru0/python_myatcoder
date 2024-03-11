a = []
while True :
    try :
        a.append(int(input()))
    except EOFError:
        break

a.reverse()
print(*a, sep = "\n")