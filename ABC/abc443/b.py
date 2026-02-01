n, k = map(int, input().split())

tot = 0
year = 0
while True :
    tot += n + year
    if tot >= k :
        break
    
    year+=1
   
print(year)
