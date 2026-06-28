s = input()

ne, nw = 0,0

for e in s :
    if e == 'E':
        ne+=1
    else :
        nw += 1

if ne > nw :
    print("East")
else:
    print("West")