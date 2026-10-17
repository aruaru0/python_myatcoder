s0 = input()
s1 = input()

for _ in range(2):
    for i in range(2):
        if s0[i] == 'A' and s1[1-i] == 'D' : 
            print("No")
            exit()
    s0, s1 = s1, s0

print("Yes")
