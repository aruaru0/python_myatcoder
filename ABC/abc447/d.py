S = input()

A = 0
AB = 0
ABC = 0

for c in S:
    if c == 'A':
        A += 1
    elif c == 'B':
        if A > 0:
            A -= 1
            AB += 1
    elif c == 'C':
        if AB > 0:
            AB -= 1
            ABC += 1

print(ABC)
