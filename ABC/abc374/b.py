s = input()
t = input()

if s == t :
    print("0")
    exit()

for i in range(min(len(s), len(t))) :
    if s[i] != t[i] :
        print(i+1)
        exit()

print(min(len(s), len(t)) +1)