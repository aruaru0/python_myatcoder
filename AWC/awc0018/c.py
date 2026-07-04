N, Q = map(int,input().split())
S = [input() for _ in range(N)]
alphabet = "abcdefghijklmnopqrstuvwxyz"
for _ in range(Q):
  a, b = input().split()
  alphabet = alphabet.replace(a,b)
for s in S:
  ans = []
  for c in s:
    i = ord(c) - ord('a')
    ans.append(alphabet[i])
  print("".join(ans))