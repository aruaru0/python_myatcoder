def f(x,y,z):
  return x+y>z and y+z>x and z+x>y

def dfs(A):
  n=len(A)
  if n==0: return 1
  ans=0
  for j in range(1,n):
    for k in range(j+1,n):
      if f(A[0],A[j],A[k]):
        ans+=dfs(A[1:j]+A[j+1:k]+A[k+1:])
  return ans

input()
A=list(map(int,input().split()))
print(dfs(A))
