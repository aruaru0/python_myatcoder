s = input()
t = input()

if s.replace('A', '') != t.replace('A', ''):
    print(-1)
    exit()


ans = 0
i, j = 0,0
while i < len(s) or j < len(t):
    cs = 0
    ct = 0
    
    # skip A
    while i < len(s) and s[i] == 'A':
        cs += 1
        i += 1
    
    while j < len(t) and t[j] == 'A':
        ct += 1
        j += 1
        
    ans += abs(cs - ct)
    
    i += 1
    j += 1

print(ans)
