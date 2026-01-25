Q = int(input())


vol = 0
play = False
for _ in range(Q) :
    a = int(input())
    if a == 1 :
        vol+=1
    elif a == 2 :
        vol = max(0, vol-1)
    else:
        play = not play

    if play and vol >= 3:
        print("Yes")
    else:
        print("No")