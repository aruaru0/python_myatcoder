x, y = input().split()
mp = {"Ocelot": 0, "Serval": 1, "Lynx": 2}
if mp[x] >= mp[y]:
    print("Yes")
else:
    print("No")

