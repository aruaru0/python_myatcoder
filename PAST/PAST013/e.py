s = input()


cnt = 0
ok = True
for e in s :
    if e == '(' :
        cnt += 1
    else :
        cnt -= 1
    if cnt < 0 : ok = False

if cnt != 0 :
    ok = False

if ok : print("Yes")
else : print("No")